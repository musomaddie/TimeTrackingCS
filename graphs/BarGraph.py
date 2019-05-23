import numpy as np
import matplotlib.pyplot as plt


def make_bar_graph(labels,
                   data,
                   xLabel,
                   yLabel,
                   title,
                   filename):
    index = np.arange(len(labels))
    plt.bar(index, data)
    plt.xlabel(xLabel, fontsize=5)
    plt.ylabel(yLabel, fontsize=5)
    plt.xticks(index, labels, fontsize=5, rotation=5)
    plt.title(title)
    plt.savefig("graphImages/barGraphs/{}.png".format(filename))
