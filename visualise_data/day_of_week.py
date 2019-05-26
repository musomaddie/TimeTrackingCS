import os
import sys
from datetime import timedelta

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data")])

from process_data.read_data import make_projects
from enums.Weekday import Weekday
from graphs.BarGraph import make_bar_graph


def _colours():
    monday_colour = "#165621"
    tuesday_colour = "#186625"
    wednesday_colour = "#1d872f"
    thursday_colour = "#13a52b"
    friday_colour = "#18c935"  # Change
    saturday_colour = "#58e870"  # Change
    sunday_colour = "#83e293"  # Change
    return [
        monday_colour,
        tuesday_colour,
        wednesday_colour,
        thursday_colour,
        friday_colour,
        saturday_colour,
        sunday_colour
        ]


def _get_time_per_dow(entries):
    time_per_dow = {Weekday.MONDAY: timedelta(),
                    Weekday.TUESDAY: timedelta(),
                    Weekday.WEDNESDAY: timedelta(),
                    Weekday.THURSDAY: timedelta(),
                    Weekday.FRIDAY: timedelta(),
                    Weekday.SATURDAY: timedelta(),
                    Weekday.SUNDAY: timedelta()}
    for e in entries:
        time_per_dow[e.day_of_week] += e.time_spent
    return time_per_dow


def _calculate_avg(s, div):
    if div.total_seconds() == 0:
        return 0
    return (s / div) / 60  # to minutes


def _get_time_per_dow_avg(entries):
    count_for_day = {Weekday.MONDAY: 0,
                     Weekday.TUESDAY: 0,
                     Weekday.WEDNESDAY: 0,
                     Weekday.THURSDAY: 0,
                     Weekday.FRIDAY: 0,
                     Weekday.SATURDAY: 0,
                     Weekday.SUNDAY: 0}
    time_per_dow = {Weekday.MONDAY: timedelta(),
                    Weekday.TUESDAY: timedelta(),
                    Weekday.WEDNESDAY: timedelta(),
                    Weekday.THURSDAY: timedelta(),
                    Weekday.FRIDAY: timedelta(),
                    Weekday.SATURDAY: timedelta(),
                    Weekday.SUNDAY: timedelta()}
    for e in entries:
        time_per_dow[e.day_of_week] += e.time_spent
        count_for_day[e.day_of_week] += 1
    avg_per_dow = {
        Weekday.MONDAY: _calculate_avg(
            time_per_dow[Weekday.MONDAY],
            timedelta(seconds=count_for_day[Weekday.MONDAY])),
        Weekday.TUESDAY: _calculate_avg(
            time_per_dow[Weekday.TUESDAY],
            timedelta(seconds=count_for_day[Weekday.TUESDAY])),
        Weekday.WEDNESDAY: _calculate_avg(
            time_per_dow[Weekday.WEDNESDAY],
            timedelta(seconds=count_for_day[Weekday.WEDNESDAY])),
        Weekday.THURSDAY: _calculate_avg(
            time_per_dow[Weekday.THURSDAY],
            timedelta(seconds=count_for_day[Weekday.THURSDAY])),
        Weekday.FRIDAY: _calculate_avg(
            time_per_dow[Weekday.THURSDAY],
            timedelta(seconds=count_for_day[Weekday.FRIDAY])),
        Weekday.SATURDAY: _calculate_avg(
            time_per_dow[Weekday.THURSDAY],
            timedelta(seconds=count_for_day[Weekday.SATURDAY])),
        Weekday.SUNDAY: _calculate_avg(
            time_per_dow[Weekday.SUNDAY],
            timedelta(seconds=count_for_day[Weekday.SUNDAY]))}
    return avg_per_dow


def _calculate_med(items):
    if len(items) == 0:
        return timedelta()
    if len(items) % 2 != 0:
        return items[len(items) // 2]
    i1 = items[len(items) // 2]
    i2 = items[(len(items) // 2) - 1]
    return (i1 + i2) / 2


def _get_time_per_dow_med(entries):
    time_per_dow = {Weekday.MONDAY: [],
                    Weekday.TUESDAY: [],
                    Weekday.WEDNESDAY: [],
                    Weekday.THURSDAY: [],
                    Weekday.FRIDAY: [],
                    Weekday.SATURDAY: [],
                    Weekday.SUNDAY: []}
    for e in entries:
        time_per_dow[e.day_of_week].append(e.time_spent)
    return {
        Weekday.MONDAY: _calculate_med(time_per_dow[Weekday.MONDAY]),
        Weekday.TUESDAY: _calculate_med(time_per_dow[Weekday.TUESDAY]),
        Weekday.WEDNESDAY: _calculate_med(time_per_dow[Weekday.WEDNESDAY]),
        Weekday.THURSDAY: _calculate_med(time_per_dow[Weekday.THURSDAY]),
        Weekday.FRIDAY: _calculate_med(time_per_dow[Weekday.FRIDAY]),
        Weekday.SATURDAY: _calculate_med(time_per_dow[Weekday.SATURDAY]),
        Weekday.SUNDAY: _calculate_med(time_per_dow[Weekday.SUNDAY])}


def _make_list(time_per_dow):
    return [time_per_dow[Weekday.MONDAY],
            time_per_dow[Weekday.TUESDAY],
            time_per_dow[Weekday.WEDNESDAY],
            time_per_dow[Weekday.THURSDAY],
            time_per_dow[Weekday.FRIDAY],
            time_per_dow[Weekday.SATURDAY],
            time_per_dow[Weekday.SUNDAY]]


def _to_hours(time):
    return [x.total_seconds()/3600 for x in time]


def _to_minutes(time):
    return [x.total_seconds()/60 for x in time]


def _labels():
    return["Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Saturday",
           "Sunday"]


def basic_bar_graph(project):
    """ Creates a bar graph showing the number of hours of work grouped by the
    days of the week """
    hours = _to_hours(_make_list(_get_time_per_dow(project.entries)))

    make_bar_graph(labels=_labels(),
                   data=hours,
                   xLabel="Day",
                   yLabel="Time Spent (hours)",
                   title="{}\nTotal Time Spent By Weekday".format(
                       project.name),
                   color=_colours(),
                   filename="{}_total_time_weekday".format(
                       project.name.replace(" ", "_")))


def average_bar_graph(project):
    """ Creates a bar graph showing the average minutes worked per week grouped
    by the days of the week """
    avg_minutes = _make_list(_get_time_per_dow_avg(project.entries))

    make_bar_graph(labels=_labels(),
                   data=avg_minutes,
                   xLabel="Day",
                   yLabel="Average Time Spent (minutes)",
                   color=_colours(),
                   title="{}\nAverage Time Spent By Weekday".format(
                       project.name),
                   filename="{}_avg_time_weekday".format(
                       project.name.replace(" ", "_")))


def median_bar_graph(project):
    """ Creates a bar graph showing the median minutes worked, grouped by
    the days of the week """
    # TODO: double check calculating the correct value for Monday hogwarts
    # crest
    median_minutes = _to_minutes(
        _make_list(_get_time_per_dow_med(project.entries)))
    make_bar_graph(labels=_labels(),
                   data=median_minutes,
                   xLabel="Day",
                   yLabel="Median Time Spent (minutes)",
                   title="{}\nMedian Time Spent By Weekday".format(
                       project.name),
                   color=_colours(),
                   filename="{}_med_time_weekday".format(
                       project.name.replace(" ", "_")))


projects = make_projects()
for p in projects:
    basic_bar_graph(projects[p])
    average_bar_graph(projects[p])
    median_bar_graph(projects[p])
