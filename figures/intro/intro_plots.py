import numpy as np

import matplotlib as mpl

import matplotlib.colors as mcolors
import matplotlib.dates as mdates
import matplotlib.table as mtable
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable


cdict = {'GANG MILLS NEW YORK': '#e6194B',
         'SARA NEW YORK': '#42d4f4',
         'SCHROON LAKE NEW YORK': '#9A6324',
         'SHERBURNE NEW YORK': '#4363d8',
         'STONYKILL NEW YORK': '#469990',
         'BINGHAMTON': '#3cb44b',
         'ISLIP LI MACARTHUR AP': '#ffe119',
         'NEW YORK LAGUARDIA AP': '#f58231',
         'BUFFALO': '#f032e6',
         'ALBANY AP': '#fabed4',
         'GLENS FALLS AP': '#dcbeff',
         'ROCHESTER GTR INTL AP': '#800000',
         'SYRACUSE HANCOCK INTL AP': '#aaffc3',
         'NEW YORK JFK INTL AP': '#000075'}

def plot_table(ax, dfs, ccolors, edgecolor='k', textcolor='k'):
    tab = mtable.table(ax, cellText=dfs.astype('str').values, cellLoc='center',
                   colLabels=dfs.columns, loc='center')
    #bbox=(0, 0, 1, 1))
    tab.auto_set_font_size(False)
    tab.set_fontsize('medium')
    tab.scale(1.25, 1.5)
    tab.auto_set_column_width(np.arange(len(dfs.columns)))
    for i, color in enumerate(ccolors):
        for j in range(len(dfs)+1):
            if textcolor is None:
                tab[(j,i)].get_text().set_color(color)
            else:
                tab[(j,i)].get_text().set_color(textcolor)
            tab[(j,i)].set_edgecolor(edgecolor)    
    
    ax.set(xticks=[], yticks=[], aspect='equal')
    ax.axis('off')
    ax.add_table(tab)
    return tab

def plot_map(ax, gdf, nystate, cmap, norm, fade='k'):
    for name in cdict:
        df = gdf.loc[[name], ['TAVG','geometry']]
        df.plot(ax=ax, facecolor=cmap(norm(df['TAVG'])), edgecolor=cdict[name], linewidth=2.5, alpha=.75, markersize=100)
    
    mapplot= nystate[nystate['postal'].str.match('NY')].plot(ax=ax, 
                                                             facecolor='white', 
                                                             edgecolor=fade, zorder=-1)
    
    ax1_divider = make_axes_locatable(ax)
    cax = ax1_divider.append_axes("right", size="5%", pad="2%")
    cb = mpl.colorbar.ColorbarBase(cax, cmap=cmap,norm=norm, orientation='vertical', drawedges=False)
    
    for axes in [ax, cax]:
        axes.tick_params(color=fade, labelcolor=fade)
        axes.spines[:].set_color(fade)
    ax.set_aspect('equal')
    ax.axis('off')
    return mapplot
    
def plot_time(ax, df, fade='k'):
    for name, gdf in df.groupby(['NAME']):
        ax.plot('DATES', 'TAVG', data=gdf, label=name,  alpha=.75, color=cdict[name])
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(mdates.AutoDateLocator()))
    ax.tick_params(color=fade, labelcolor=fade)
    ax.spines[:].set_color(fade)
   
    