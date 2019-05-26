import numpy as np
import matplotlib.pyplot as plt


def make_bar_graph(labels,
                   data,
                   xLabel,
                   yLabel,
                   title,
                   filename,
                   color="#3d1215"):
    index = np.arange(len(labels))

    plt.style.use("seaborn")
    plt.bar(index, data, color=color)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.xticks(index, labels, fontsize=8)
    plt.title(title)
    plt.savefig("graphImages/barGraphs/{}.png".format(filename))
    plt.close()
