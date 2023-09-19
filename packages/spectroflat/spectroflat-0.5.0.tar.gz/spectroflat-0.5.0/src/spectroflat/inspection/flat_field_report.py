import matplotlib.pyplot as plt
import numpy as np

from .pdf import A4_PORTRAIT, A4_LANDSCAPE, PdfPages

MEAN = 'MEAN'
STD = 'STD'
MAX = '|MAX|'


def plt_smoothing_delta(before: list, img: np.array, pdf: PdfPages):
    states = len(before)
    if states == 1:
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=A4_PORTRAIT)
        _add_smoothing_result(ax, before[0], img[0])
    elif states < 9:
        fig, axs = plt.subplots(ncols=2, nrows=states // 2, sharex='all', figsize=A4_PORTRAIT)
        j = 0
        for s in range(states):
            i = 0 if s % 2 == 0 else 1
            _add_smoothing_result(axs[i][j], before[s], img[s], state=s)
            j += i
    else:
        fig, axs = plt.subplots(ncols=3, nrows=states // 3, sharex='all', figsize=A4_PORTRAIT)
        j = 0
        for s in range(states):
            i = 0 if s % 3 == 0 else 1
            _add_smoothing_result(axs[i][j], before[s], img[s], state=s)
            if i == 2:
                j += 1
    fig.suptitle(f'Detected residuals and col-wise mean before and after smoothing')
    fig.tight_layout()
    pdf.savefig()
    plt.close()


def _add_smoothing_result(ax, before: np.array, img: np.array, state: int = None) -> None:
    quarter = img.shape[0] // 4
    after = np.mean(img[quarter:-quarter, :], axis=0)
    state = 'Average' if state is None else f'#{state}'
    title = f'[{state}] From: {np.max(np.abs(before - 1)):.2e}. To: {np.max(np.abs(after - 1)):.2e}'
    ax.set_title(title)
    ax.plot(before, label='before')
    ax.plot(after, label='after')
    ax.set_xlabel(r'$\lambda$ [px]')
    ax.set_ylabel('Column mean')
    ax.set_xlim([0, len(before)])
    ax.legend()


def plt_state_imgs(img: np.array, pdf: PdfPages, title='', clim=None):
    states = img.shape[0]
    if states == 1:
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=A4_PORTRAIT)
        im = _add_img_plot(ax, img[0], clim=clim)
        fig.colorbar(im, ax=ax, orientation='horizontal')
    elif states < 9:
        fig, axs = plt.subplots(ncols=2, nrows=states // 2, sharex='col', sharey='row', figsize=A4_PORTRAIT)
        j = 0
        for s in range(states):
            i = 0 if s % 2 == 0 else 1
            im = _add_img_plot(axs[i][j], img[s], state=s, clim=clim)
            fig.colorbar(im, ax=axs[i][j], orientation='horizontal')
            j += i
    else:
        fig, axs = plt.subplots(ncols=3, nrows=states // 3, sharex='col', sharey='row', figsize=A4_PORTRAIT)
        j = 0
        for s in range(states):
            i = s % 3
            im = _add_img_plot(axs[j][i], img[s], state=s)
            fig.colorbar(im, ax=axs[j][i], orientation='horizontal')
            if i == 2:
                j += 1
    fig.suptitle(title)
    fig.tight_layout()
    pdf.savefig()
    plt.close()


def _add_img_plot(ax, img: np.array, state: int = None, clim=None):
    state = 'Average' if state is None else f'State #{state}'
    # ax.set_title(f'[{state}] MEAN:{img.mean():.2e} MIN:{img.min():.2e}\nMAX:{img.max():.2e} STD:{img.std():.2e}')
    ax.set_title(f'[{state}]')
    ax.set_xlabel(r'$\lambda$ [px]')
    ax.set_ylabel('y [px]')
    if clim is None:
        return ax.imshow(img, cmap='gray')
    if clim == 'sigma':
        m = img.mean()
        s = img.std()
        return ax.imshow(img, cmap='gray', clim=[m - s, m + s])
    return ax.imshow(img, cmap='gray', clim=clim)


def plt_img(img: np.array, pdf: PdfPages, title: str = '', roi: tuple = None, clim=None):
    fig, ax = plt.subplots(nrows=1, figsize=A4_LANDSCAPE)
    fig.suptitle(title)
    c = ax.imshow(img, cmap='gray', clim=clim)
    if roi is not None:
        ax.axvline(x=roi[1].start, linestyle='--')
        ax.axvline(x=roi[1].stop, linestyle='--')
        ax.axhline(y=roi[0].start, linestyle='--')
        ax.axhline(y=roi[0].stop, linestyle='--')
    fig.colorbar(c, ax=ax, label="Counts")
    ax.set_xlabel(r'$\lambda$ [px]')
    ax.set_ylabel('y [px]')
    fig.tight_layout()
    pdf.savefig()
    plt.close()


def plt_adjustment_comparison(original: np.array, desmiled: np.array, pdf: PdfPages, window: int = 230, roi=None):
    """
    Plot a cutout of selected rows from the original and the smile-corrected image.
    The plot shows window//2 pixels around the strongest line in the original.

    :param original: The original image
    :param desmiled: The desmiled image
    :param pdf: The PdfPages object to save the figure to
    :param window: Windows size in px
    :param roi: region of interest, if any
    """
    if roi is not None:
        original = original[roi]
        desmiled = desmiled[roi]
    brow = original.shape[0] // 3
    mrow = original.shape[0] // 2
    wcenter = original[mrow].argmin()
    wsize = window // 2
    xlim = [wcenter - wsize, wcenter + wsize]
    fig, ax = plt.subplots(nrows=2, figsize=A4_PORTRAIT)
    fig.suptitle(f'Correction result ({window} px around strongest line)')
    ax[0].set_title(f'Original')
    ax[0].plot(original[brow], label='top+margin')
    ax[0].plot(original[mrow], label='middle')
    ax[0].plot(original[-brow], label='bottom-margin')
    ax[0].set_xlim(xlim)
    ax[1].set_title(f'Corrected (selected rows)')
    ax[1].plot(desmiled[brow])
    ax[1].plot(desmiled[mrow])
    ax[1].plot(desmiled[-brow])
    ax[1].set_xlim(xlim)
    fig.legend()
    fig.tight_layout()
    pdf.savefig()
    plt.close()


def plt_std_of_consecutive_hard_flats(data: list, pdf: PdfPages) -> None:
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=A4_LANDSCAPE)
    ax.plot(data)
    ax.grid(True)
    fig.suptitle("Standard deviation of two consecutive hard flats")
    fig.tight_layout()
    pdf.savefig()
    plt.close()


def plt_selected_lines(data: np.array, lines: list, pdf: PdfPages, roi: tuple = None) -> None:
    fig, ax = plt.subplots(nrows=1, figsize=A4_LANDSCAPE)
    ax.set_title(f'Selected lines for fitting')
    ax.plot(data)
    for line in lines:
        li = line if roi is None else line + roi[1].start
        ax.axvline(x=li, linestyle='--')
    ax.set_xlim([0, len(data)])
    ax.set_xlabel(r'$\lambda$ [px]')
    ax.set_ylabel('Counts')
    fig.tight_layout()
    pdf.savefig()
    plt.close()


def ax_idx(num: int, cols: int = 2) -> tuple:
    return num // cols, num % cols
