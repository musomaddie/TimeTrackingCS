import os
import sys
import imageio
from datetime import timedelta

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data/day_of_week")])

from process_data.read_data import make_projects
from graphs.BarGraph import make_bar_graph
from visualise_data.day_of_week.manager import get_time_per_dow
from visualise_data.day_of_week.manager import get_time_per_dow_avg
from visualise_data.day_of_week.manager import get_time_per_dow_med
from visualise_data.day_of_week.manager import find_all_filenames
from visualise_data.day_of_week.manager import find_all_images
from visualise_data.day_of_week.manager import labels
from visualise_data.day_of_week.manager import make_list
from visualise_data.day_of_week.manager import to_hours
from visualise_data.day_of_week.manager import to_minutes


def _colours():
    monday_colour = "#165621"
    tuesday_colour = "#186625"
    wednesday_colour = "#1d872f"
    thursday_colour = "#13a52b"
    friday_colour = "#1abc35"
    saturday_colour = "#22d63f"
    sunday_colour = "#2ae048"
    return [
        monday_colour,
        tuesday_colour,
        wednesday_colour,
        thursday_colour,
        friday_colour,
        saturday_colour,
        sunday_colour
        ]



def _calculate_avg(s, div):
    if div.total_seconds() == 0:
        return 0
    return (s / div) / 60  # to minutes


def _calculate_med(items):
    if len(items) == 0:
        return timedelta()
    if len(items) % 2 != 0:
        return items[len(items) // 2]
    i1 = items[len(items) // 2]
    i2 = items[(len(items) // 2) - 1]
    return (i1 + i2) / 2


def _make_bar_graph(data, y_title, title, filename, for_animation=False):
    make_bar_graph(labels=labels(),
                   data=data,
                   x_title="Day",
                   y_title=y_title,
                   title=title,
                   color=_colours(),
                   filename=filename,
                   for_animation=for_animation)


def _total_bar_graph(entries, project, count="", for_animation=False):
    _make_bar_graph(data=to_hours(make_list(get_time_per_dow(entries))),
                    y_title="Time Spent (hours)",
                    title="{}\nTotal Time Spent By Weekday".format(
                        project.name),
                    filename="{}_total_time_weekday{}".format(
                        project.filename(), count),
                    for_animation=for_animation)


def basic_bar_graph(project):
    """ Creates a bar graph showing the number of hours of work grouped by the
    days of the week """
    _total_bar_graph(project.entries, project)


def average_bar_graph(project):
    """ Creates a bar graph showing the average minutes worked per week grouped
    by the days of the week """
    avg_minutes = make_list(get_time_per_dow_avg(project.entries))

    _make_bar_graph(data=avg_minutes,
                    y_title="Average Time Spent (minutes)",
                    title="{}\nAverage Time Spent By Weekday".format(
                        project.name),
                    filename="{}_avg_time_weekday".format(
                        project.filename()))


def median_bar_graph(project):
    """ Creates a bar graph showing the median minutes worked, grouped by
    the days of the week """
    # TODO: double check calculating the correct value for Monday hogwarts
    # crest
    median_minutes = to_minutes(
        make_list(get_time_per_dow_med(project.entries)))
    _make_bar_graph(data=median_minutes,
                    y_title="Median Time Spent (minutes)",
                    title="{}\nMedian Time Spent By Weekday".format(
                        project.name),
                    filename="{}_med_time_weekday".format(
                        project.filename()))




def animation_bar_graph(project):
    """ Creates a gif of the bar graph as it grows overtime. Only deals with
        the total time stitched """

    # Make diagrams for all the steps
    for i in range(len(project.entries)):
        _total_bar_graph(project.entries_by_order[:i+1], project, i, True)

    # put them all into one image
    find_all_images(find_all_filenames(project), project, "barGraphs")


def make_pie_graph(project):
    """ Creates a pie graph showing the number of hours of work grouped by the
    days of the week """

    days_of_week = get_time_per_dow(project.entries)
    print(days_of_week)


projects = make_projects()
for p in projects:
    basic_bar_graph(projects[p])
    average_bar_graph(projects[p])
    median_bar_graph(projects[p])
    # animation_bar_graph(projects[p])
