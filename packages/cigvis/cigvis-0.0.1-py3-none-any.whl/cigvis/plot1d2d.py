# Copyright (c) 2023 Jintao Li.
# Computational and Interpretation Group (CIG),
# University of Science and Technology of China (USTC).
# All rights reserved.
"""
Functions for drawing 1D/2D data using matplotlib
----------------------------------------------------

This is 
"""

from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtf
import cigvis
from cigvis import colormap

################## For traces plot #############


def plot1d(data: np.ndarray or List,
           dt: float = 1,
           beg: float = 0,
           orient: str = 'v',
           figsize: Tuple or List = (2, 8),
           title: str = None,
           axis_label: str = None,
           value_label: str = 'Amplitude',
           fill_up=None,
           fill_down=None,
           fill_color=None,
           c='#1f77b4',
           save=None):
    """
    plot a 1d trace

    Parameters
    -----------
    data : array-like
        input data
    dt : float
        interval of data, such as 0.2 means data sampling in 0.2, 0.4, ...
    beg : float
        begin sampling, beg=1.6, dt=0.2 means data sampling is 1.6, 1.8, ..
    orient : Optinal ['v', 'h']
        orientation of the data, 'v' means vertical, 'h' means horizontal
    figsize : Tuple or List
        (value-axis length, sampling-axis length)
    title : str
        title
    axis_label : str
        sampling-axis label
    value_label : str
        value axis label
    c : mpl.colors.Color
        color for the line
    """
    assert len(data.shape) == 1
    figsize = figsize

    if fill_up is not None:
        assert fill_up > 0 and fill_up < 1
    if fill_down is not None:
        assert fill_down > 0 and fill_down < 1
    fill_color = c if fill_color is None else fill_color

    sampling = np.arange(beg, beg + len(data) * dt, dt)[:len(data)]

    if orient == 'h':
        data, sampling = sampling, data
        value_label, axis_label = axis_label, value_label
        figsize = (figsize[1], figsize[0])

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(data, sampling, c=c)
    _fill_traces(ax, data, sampling, fill_down, fill_up, orient, fill_color)
    plt.ylabel(axis_label)
    plt.xlabel(value_label)
    plt.title(title)
    if orient == 'v':
        plt.gca().invert_yaxis()
    plt.tight_layout()

    if save is not None:
        plt.savefig(save, bbox_inches='tight', pad_inches=0, dpi=600)

    plt.show()


def plot_multi_traces(data,
                      dt=0.002,
                      beg=0,
                      c='black',
                      fill_up=None,
                      fill_down=None,
                      fill_color='black',
                      figsize=None,
                      xlabel='Trace number',
                      ylabel='Time / s',
                      save: str = None):
    """
    data.shape = (h, n_traces)
    """
    h, n = data.shape
    r = data.max() - data.min()
    r = r if r != 0 else 1
    y = np.arange(beg, beg + h * dt, dt)[:h]

    if fill_up is not None:
        assert fill_up > 0 and fill_up < 1
    if fill_down is not None:
        assert fill_down > 0 and fill_down < 1

    # figsize = figsize if figsize is not None else (4, 6)
    fig, ax = plt.subplots(figsize=figsize)

    prev_max = 0
    tick_pos = []
    for i in range(n):
        l = (data[:, i] - data.min()) / r + prev_max
        prev_max = l.max() if data[:, i].sum() != 0 else prev_max + 1
        tick_pos.append(l.mean())
        ax.plot(l, y, c=c)
        _fill_traces(ax, l, y, fill_down, fill_up, color=fill_color)

    tick_label = np.arange(0, n)
    step = 1 if n // 10 == 0 else n // 10
    ax.set_xticks(tick_pos[::step])
    ax.set_xticklabels(tick_label[::step])
    ax.invert_yaxis()
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    # ax.xaxis.set_ticks_position('top')
    ax.xaxis.set_label_position('top')

    # plt.xticks(fontproperties='Times New Roman', size=tick_size)
    # plt.yticks(fontproperties='Times New Roman', size=tick_size)
    # fontdict = {
    #         'family': 'Times New Roman',
    #         'weight': 'bold',
    #         'size': label_size
    #     }
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()

    if save is not None:
        plt.savefig(save, bbox_inches='tight', pad_inches=0, dpi=600)

    plt.show()


def _fill_traces(ax, x, y, fill_down, fill_up, orient='v', color='black'):
    h = len(y)
    if fill_down is not None:
        if orient == 'v':
            fmin = x.mean() - (x.max() - x.min()) / 2 * fill_down
            ax.fill_betweenx(y,
                             x, [fmin] * h,
                             where=(x < fmin),
                             interpolate=True,
                             color=color)
        else:
            fmin = y.mean() - (y.max() - y.min()) / 2 * fill_down
            ax.fill_between(x,
                            y, [fmin] * h,
                            where=(y < fmin),
                            interpolate=True,
                            color=color)
    if fill_up is not None:
        if orient == 'v':
            fmax = x.mean() + (x.max() - x.min()) / 2 * fill_up
            ax.fill_betweenx(y,
                             x, [fmax] * h,
                             where=(x > fmax),
                             interpolate=True,
                             color=color)
        else:
            fmax = y.mean() + (y.max() - y.min()) / 2 * fill_up
            ax.fill_between(x,
                            y, [fmax] * h,
                            where=(y > fmax),
                            interpolate=True,
                            color=color)


############## for image plot #####################


def _set_figsize(shape):
    n1, n2 = shape
    if n1 / n2 > 2:
        figsize = (3, 6)
    elif n2 / n1 > 2:
        figsize = (8, 4)
    else:
        figsize = [x * 1 for x in [int(6 * n2 / n1) + 1, 6]]

    return figsize


def _add_right_cax(ax, pad=0.02, width=0.04):
    axpos = ax.get_position()
    caxpos = mtf.Bbox.from_extents(axpos.x1 + pad, axpos.y0,
                                   axpos.x1 + pad + width, axpos.y1)
    cax = ax.figure.add_axes(caxpos)

    return cax


def plot2d(img,
           overylay=None,
           lines=None,
           cmap='gray',
           ov_cmap='jet',
           alpha=0.5,
           clim=None,
           ov_clim=None,
           figsize=None,
           title=None,
           xlabel=None,
           ylabel=None,
           cbar=None,
           interpolation='bicubic',
           ov_interp='bicubic',
           save=None):
    """
    plot2d
    """

    line_first = cigvis.is_line_first()
    if line_first:
        img = img.T

    if overylay is not None:
        if isinstance(overylay, np.ndarray):
            overylay = [overylay]
        if line_first:
            overylay = [v.T for v in overylay]

        if ov_clim is None:
            ov_clim = [[np.nanmin(v), np.nanmax(v)] for v in overylay]
        assert len(ov_clim) == len(overylay)

        if isinstance(ov_interp, str):
            ov_interp = [ov_interp] * len(overylay)

        if not isinstance(ov_cmap, List):
            ov_cmap = ['jet'] * len(overylay)
        assert len(ov_cmap) == len(overylay)

        # 显示要求为每个 cmap 设置 alpha
        if not isinstance(alpha, List):
            alpha = [alpha]
        assert len(alpha) == len(overylay)

    if figsize is None:
        figsize = _set_figsize(img.shape)
    if clim is None:
        clim = [img.min(), img.max()]
    cmap = colormap.get_cmap_from_str(cmap)

    fig, ax = plt.subplots(figsize=figsize)

    im = ax.imshow(img,
                   cmap=cmap,
                   vmin=clim[0],
                   vmax=clim[1],
                   aspect='auto',
                   interpolation=interpolation)

    if overylay is not None:
        for i in range(len(overylay)):
            print(alpha[i])
            ax.imshow(overylay[i],
                      cmap=ov_cmap[i],
                      vmin=ov_clim[i][0],
                      vmax=ov_clim[i][1],
                      alpha=alpha[i],
                      aspect='auto',
                      interpolation=ov_interp[i])

    if cbar is not None:
        cb = fig.colorbar(im, cax=_add_right_cax(ax))
        cb.set_label(cbar)
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if save is not None:
        plt.savefig(save, bbox_inches='tight', pad_inches=0, dpi=200)

    plt.show()


if __name__ == '__main__':
    pass