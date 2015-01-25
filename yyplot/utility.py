import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def title_helper(ax, title, fontsize=20, color='k', alpha=0.8, 
                 ha='center', va='bottom', xloc=0.5, yloc=1.05):
    
    ax.set_title(label=title, fontsize=fontsize, 
                 color=color, alpha=alpha, ha=ha, va=va)
    plt.subplots_adjust(top=0.9)
    ax.title.set_position((xloc,yloc))

def axis_helper(ax, left=True, bottom=True, right=False, top=False,
                grid=False, xtick=True, ytick=True, color='dimgrey'):

    ax.grid(grid)
    ax.spines["right"].set_visible(right)
    ax.spines["top"].set_visible(top)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)
    if left is True:
        ax.spines['left'].set_color(color)
        ax.tick_params(axis='y', colors=color)
        ax.get_yaxis().tick_left()
    if bottom is True:
        ax.spines['bottom'].set_color(color)
        ax.tick_params(axis='x', colors=color)
        ax.get_xaxis().tick_bottom()
    if right is True:
        ax.spines['right'].set_color(color)
    if top is True:
        ax.spines['top'].set_color(color)
    
    if ytick is False:
        ax.yaxis.set_ticks_position('none')
    if xtick is False:
        ax.xaxis.set_ticks_position('none')

def colorbar_helper(customcmap, vmin, vmax, interval, label, 
                    cb_alpha=0.05, cb_aspect=16, cb_shrink=0.4,
                    tick_labelsize=14, tick_alpha=0.7, label_fontsize=20,
                    labelpad=30, label_alpha=0.7):
    # Create a fake colorbar
    ctb = LinearSegmentedColormap.from_list('custombar', customcmap, N=2048)
    # Trick from http://stackoverflow.com/questions/8342549/
    # matplotlib-add-colorbar-to-a-sequence-of-line-plots
    sm = plt.cm.ScalarMappable(cmap=ctb, norm=plt.normalize(vmin=vmin, vmax=vmax))
    # Fake up the array of the scalar mappable
    sm._A = []
    # Set colorbar, aspect ratio
    cbar = plt.colorbar(sm, alpha=cb_alpha, aspect=cb_aspect, shrink=cb_shrink)
    cbar.solids.set_edgecolor("face")
    # Remove colorbar container frame
    cbar.outline.set_visible(False)
    # Fontsize for colorbar ticklabels
    cbar.ax.tick_params(labelsize=tick_labelsize)
    # Customize colorbar tick labels
    mytks = np.arange(vmin, vmax, interval)
    cbar.set_ticks(mytks)
    cbar.ax.set_yticklabels([str(a) for a in mytks], alpha = tick_alpha)
    # Colorbar label, customize fontsize and distance to colorbar
    cbar.set_label(label, alpha = label_alpha, rotation=270, 
                   fontsize=label_fontsize, labelpad=labelpad)
    # Remove color bar tick lines, while keeping the tick labels
    cbarytks = plt.getp(cbar.ax.axes, 'yticklines')
    plt.setp(cbarytks, visible=False)