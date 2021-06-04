import matplotlib.table as mtable

import numpy as np

def linked_plot(fig, x,y,c):
    axd = fig.subplot_mosaic([["histx", "."],["scat", "histy"]], 
                                     gridspec_kw={'width_ratios': [7,2], 'height_ratios':[2,7]})

    im = axd['scat'].scatter(x, y, c=c, cmap='RdBu', picker=True)
    fig.colorbar(im, ax=axd['scat'], orientation='horizontal')

    _, _,  patchesx = axd['histx'].hist(x)
    _, _, patchesy = axd['histy'].hist(y, orientation='horizontal')

    axd['histx'].sharex(axd['scat'])
    axd['histy'].sharey(axd['scat'])


    def on_xlims_change(axes):
        start, end = axes.get_xlim()
        dx = x[(start<=x) & (x<=end)]
        _, _, patchesx = axd['histx'].hist(dx)
        axd['histx'].set_xlim([start,end])
        return [patchesx]

    def on_ylims_change(axes):
        start, end = axes.get_ylim()
        dy = y[(start<=y) & (y<=end)]
        _, _, patchesy = axd['histy'].hist(dy, orientation='horizontal')
        axd['histy'].set_ylim([start,end])
        return [patchesy]

    axd['scat'].callbacks.connect('xlim_changed', on_xlims_change)
    axd['scat'].callbacks.connect('ylim_changed', on_ylims_change)
    return axd

def plot_table(ax, data, columns=None, rows=None, scale=(1,1)):
    tab = mtable.table(ax, cellText=data, cellLoc='center',
                   colLabels=columns, rowLabels=rows, loc='center')
    tab.auto_set_font_size(False)
    tab.set_fontsize('medium')
    tab.scale(*scale)
    if columns is not None:
        tab.auto_set_column_width(np.arange(len(columns)))
   
    
    ax.set(xticks=[], yticks=[], aspect='equal')
    ax.axis('off')
    ax.add_table(tab)
    return tab

def source_cell(cell, color='k', xr=.5, yr=.5):
    #cell.get_text().set_color(color)
    x = cell.get_x() + cell.get_width()*xr
    y = cell.get_y() + cell.get_height()*yr
    return x, y