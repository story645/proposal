import matplotlib.patches as mpatches
import matplotlib.table as mtable

import numpy as np
import pandas as pd

import intro_plots as ip

def linked_plot(fig, nydf):
    axd = fig.subplot_mosaic([["histx", "."],["scat", "histy"]], 
                                     gridspec_kw={'width_ratios': [7,2], 'height_ratios':[2,7]})

    im = axd['scat'].scatter('TAVGF', 'PRCPI', c=nydf['color'], alpha=.5, edgecolor='silver', data=nydf, picker=True)
    labels, handles = zip(*[(n, mpatches.Circle(.2, facecolor=c)) for n, c in ip.cdict.items()])
    axd['scat'].set(xlabel='temperature (°F)', ylabel='precipitation (in.)')
    axd['scat'].legend(list(handles), list(labels), ncol=1,
                       bbox_to_anchor=(1.5, 1))

    for l, gdf in nydf.groupby('NAME'):
        try:
            _, _,  patchesx = axd['histx'].hist('TAVGF', data=gdf, 
                                            color=ip.cdict[l], histtype='step')
            _, _, patchesy = axd['histy'].hist('PRCPI', data=gdf, 
                                    color=ip.cdict[l], histtype='step',
                                    orientation='horizontal')
        except ValueError as e:
            print(f'{l}')

    axd['histx'].sharex(axd['scat'])
    axd['histy'].sharey(axd['scat'])

    def on_xlims_change(axes):
        start, end = axes.get_xlim()
        
        dx = nydf[(startx<=nydf['TAVG']) & (nydf['TAVG']<=endx)]
        
        patchesx = []
        for l, gdf in dx.groupby('NAME'):
            _, _, px = axd['histx'].hist('TAVG', data=gdf, color=ip.cdict[l])
            patchesx.append[px]
            
        axd['histx'].set_xlim([startx,endx])
        return patchesx

    def on_ylims_change(axes):
        starty, endy = axes.get_ylim()
        dy = nydf[(starty<=nydf['PRCPI']) & (nydf['PRCPI']<=endy)]
        patchesy = []
        for l, gdf in dy.groupby('NAME'):
            _, _, py = axd['histy'].hist('PRCPI', data=gdf, color=ip.cdict[l])
            patchesy.append[py]
            
        axd['histy'].set_ylim([starty,endy])
        return [patchesy]
    
    def on_pick(event): #write legend selector for the hell of it? https://matplotlib.org/stable/gallery/event_handling/legend_picking.html
        pass

    axd['scat'].callbacks.connect('xlim_changed', on_xlims_change)
    axd['scat'].callbacks.connect('ylim_changed', on_ylims_change)
    return axd



def plot_table(ax, data, columns=None, rows=None, scale=(1,1), loc='center'):
    tab = mtable.table(ax, cellText=data, cellLoc='center',
                   colLabels=columns, rowLabels=rows, loc=loc)
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