import numpy as np
import matplotlib.pyplot as plt


def _find_percent(data, i):
    this_item = data[i]
    total_sum = sum(x for x in data)

    return this_item / total_sum * 100


def _make_display_label(label, data, i):
    return "{}: {:.1f}%".format(label[i],
                                (data[i] / sum(x for x in data)) * 100)


def make_pie_chart(labels,
                   data,
                   filename):
    labels = labels
    patches, texts = plt.pie(data,
                             wedgeprops=dict(width=0.5),
                             startangle=90,
                             counterclock=False)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")
    # plt.legend(patches, labels, loc="best")
    for i, p in enumerate(patches):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        plt.annotate(_make_display_label(labels, data, i),
                     xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                     horizontalalignment=horizontalalignment, **kw)
    plt.axis('equal')  # ensures a circle
    plt.autoscale()
    plt.savefig("graphImages/pieCharts/{}.png".format(filename),
                bbox_inches="tight")
    plt.close()
