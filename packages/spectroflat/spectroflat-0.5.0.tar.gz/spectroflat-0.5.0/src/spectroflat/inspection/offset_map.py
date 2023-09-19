import matplotlib.pyplot as plt
import numpy as np

from .pdf import A4_PORTRAIT, A4_LANDSCAPE
from ..smile import SmileMapGenerator, OffsetMap


def plt_deviation_from_straight(smg: SmileMapGenerator, pdf=None) -> None:
    fig, ax = plt.subplots(nrows=2, sharex='all', figsize=A4_PORTRAIT)
    fig.suptitle('Difference to straight line')

    for i in range(len(smg.fitters)):
        xes = [smg.fitters[i].cores[j].center for j in range(len(smg.fitters[i].cores))]
        data = [smg.fitters[i].fitted[j].c[0] for j in range(len(smg.fitters[i].cores))]
        ax[0].plot(xes, data, '-*', label=f'State {i}')
        ax[1].plot(xes, smg.px_deviations(i), '-*')
    title = 'x^2 coefficient of each fitted line\n'
    title += f'MEAN {smg.mean():.4e}; STD {smg.std():.4e}'
    ax[0].set_title(title)
    ax[0].set_ylabel('x² coefficient')
    ax[1].set_xlabel(r'Position of the line center on $\lambda$-axis [px]')
    ax[1].set_ylabel(r'max($\Delta$ px)')
    title = 'Max deviation from a straight of each fitted line in pixels\n'
    title += f'MEAN {smg.mean_px_deviation():.4e}; STD {smg.std_px_deviation():.4e}'
    ax[1].set_title(title)
    fig.legend()
    fig.tight_layout()
    if pdf is not None:
        pdf.savefig()
        plt.close()
    else:
        plt.show()


def plt_map(smap: OffsetMap, rows: tuple = (50, 550, -550, -50), state_aware: bool = True, pdf=None) -> None:
    """
    Generates a heatmap plot of the given smile offset map.
    Note: Will only plot the average for all states (e.g. the "squashed" version, without squashing the map)

    ### Params
    - smap: The `OffsetMap` to plot
    - rows: The row numbers to plot cuts through
    - title: The title of the plot
    """
    if smap.is_squashed():
        _omap_state_plot(smap.map, smap.error, rows, 'Squashed Offset Map', pdf)
    elif not state_aware:
        _omap_state_plot(smap.map[0], smap.error[0], rows, f'Offset Map for all states', pdf)
    else:
        for s in range(smap.map.shape[0]):
            _omap_state_plot(smap.map[s], smap.error[s], rows, f'Offset Map for state #{s}', pdf)


def _omap_state_plot(shifts: np.array, error: np.array, rows: tuple, title: str, pdf=None):
    colors = ['green', 'red', 'orange', 'purple', 'lime', 'pink', 'blue', 'yellow']
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex='col', dpi=100, figsize=A4_LANDSCAPE)
    fig.suptitle(title)
    xes = range(shifts.shape[1])
    axs[0, 0].set_title(r'Offset per column in $\lambda$ direction')
    axs[0, 0].set_xlabel(r'column($\lambda$ [px])')
    axs[0, 0].set_ylabel('offset [px]')

    c = axs[0, 1].imshow(shifts, cmap='gray')
    fig.colorbar(c, ax=axs[0, 1], label='Offset [px]')
    axs[0, 1].set_title('Offset per pixel')
    axs[0, 1].set_xlabel(r'$\lambda$ [px]')
    axs[0, 1].set_ylabel('y [px]')
    for i in range(len(rows)):
        r = shifts.shape[0] + rows[i] if rows[i] < 0 else rows[i]
        axs[0, 0].plot(xes, shifts[r], label=f"row  {r}", color=colors[i])
        axs[0, 1].axhline(y=r, color=colors[i], linestyle='--', linewidth=0.5)
    axs[0, 0].legend()

    axs[1, 0].set_title(r'Error per column in $\lambda$ direction')
    axs[1, 0].set_xlabel(r'column($\lambda$ [px])')
    axs[1, 0].set_ylabel(r'$\chi^2$ Error')

    c = axs[1, 1].imshow(error, cmap='gray', clim=[0, 0.005])
    fig.colorbar(c, ax=axs[1, 1], label=r'$\chi^2$ Error')
    axs[1, 1].set_title(r'$\chi^2$ error per pixel (clipped at 0.005)')
    axs[1, 1].set_xlabel(r'$\lambda$ [px]')
    axs[1, 1].set_ylabel('y [px]')
    for i in range(len(rows)):
        axs[1, 0].plot(xes, error[rows[i]], label=f"row  {rows[i]}", color=colors[i])
        r = error.shape[0] + rows[i] if rows[i] < 0 else rows[i]
        axs[1, 1].axhline(y=r, color=colors[i], linestyle='--', linewidth=0.5)

    fig.tight_layout()
    if pdf is not None:
        pdf.savefig()
        plt.close()
    else:
        plt.show()
