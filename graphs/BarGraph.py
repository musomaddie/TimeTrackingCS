import pygal


def make_bar_graph(labels,
                   data,
                   x_title,
                   y_title,
                   title,
                   filename,
                   color=["#3d1215"],
                   for_animation=False,
                   short_y_title="time"):
    chart = pygal.Bar(title=title,
                      x_title=x_title,
                      y_title=y_title,
                      show_legend=False)
    chart.x_labels = labels
    chart.add(short_y_title, _create_data_dict(data, color))
    if for_animation:
        chart.render_to_png(
            "graphImages/animationProcessing/bar/{}.png".format(filename))
    else:
        chart.render_to_png("graphImages/barGraphs/{}.png".format(filename))


def _create_data_dict(values, color):
    # TODO: add sensible way of dealing with colour if not in a reasonably
    # sized list
    modified_values = []
    for index, value in enumerate(values):
        modified_values.append({"value": value,
                                "color": color[index]})
    return modified_values

    """
    index = np.arange(len(labels))

    plt.style.use("seaborn")
    plt.bar(index, data, color=color)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.xticks(index, labels, fontsize=8)
    plt.title(title)
    if for_animation:
        plt.savefig("graphImages/animationProcessing/{}.png".format(filename))
    else:
        # TODO: group images by project name as well.
        plt.savefig("graphImages/barGraphs/{}.png".format(filename))
    plt.close()
    """
