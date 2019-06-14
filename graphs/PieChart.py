import numpy as np
import matplotlib.pyplot as plt


def make_pie_chart(labels,
                   data,
                   filename):
    labels = labels
    sizes = data
    patches, texts = plt.pie(sizes,
                             startangle=90,
                             counterclock=False)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')  # ensures a circle
    plt.tight_layout()
    plt.savefig("graphImages/pieCharts/{}.png".format(filename))
