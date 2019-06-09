import os
import sys
import imageio
from datetime import timedelta

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data")])

from process_data.read_data import make_projects
from enums.Weekday import Weekday
from graphs.BarGraph import make_bar_graph
from visualise_data.day_of_week_manager import get_time_per_dow


def make_pie_graph(project):
    """ Creates a pie graph showing the number of hours of work grouped by the
    days of the week """

    days_of_week = get_time_per_dow(project.entries)
    print(days_of_week)


projects = make_projects()
for p in projects:
    make_pie_graph(projects[p])
