import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#a function to draw personal style joint plot
def jointplot(x, y, data=None, kind='hex', stat_func=None, 
              maincolor='grey', size=6, ratio=4, space=0.2, dropna=True, 
              xlim=None, ylim=None, xlabel=None, ylabel=None, 
              style='ticks', hist_bins=30, hist_type='stepfilled',
              hist_facecolor='grey', hist_edgecolor='grey', 
              hist_alpha=0.3, hist_kde=True, kde_color='grey', 
              kde_linewidth=2, kde_linestyle='-', kde_alpha=0.7):

    """
        Attributes:
            x,y: data
            data: dataframe when x, y are variable names
            kind: main fig kind {“scatter”|“reg”|“resid”|“kde”|“hex”}
            stat_func: stat functions
            maincolor: color for main plot
            size: figure size
            ratio: ratio of joint fig to main fig
            space: space between joint and main fig
            dropna: If True, remove observations that are missing from x and y
            {x, y}lim: Axis limits to set before plotting, e.g. {(1,100),(1,100)}
            {x, y}label: label for x, y axis
            style: joint fig axes style, None, or {"darkgrid"|"whitegrid"|"dark"|"white"|"ticks"}
            hist_bins: bins
            hist_type: {"bar"|"barstacked"|"step"|"stepfilled"}
            hist_facecolor: face color of hist bars
            hist_edgecolor: edge color of hist bars
            hist_alpha: alpha of hist
            kde_color: color of kde plot
            kde_linewidth: line width
            kde_linestyle: {'-'|'--'|'-.'|':'|'None'|' '|''}
            kde_alpha: alpha of kde
        Ref:
        http://stanford.edu/%7Emwaskom/software/seaborn/generated/seaborn.jointplot.html?highlight=jointplot#seaborn.jointplot
        """

    if xlabel is None:
        xlabel = ''
    if ylabel is None:
        ylabel = ''

    sns.set(style=style)
    g = sns.jointplot(x, y, data=data, kind=kind, stat_func=stat_func, 
                      color=maincolor,  size=size, ratio=ratio, 
                      space=space, dropna=dropna, xlim=xlim, ylim=ylim,
                      marginal_kws = {"kde":hist_kde, 
                                      "bins": hist_bins, 
                                      "hist_kws" : {"histtype": hist_type, "facecolor":hist_facecolor,"edgecolor":hist_edgecolor, "alpha" : hist_alpha},
                                      "kde_kws" : {"alpha":kde_alpha, "linewidth":kde_linewidth, "linestyle":kde_linestyle, "color":kde_color}
                                      }
                      )

    g.set_axis_labels(xlabel,ylabel)
    return g









