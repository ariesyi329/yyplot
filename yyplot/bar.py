import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utility import axis_helper
from utility import title_helper
from utility import background_helper

def bar( x, df, alpha=0.7, title=None, legend=False, 
        color='skyblue', edgecolor='w',xlabel=None, 
        xlabelsize=20, x_fontsize=16, y_fontsize=20, ypad=12):

    if title is None:
        title = ''
    if xlabel is None:
        xlabel = ''

    fig = plt.figure(figsize=(16,12))
    ax = fig.add_subplot(111)
    df[x].plot(kind='barh', ax=ax, alpha=alpha, legend=legend, 
               color=color, edgecolor=edgecolor, xlim=(0,max(df[x])))

    #set x axis label on top of plot, set label text
    ax.xaxis.set_label_position('top')
    ax.set_xlabel(xlabel, fontsize=20, alpha=alpha, ha='left', va='bottom')
    ax.xaxis.set_label_coords(0.005, 1.05)

    # Position x tick labels on top
    ax.xaxis.tick_top()
    #pandas trick: remove weird dotted line on axis
    ax.lines[0].set_visible(False)

    axis_helper(ax, left=False, bottom=False, xtick=False, ytick=False)
    title_helper(ax=ax, title=title, fontsize=26, ha='left', xloc=0, yloc=1.1, alpha=alpha)

    # Customize y tick labels
    yticks = [item.get_text() for item in ax.get_yticklabels()]
    ax.set_yticklabels(yticks, fontsize=y_fontsize, alpha=alpha)
    ax.yaxis.set_tick_params(pad=ypad)
    
    xticks = [int(min(df[x])), int(np.mean(df[x])), int(np.median(df[x])), int(max(df[x]))]
    xticks_labels = [int(min(df[x])), int(np.mean(df[x])), int(np.median(df[x])), int(max(df[x]))]
    ax.xaxis.set_ticks(xticks)
    ax.set_xticklabels(xticks_labels, fontsize=x_fontsize, alpha=alpha)
    
    ax.set_ylabel('')
    background_helper(ax, color='w')

    return ax
