import os
import sys
import imageio

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data/day_of_week")])

from graphs.PieChart import make_pie_chart
from process_data.read_data import make_projects
from visualise_data.day_of_week.manager import get_time_per_dow
from visualise_data.day_of_week.manager import find_all_filenames
from visualise_data.day_of_week.manager import find_all_images
from visualise_data.day_of_week.manager import labels
from visualise_data.day_of_week.manager import make_list
from visualise_data.day_of_week.manager import to_hours


def _colours():
    return ["#f93b3b",
            "#f9973b",
            "#f9e63b",
            "#3bf968",
            "#3bddf9",
            "#4e3bf9",
            "#c43bf9"]


def _make_pie_chart(data, filename, title, for_animation):
    make_pie_chart(
        labels=labels(),
        data=data,
        title=title,
        colours=_colours(),
        filename=filename,
        for_animation=for_animation)


def make_pie_graph(entries, project, count="", for_animation=False):
    """ Creates a pie graph showing the number of hours of work grouped by the
    days of the week """
    _make_pie_chart(to_hours(make_list(get_time_per_dow(entries))),
                    "{}_total_time_weekday{}".format(project.filename(),
                                                     count),
                    "{} Total Time Spent Stitching".format(project.name),
                    for_animation)


def animation_pie_graph(project):
    """ Creates a pie graph animation that shows the data changing as entries
    are added. """

    # Graph all the steps
    for i in range(len(project.entries)):
        make_pie_graph(project.entries_by_order[:i+1], project, i, True)

    # Put them all into one image
    find_all_images(find_all_filenames(project), project, "pieCharts")


projects = make_projects()
for p in projects:
    make_pie_graph(projects[p].entries, projects[p])
    # animation_pie_graph(projects[p])
