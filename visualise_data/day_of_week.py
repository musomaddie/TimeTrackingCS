import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data")])

from process_data.read_data import make_projects


def bar_graph(projects):
    """ Creates a bar graph showing the number of hours of work grouped by the
    days of the week """
    pass


projects = make_projects()
print(projects)
