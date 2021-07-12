import itertools

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.transforms as mtransforms
from matplotlib import rcParams

import themepy
theme = themepy.Theme('paper')

import intro_plots as ip

rcParams['figure.dpi'] = 200
rcParams['font.family'] = 'Segoe Print'

fc = '#FEF7F9'
ec = '#f2f8fa'
ecolor = '#248EA6'
fcolor = '#E30B5C'
kcolor = '#021859'
scolor='C1'
pcolor = 'darkgray'
tcolor = 'dimgray'
acolor = 'C4'
posc='#4A73A8'

station_color = {v: ip.cdict.get(k, None) for k, v in ip.airport_codes.items()}


E = ['temp', 'prcp', 'station']
V = ['x', 'y', 'color']
grid = [['E', 'V', 'V*', 'H'], 
          ['.', 'K', 'S', '.']]


def table(axd, data):
    w = h = .25
    y = 0
    for i, record in enumerate(data):
        x=.25
        for (c, val) in record:
            wo = w if c in ['temp', 'prcp'] else w*5.25
            ha = 'center' if c in ['temp', 'prcp'] else 'left'
            xt = .5 if c in ['temp', 'prcp'] else .015
            
            axsub = axd['E'].inset_axes([x,y,wo,h], 
                                transform=axd['E'].transData)
            axsub.text(xt, .5, val, 
                        transform=axsub.transAxes, 
                       ha=ha, va='center')
            axsub.set(xticks=[], yticks=[])
            if i == len(data)-1:
                axsub.set_title(c, fontsize=10, rotation=0)
            x+=w
        y+=1.5*w

def make_figure(artist=False, section=False, visual=False, continuity=False, data=False, values=None, plot_type='scatter', label=None, fiber=False, fig=None):
    
    if continuity or fiber:
        figsize = (11,5)
        mosaic = grid
    else:
        figsize = (11, 2.5)
        mosaic = [grid[0]]
        
    if fig is None:
        fig = plt.figure(figsize=figsize, facecolor='white')
        
    axd = fig.subplot_mosaic(mosaic)
    
    label = [] if label is None else label
    
 
    for n in axd.keys():
        if n not in ['H']:
            axd[n].set_aspect('equal')
            axd[n].set(xlim=(0,1), ylim=(0,1))
            axd[n].axis('off')
    
        w = h = .25
        axsub = {}
        for (n, C) in [('E',E), ('V', V)]:
            x = .5
            xt = [x+w/2]
            if (not visual and n=='V') or (not data and n=='E'):
                xt.append(x+w/2)
                continue
            
            for i, d in enumerate(values):
                row = dict(d)
                y = .6
                for c in C:  
                    axsub[c] = axd[n].inset_axes([x,y,w,h], transform=axd[n].transData)
                    axsub[c].set(xticks=[], yticks=[])
                    y-=w
                    if n == 'E':
                        axsub[c].text(.5, .5, row[c], transform=axsub[c].transAxes, ha='center', va='center')
                    if i>0:
                        continue
                    axsub[c].set_ylabel(c, fontsize=14, rotation=0, labelpad=15, ha='right', va='center')
                x+=2*w
                xt.append(x+w/2)

                if visual and n == 'V':
                    axsub['x'].axvline(row['prcp'], color=posc, lw=3)
                    axsub['y'].axhline(row['temp'], color=posc, lw=3)
                    axsub['color'].set_facecolor(ip.cdict[row['station']])


                if visual and 'V*' in label:
                    #fewer but bigger
                    wm=hm=.15
                    axsubp = [(-.1, .6), (.1, .4), (.3, .7), (.5, .5)]
                    for (xm, ym) in axsubp:
                            axv = {}
                            for c in V:
                                axv[c] = axd['V*'].inset_axes([xm,ym,wm,hm], transform=axd['V*'].transData)
                                axv[c].set(xticks=[], yticks=[])
                                ym-=hm
                    
                            axv['x'].axvline(row['prcp'], color=posc, lw=3)
                            axv['y'].axhline(row['temp'], color=posc, lw=3)
                            axv['color'].set_facecolor(ip.cdict[row['station']])
                    
    for (xlab, x), (ylab, y), (_, station) in values:
        c = ip.cdict[station]
        if plot_type=='scatter':
            axd['H'].scatter(x, y, c=c,
                             ec='k', s=250, zorder=5, 
                             label=ip.airport_codes[station])
            axd['H'].legend(facecolor='white', ncol=1, 
                            loc='upper left', markerscale=.5)
        if visual:
            axd['H'].axvline(x, lw=5, color=posc, alpha=.25)
            axd['H'].axhline(y, lw=5, color=posc, alpha=.25)
    axd['H'].set(xlim=(-30, 30), ylim=(-2.5, 50), facecolor='white')
    axd['H'].set_xlabel(f'{xlab} (°C)', loc='right')
    axd['H'].set_ylabel(f'{ylab} (mm)', loc='top')
    

    if continuity or fiber:
        N = len(values)
        xk = np.linspace(.4, .8, N)
        xs = np.linspace(.2, .6, N)
        axd['K'].scatter(xk, [.5]*N, s=20, c=kcolor)
        axd['S'].scatter(xs, [.5]*N, s=1000, lw=2, facecolor=scolor, edgecolor=kcolor)
        if ['K'] in label:
            axd['K'].text(.625, .2, r'k$\in$K', fontsize=16, 
                          color=kcolor, ha='center', va='bottom')
        if ['S'] in label:
            axd['S'].text(.325, .2, r'$S_k$',
                          color=kcolor, fontsize=16, ha='center', va='bottom')
     
    font_kw = {'fontsize':14, 'fontweight':'bold', 'va':'center', 'ha':'center'}
    bbox = {'facecolor':'white', 'edgecolor':'white','pad':.02}
    tfont_kw = {'fontsize':14, 'fontweight':'bold', 'va':'center', 'ha':'center'}
    
    if section or fiber:
        for i, ((xlab, xd), (ylab, yd), (_, station)) in enumerate(values):
            for n,x in [('E', .225), ('V', .425), ('V*', .575), ('H',.8)]:
                if n in label:
                    fig.text(x, .875, n,color=ecolor, fontsize=16, ha='center', va='bottom')
                    
            for n in ['E', 'V']:
                if n in label:
                    tau = mpatches.ConnectionPatch(xyA=(xk[i], .5), coordsA=axd['K'].transAxes, 
                                                  xyB=(xt[i], .075), coordsB=axd[n].transAxes, 
                                                  arrowstyle='->', mutation_scale=15,
                                                   lw=2, linestyle='--', color=tcolor) 
                    fig.add_artist(tau)
        
            if 'E' in label:
                fig.text(0, .86, r'$\tau$', color=tcolor, **tfont_kw, transform=axd['K'].transAxes)
            if 'V' in label:
                fig.text(.69, .95, r'$\mu$', color=tcolor, **tfont_kw, transform=axd['K'].transAxes)

            if 'H' in label:
                rho = mpatches.ConnectionPatch(xyA=(xs[i], .625), coordsA=axd['S'].transAxes, 
                                                  xyB=(xd-2.5, yd-.04), coordsB=axd['H'].transData, 
                                                  arrowstyle='->', mutation_scale=15, 
                                                   lw=2, linestyle='--', color=tcolor) 
                fig.add_artist(rho)
                fig.text(.92, .92, r'$\rho$', color=tcolor, **tfont_kw, transform=axd['S'].transAxes)



        

        if artist:
            for src, dest in [('temp', 'x'), ('prcp', 'y'), ('station', 'color')]:
                nu = mpatches.ConnectionPatch(xyA=(1.1, .5), coordsA=axsub[src].transAxes, 
                                              xyB=(0, .5), coordsB=axsub[dest].transAxes, 
                                               mutation_scale=25, arrowstyle='-|>', lw=4, color=acolor)      
                fig.add_artist(nu)
            x = -2.15
            y = .8
            fig.text(x, y, r'$\nu_{x}$',  color=acolor, **font_kw, transform=axsub['x'].transAxes) 
            fig.text(x, y, r'$\nu_{y}$', color=acolor, **font_kw, transform=axsub['y'].transAxes)      
            fig.text(x, y, r'$\nu_{color}$',  color=acolor, **font_kw, transform=axsub['color'].transAxes)


            if 'V*' in label:
                q1 = mpatches.ConnectionPatch(xyA=(-.5, .5), coordsA=axd['H'].transAxes, 
                                                  xyB=(xd-5, yd+.01), coordsB=axd['H'].transData, 
                                                  arrowstyle=']-,widthA=2.25,lengthA=.5', 
                                               mutation_scale=25, lw=5, color=acolor)      
                fig.add_artist(q1)

                q2 = mpatches.ConnectionPatch(xyA=(-.5, .5), coordsA=axd['H'].transAxes, 
                                            xyB=(xd, yd), coordsB=axd['H'].transData, 
                                                   mutation_scale=25, arrowstyle='-|>', lw=5, color=acolor)      
                fig.add_artist(q2)

                fig.text(-.39, .6, r'$Q$',color=acolor, **font_kw, transform=axd['H'].transAxes)

            
                xi1 = mpatches.ConnectionPatch(xyA=(-.15, .5), coordsA=axd['V*'].transAxes, 
                                                  xyB=(.75, .5), coordsB=axd['V'].transAxes, 
                                                   mutation_scale=25, arrowstyle='-|>', lw=5, color=acolor)      
                fig.add_artist(xi1)

                fig.text(-.25, .6, r'$\xi^*$', color=acolor, **font_kw, transform=axd['V*'].transAxes)
            elif 'V' in label:
                qh1 = mpatches.ConnectionPatch(xyA=(.85, .5), coordsA=axd['V'].transAxes, 
                                                  xyB=(xd-5, yd+.01), coordsB=axd['H'].transData, 
                                                  arrowstyle=']-,widthA=2.25,lengthA=.5', 
                                               mutation_scale=25, lw=5, color=acolor)      
                fig.add_artist(qh1)

                qh2 = mpatches.ConnectionPatch(xyA=(.85, .5), coordsA=axd['V'].transAxes,
                                               xyB=(xd, yd), coordsB=axd['H'].transData, 
                                        mutation_scale=25, arrowstyle='-|>', lw=5, color=acolor)      
                fig.add_artist(qh2)

                fig.text(1.5, .6, r'$\hat{Q}$', color=acolor, **font_kw, transform=axd['V'].transAxes)
                
        if continuity:
            xioff=.15
            xi2 = mpatches.ConnectionPatch(xyA=(xs[0]-xioff, .5), coordsA=axd['S'].transAxes, 
                                              xyB=(xk[-1], .5), coordsB=axd['K'].transAxes, 
                                               mutation_scale=25, arrowstyle='-|>', lw=5, color=acolor)      
            fig.add_artist(xi2) 
            fig.text(-.2, .6, r'$\xi$', color=acolor, **font_kw, transform=axd['S'].transAxes)
      
        if 'V*' in label:
            for dest in axsubp:
                xd, yd = dest[0]+wm/2, dest[1]-2*wm 
                mus = mpatches.ConnectionPatch(xyA=(xs[0], .625), coordsA=axd['S'].transAxes, 
                                              xyB=(xd,yd), coordsB=axd['V*'].transData, 
                                              arrowstyle='->', mutation_scale=15, 
                                               lw=1.5, linestyle='--', color=tcolor) 
                fig.add_artist(mus)

            fig.text(.38, 1.175, r'$\mu*$', color=tcolor, **tfont_kw, transform=axd['S'].transAxes)
    
    return fig, axd