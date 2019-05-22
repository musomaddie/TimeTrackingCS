import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data")])

from process_data.read_data import make_projects
from enums.Weekday import Weekday


def _get_hours_per_dow(entries):
    hours_per_dow = {Weekday.MONDAY: timedelta(),
                     Weekday.TUESDAY: timedelta(),
                     Weekday.WEDNESDAY: timedelta(),
                     Weekday.THURSDAY: timedelta(),
                     Weekday.FRIDAY: timedelta(),
                     Weekday.SATURDAY: timedelta(),
                     Weekday.SUNDAY: timedelta()}
    for e in entries:
        hours_per_dow[e.day_of_week] += e.time_spent
    return hours_per_dow


def _make_list(hours_per_dow):
    return [hours_per_dow[Weekday.MONDAY],
            hours_per_dow[Weekday.TUESDAY],
            hours_per_dow[Weekday.WEDNESDAY],
            hours_per_dow[Weekday.THURSDAY],
            hours_per_dow[Weekday.FRIDAY],
            hours_per_dow[Weekday.SATURDAY],
            hours_per_dow[Weekday.SUNDAY]]

def _to_seconds(hours):
    return [x.total_seconds()/3600 for x in hours]

def bar_graph(project):
    """ Creates a bar graph showing the number of hours of work grouped by the
    days of the week """
    # TODO: refactor creating the bar graph into its own function in own file
    # (once working here)

    hours = _make_list(_get_hours_per_dow(project.entries))
    seconds = _to_seconds(hours)
    print(hours, seconds)
    labels = ["Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              "Sunday"]

    index = np.arange(len(labels))
    plt.bar(index, seconds)
    plt.xlabel("Day", fontsize=5)
    plt.ylabel("Time Spent (hours)", fontsize=5)
    plt.xticks(index, labels, fontsize=5, rotation=5)
    plt.title("Total Time Spent Stitching By Weekday")
    plt.show()

projects = make_projects()
for p in projects:
    bar_graph(projects[p])
