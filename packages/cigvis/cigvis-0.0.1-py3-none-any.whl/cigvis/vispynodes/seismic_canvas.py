# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2023, modified by Jintao Li.
# Computational and Interpretation Group (CIG),
# University of Science and Technology of China (USTC)
#
# Copyright (C) 2019 Yunzhi Shi @ The University of Texas at Austin.
# All rights reserved.
# Distributed under the MIT License. See LICENSE for more info.
# -----------------------------------------------------------------------------

import vispy
from vispy.util import keys
from vispy.gloo.util import _screenshot
from vispy.visuals import MeshVisual, CompoundVisual
from vispy.visuals.filters import ShadingFilter

import cigvis
from .xyz_axis import XYZAxis
from .axis_aligned_image import AxisAlignedImage
from .fixed_image import FixedImage


class SeismicCanvas(vispy.scene.SceneCanvas):
    """
    A canvas that automatically draw all contents in a 3D seismic
    visualization scene, which may include 3D seismic volume slices, axis
    legend, colorbar, etc.

    Parameters:

    """

    def __init__(
        self,
        size=(800, 720),
        bgcolor='white',
        visual_nodes=[],
        xyz_axis=None,
        colorbar=None,
        colorbar_region_ratio=0.125,
        scale_factor=None,
        center=None,
        fov=45,
        azimuth=50,
        elevation=30,
        zoom_factor=1.0,
        axis_scales=(1.0, 1.0, 1.0),
        auto_range=True,
        savedir='./',
        title='Seismic3D',
    ):

        self.pngDir = savedir

        # Create a SceneCanvas obj and unfreeze it so we can add more
        # attributes inside.
        vispy.scene.SceneCanvas.__init__(self,
                                         title=title,
                                         keys='interactive',
                                         size=size,
                                         bgcolor=bgcolor)
        self.unfreeze()

        # self.dpi = 200

        # Create a Grid widget on the canvas to host separate Viewbox (e.g.,
        # 3D image on the left panel and colorbar to the right).
        self.grid = self.central_widget.add_grid()

        # Attach a ViewBox to a grid and initiate the camera with the given
        # parameters.
        self.view = self.grid.add_view(row=0, col=0)
        if not (auto_range or (scale_factor and center)):
            raise ValueError("scale_factor and center cannot be None" +
                             " when auto_range=False")
        self.camera = vispy.scene.cameras.TurntableCamera(
            scale_factor=scale_factor,
            center=center,
            fov=fov,
            azimuth=azimuth,
            elevation=elevation)
        self.fov = fov
        self.azimuth = azimuth
        self.elevation = elevation
        self.view.camera = self.camera

        # scale axis
        axis_scales = list(axis_scales)
        for i, r in enumerate(cigvis.is_axis_reversed()):
            axis_scales[i] *= (1 - 2 * r)
        self.axis_scales = axis_scales
        self.camera._flip_factors = self.axis_scales.copy()

        # Attach all main visual nodes (e.g. slices, meshs, volumes) to the ViewBox.
        self.nodes = visual_nodes
        for node in self.nodes:
            self.view.add(node)

        # Connect the XYZAxis visual to the primary ViewBox.
        if xyz_axis is not None:
            # Set the parent to view, instead of view.scene, so that this legend will
            # stay at its location on the canvas, and won't rotate away.
            xyz_axis.parent = self.view
            xyz_axis.canvas_size = self.size
            self.events.resize.connect(xyz_axis.on_resize)
            xyz_axis.highlight.parent = self.view
            xyz_axis._update_axis()
            self.events.mouse_move.connect(xyz_axis.on_mouse_move)

        # Create a secondary ViewBox to host the Colorbar visual.
        # Make it solid background, image from primary ViewBox shall be
        # blocked if overlapping.
        if colorbar is not None:  # move to here
            self.view2 = self.grid.add_view(row=0, col=1, bgcolor=self.bgcolor)
            self.view2.width_max = colorbar_region_ratio * self.size[0]
            self.view2.interactive = False  # disable so that it won't be selectable
            # Connect the Colorbar visual to the secondary ViewBox.

            # if colorbar is not None:
            colorbar.parent = self.view2

            # Pad a gap horizontally, and put the bar in the middle vertically.
            # colorbar.pos = (min(colorbar.bar_size), self.size[1] / 2)
            colorbar.pos = (0, self.size[1] / 2)
            colorbar.canvas_size = self.size
            self.events.resize.connect(colorbar.on_resize)

        # Manage the selected visual node.
        self.drag_mode = False
        self.selected = None  # no selection by default
        self.hover_on = None  # visual node that mouse hovers on, None by default

        # Automatically set the range of the canvas, display, and wrap up.
        if auto_range: self.camera.set_range()
        # Record the scale factor for a consistent camera reset.
        self.scale_factor = self.camera.scale_factor
        # Zoom in or out after auto range setting.
        self.zoom_factor = zoom_factor
        self.camera.scale_factor /= self.zoom_factor
        self.freeze()
        self._attach_light()

    def on_mouse_press(self, event):
        if keys.ALT in event.modifiers and event.button == 1:
            self.view.interactive = False
            hover_on = self.visual_at(event.pos)
            if hover_on is not None:
                tf1 = hover_on.transforms.get_transform(map_to="canvas")
                tf2 = hover_on.transform
                pos = event.pos
                # pos = tf1.imap(event.pos)
                pos = tf2.imap((pos[0], 0, pos[1]))
                print(f'[{pos[0]:.3f}, {pos[1]:.3f}, {pos[2]:.3f}, {pos[3]:.3f}]')
                self.view.interactive = True

        # Hold <Ctrl> to enter drag mode or press <d> to toggle.
        if keys.CONTROL in event.modifiers or self.drag_mode:
            # Temporarily disable the interactive flag of the ViewBox because it
            # is masking all the visuals. See details at:
            # https://github.com/vispy/vispy/issues/1336
            self.view.interactive = False
            hover_on = self.visual_at(event.pos)

            if event.button == 1 and self.selected is None:
                # If no previous selection, make a new selection if cilck on a valid
                # visual node, and highlight this node.
                if hover_on is not None and not isinstance(
                        hover_on, FixedImage):
                    self.selected = hover_on
                    self.selected.highlight.visible = True
                    # Set the anchor point on this node.
                    self.selected.set_anchor(event)

                # Nothing to do if the cursor is NOT on a valid visual node.

            # Reenable the ViewBox interactive flag.
            self.view.interactive = True

    def on_mouse_release(self, event):
        # Hold <Ctrl> to enter drag mode or press <d> to toggle.
        if keys.CONTROL in event.modifiers or self.drag_mode:
            if self.selected is not None:
                # Erase the anchor point on this node.
                self.selected.anchor = None
                # Then, deselect any previous selection.
                self.selected = None

    def on_mouse_move(self, event):
        # Hold <Ctrl> to enter drag mode or press <d> to toggle.
        if keys.CONTROL in event.modifiers or self.drag_mode:
            # Temporarily disable the interactive flag of the ViewBox because it
            # is masking all the visuals. See details at:
            # https://github.com/vispy/vispy/issues/1336
            self.view.interactive = False
            hover_on = self.visual_at(event.pos)

            if event.button == 1:
                if self.selected is not None:
                    self.selected.drag_visual_node(event)
            else:
                # If the left cilck is released, update highlight to the new visual
                # node that mouse hovers on.
                if hover_on != self.hover_on:
                    if self.hover_on is not None:  # de-highlight previous hover_on
                        self.hover_on.highlight.visible = False
                    self.hover_on = hover_on
                    if self.hover_on is not None:  # highlight the new hover_on
                        self.hover_on.highlight.visible = True

            # Reenable the ViewBox interactive flag.
            self.view.interactive = True

    def on_key_press(self, event):
        # Hold <Ctrl> to enter drag mode.
        if keys.CONTROL in event.modifiers:
            # TODO: I cannot get the mouse position within the key_press event ...
            # so it is not yet implemented. The purpose of this event handler
            # is simply trying to highlight the visual node when <Ctrl> is pressed
            # but mouse is not moved (just nicer interactivity), so not very
            # high priority now.
            # print(event)
            pass

        # Press <Space> to reset camera.
        if event.text == ' ':
            self.camera.fov = self.fov
            self.camera.azimuth = self.azimuth
            self.camera.elevation = self.elevation
            self.camera.set_range()
            self.camera.scale_factor = self.scale_factor
            self.camera.scale_factor /= self.zoom_factor
            self.camera._flip_factors = self.axis_scales
            self.camera._update_camera_pos()

            for child in self.view.children:
                if type(child) == XYZAxis:
                    child._update_axis()

        # Press <s> to save a screenshot.
        if event.text == 's':
            screenshot = _screenshot()
            # screenshot = self.render()
            vispy.io.write_png(self.pngDir + self.title + '.png', screenshot)

        # Press <d> to toggle drag mode.
        if event.text == 'd':
            if not self.drag_mode:
                self.drag_mode = True
                self.camera.viewbox.events.mouse_move.disconnect(
                    self.camera.viewbox_mouse_event)
            else:
                self.drag_mode = False
                self._exit_drag_mode()
                self.camera.viewbox.events.mouse_move.connect(
                    self.camera.viewbox_mouse_event)

        # Press <a> to get the parameters of all visual nodes.
        if event.text == 'a':
            print("===== All useful parameters ====")
            # Canvas size.
            print("Canvas size = {}".format(self.size))
            # Collect camera parameters.
            print("Camera:")
            camera_state = self.camera.get_state()
            for key, value in camera_state.items():
                print(" - {} = {}".format(key, value))
            print(" - {} = {}".format('zoom factor', self.zoom_factor))

            # axis scales
            factors = list(self.camera._flip_factors)
            print(f'axes scale ratio (< 0 means axis reversed):')
            print(f' - x: {factors[0]}')
            print(f' - y: {factors[1]}')
            print(f' - z: {factors[2]}')

            # Collect slice parameters.
            print("Slices:")
            pos_dict = {'x': [], 'y': [], 'z': []}
            for node in self.view.scene.children:
                if type(node) == AxisAlignedImage:
                    pos = node.pos
                    pos_dict[node.axis].append(pos)
            for axis, pos in pos_dict.items():
                print(" - {}: {}".format(axis, pos))
            # Collect the axis legend parameters.
            for node in self.view.children:
                if type(node) == XYZAxis:
                    print("XYZAxis loc = {}".format(node.loc))

        # zoom in z axis, press <z>
        if event.text == 'z':
            factors = list(self.camera._flip_factors)
            factors[2] += (0.02 * (1 - 2 * cigvis.is_z_reversed()))
            self.camera._flip_factors = factors
            self.camera._update_camera_pos()
            self.update()

        # zoom out z axis, press <Z>, i.e. <Shift>+<z>
        if event.text == 'Z':
            factors = list(self.camera._flip_factors)
            factors[2] -= (0.02 * (1 - 2 * cigvis.is_z_reversed()))
            self.camera._flip_factors = factors
            self.camera._update_camera_pos()
            self.update()

        # zoom in fov, press <f>
        if event.text == 'f':
            self.camera.fov += 5

        # zoom out fov, press <F>
        if event.text == 'F':
            self.camera.fov -= 5

    def on_key_release(self, event):
        # Cancel selection and highlight if release <Ctrl>.
        if keys.CONTROL not in event.modifiers:
            self._exit_drag_mode()

    def _exit_drag_mode(self):
        if self.hover_on is not None:
            self.hover_on.highlight.visible = False
            self.hover_on = None
        if self.selected is not None:
            self.selected.highlight.visible = False
            self.selected.anchor = None
            self.selected = None

    def _attach_light(self):
        """
        change light direction when status of camera changed
        """
        for node in self.nodes:
            if isinstance(node, CompoundVisual):
                if hasattr(node, 'meshs'):
                    node.meshs[0].shading_filter.light_dir = (-1, -1, 1)

        initial_light_dir = self.view.camera.transform.imap((-1, -1, 1, 0))

        @self.view.scene.transform.changed.connect
        def on_transform_change(event):
            transform = self.view.camera.transform
            for node in self.nodes:
                # if isinstance(node, MeshVisual):
                #     node.shading_filter.light_dir = transform.map(
                #         initial_light_dir)[:3]
                if isinstance(node, CompoundVisual):
                    if hasattr(node, 'meshs'):
                        node.meshs[0].shading_filter.light_dir = transform.map(
                            initial_light_dir)[:3]
