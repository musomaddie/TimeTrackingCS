import os
import sys
import imageio

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data/day_of_week")])

from graphs.PieChart import make_pie_chart
from process_data.read_data import make_projects
from visualise_data.day_of_week.manager import get_time_per_dow
from visualise_data.day_of_week.manager import make_list
from visualise_data.day_of_week.manager import to_hours
from visualise_data.day_of_week.manager import labels


def _make_pie_chart(data, filename):
    make_pie_chart(
        labels=labels(),
        data=data,
        filename=filename)


def make_pie_graph(project):
    """ Creates a pie graph showing the number of hours of work grouped by the
    days of the week """

    _make_pie_chart(to_hours(make_list(get_time_per_dow(project.entries))),
                    project.filename())


projects = make_projects()
for p in projects:
    make_pie_graph(projects[p])
