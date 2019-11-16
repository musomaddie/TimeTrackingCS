import pygal
from pygal.style import Style


def _find_percent(data, i):
    this_item = data[i]
    total_sum = sum(x for x in data)

    return this_item / total_sum * 100


def _make_display_label(label, data, i):
    return "{}: {:.1f}%".format(label[i],
                                (data[i] / sum(x for x in data)) * 100)


def _display_percent(data, i):
    return "{:.1f}%".format(data[i] / sum(x for x in data) * 100)


def make_pie_chart(labels,
                   data,
                   colours,
                   title,
                   filename,
                   for_animation=False):
    pie_chart = pygal.Pie(title=title,
                          print_labels=True,
                          style=Style(colors=colours))
    for i, label in enumerate(labels):
        # TODO: make label text look pretty
        pie_chart.add(label, [{'value': data[i],
                               'label': _display_percent(data, i)}])
    if for_animation:
        pie_chart.render_to_png(
            "graphImages/animationProcessing/pie/{}.png".format(filename))
        # TODO: if processing for animation go through and delete all halfway
        # images when complete -> means can get rid of some subfolders too
    else:
        pie_chart.render_to_png(
            "graphImages/pieCharts/{}.png".format(filename))
