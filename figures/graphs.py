import matplotlib.patches as mpatches
import matplotlib.table as mtable

import numpy as np
import pandas as pd

import intro_plots as ip

def linked_plot(fig, nydf):
    axd = fig.subplot_mosaic([["histx", "."],["scat", "histy"]], 
                              gridspec_kw={'width_ratios': [7,2], 'height_ratios':[2,7], 'wspace':-.1, 'hspace':-.1})

    axd['histx'].sharex(axd['scat'])
    axd['histy'].sharey(axd['scat'])
    
    im = axd['scat'].scatter('TAVGF', 'PRCPI', c=nydf['color'], alpha=.5, edgecolor='silver', data=nydf, picker=True)
    labels, handles = zip(*[(ip.airport_codes[n], mpatches.Circle(.2, facecolor=c)) for n, c in ip.cdict.items()])
    axd['scat'].set(xlabel='temperature (°F)', ylabel='precipitation (in.)')
    
    axd['histy'].legend(list(handles), list(labels), ncol=1,
                       loc='right', 
                       bbox_transform=axd['histy'].transAxes,    bbox_to_anchor=(2, .5))

    for l, gdf in nydf.groupby('NAME'):
        try:
            _, _,  patchesx = axd['histx'].hist('TAVGF', data=gdf, 
                                            color=ip.cdict[l], histtype='step')
            _, _, patchesy = axd['histy'].hist('PRCPI', data=gdf, 
                                    color=ip.cdict[l], histtype='step',
                                    orientation='horizontal')
        except ValueError as e:
            print(f'{l}')


    axd['histx'].tick_params(axis="x", length=0,labelbottom=False)
    axd['histy'].tick_params(axis="y", length=0, labelleft=False)
    axd['histx'].set_ylim(0,50)
    axd['histy'].set_xlim(0,100)
    
    def on_xlims_change(axes):
        startx, endx = axes.get_xlim()
        
        dx = nydf[(startx<=nydf['TAVGF']) & (nydf['TAVGF']<=endx)]
        
        patchesx = []
        for l, gdf in dx.groupby('NAME'):
            _, _, px = axd['histx'].hist('TAVGF', data=gdf, color=ip.cdict[l], histtype='step')
            patchesx.append(px)
            
        axd['histx'].set(xlim=[startx,endx], ylim=[0,50])
        return patchesx

    def on_ylims_change(axes):
        starty, endy = axes.get_ylim()
        dy = nydf[(starty<=nydf['PRCPI']) & (nydf['PRCPI']<=endy)]
        patchesy = []
        for l, gdf in dy.groupby('NAME'):
            _, _, py = axd['histy'].hist('PRCPI', data=gdf, color=ip.cdict[l], histtype='step')
            patchesy.append(py)
            
        axd['histy'].set(ylim=[starty,endy], xlim=(0,100))
        return [patchesy]
    
    def on_pick(event): #write legend selector for the hell of it? https://matplotlib.org/stable/gallery/event_handling/legend_picking.html
        pass

    axd['scat'].callbacks.connect('xlim_changed', on_xlims_change)
    axd['scat'].callbacks.connect('ylim_changed', on_ylims_change)
    return axd



def plot_table(ax, data, columns=None, rows=None, scale=(1,1), loc="center", hide=None, spacing="          "):
    hide = hide if hide is not None else []
    tab = mtable.table(ax, cellText=data, cellLoc='center',
                       colLabels=columns, rowLabels=rows, loc=loc)
    tab.auto_set_font_size(False)
    tab.set_fontsize('medium')
    tab.scale(*scale)
    if columns is not None:
        tab.auto_set_column_width(np.arange(len(columns)))
   
    for j, column in enumerate(columns):
        if column == 'gap':
            tab[0,j].get_text().set_text(spacing)
        for i in range(len(data)+1):
            if column == 'gap':
                tab[i,j].visible_edges='vertical'
            if j in hide:
                tab[i,j].set_visible(False)
    
    ax.set(xticks=[], yticks=[], aspect='equal')
    ax.axis('off')
    
    ax.add_table(tab)
    return tab

def source_cell(cell, color='k', xr=.5, yr=.5):
    #cell.get_text().set_color(color)
    x = cell.get_x() + cell.get_width()*xr
    y = cell.get_y() + cell.get_height()*yr
    return x, y