import os
import sys
import imageio
from datetime import timedelta

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("visualise_data/day_of_week")])

from enums.Weekday import Weekday


def find_all_filenames(project):
    filenames = []
    for i in range(len(project.entries)):
        filenames.append(
            "graphImages/animationProcessing/{}_total_time_weekday{}.png"
            .format(project.filename(), i))
    return filenames


def find_all_images(filenames, project, graph_type):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    # Hold the last images for longer
    for _ in range(20):
        images.append(imageio.imread(
            "graphImages/animationProcessing/{}_total_time_weekday{}.png"
            .format(project.filename(), len(project.entries) - 1)))
    imageio.mimsave(
        "graphImages/{}/{}_total_time_weekday_incremental.gif"
        .format(graph_type, project.filename()), images)


def get_time_per_dow(entries):
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


def get_time_per_dow_avg(entries):
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


def get_time_per_dow_med(entries):
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


def make_list(time_per_dow):
    return [time_per_dow[Weekday.MONDAY],
            time_per_dow[Weekday.TUESDAY],
            time_per_dow[Weekday.WEDNESDAY],
            time_per_dow[Weekday.THURSDAY],
            time_per_dow[Weekday.FRIDAY],
            time_per_dow[Weekday.SATURDAY],
            time_per_dow[Weekday.SUNDAY]]


def to_hours(time):
    return [x.total_seconds()/3600 for x in time]


def to_minutes(time):
    return [x.total_seconds()/60 for x in time]


def labels():
    return["Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday",
           "Saturday",
           "Sunday"]
