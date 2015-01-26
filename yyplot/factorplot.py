import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def factorplot(x, y, hue, data, kind="box", 
               palette="PRGn", aspect=1.25, legend=False, 
               style='ticks', xlabel=None, ylabel=None, 
               legend_title=None, other_kws=None):

    if other_kws is None:
        other_kws = {}
    if xlabel is None:
        xlabel = ''
    if ylabel is None:
        ylabel = ''
    if legend_title is None:
        legend_title = ''

    sns.set(style=style)
    g = sns.factorplot(x, y, hue, data, kind=kind, palette=palette, 
                       aspect=aspect, legend=legend, **other_kws)

    if kind == 'box':
        g.despine(offset=10, trim=True)

    g.set_axis_labels(xlabel, ylabel)
    legend = plt.legend(title=legend_title, loc='center left', bbox_to_anchor=(1, 0.5))
    legend.get_title().set_fontsize('12')
    
    return g


