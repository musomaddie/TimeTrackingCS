from datetime import date
from datetime import time
from datetime import timedelta

import csv
import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("process_data")])
from enums.TagType import TagType
from enums.Weekday import Weekday


class Entry:
    """
    This stores data relating to each timed entry collected.

    Attributes:
        date (datetime.date): the date this entry was started on.
            Equivalent to Date in csv. In the format month/day/yy
        start_time (datetime.time): the time this entry was started
            Equivalent to Start time in the csv. In the format hours:minutes
        end_time (datetime.time): the time we stopped working this entry.
            Equivalent to End time in the csv.
        time_spent (datetime.timedelta): The time we actually spent stitching
            this (not counting break times).
            Equivalent to rel. Duration in the csv.
        tags (Dictionary<TagType, Tag>): A dictionary of tags associated with
            this entry. These include the enum of the type of data mapped to
            the information about them.
            Equivalent to Tags in the csv.
        day_of_week (Weekday): the day of the week on which this Entry
            occurred.
    """

    def _make_date(self, d):
        month, day, year = d.split("/")
        return date(int("20" + year), int(month), int(day))

    def _make_time(self, t):
        hours, minutes = [int(x) for x in t.split(":")]
        return time(hours, minutes)

    def _make_time_difference(self, time_spent):
        hours, minutes, seconds = [int(x) for x in time_spent.split(":")]
        # Seconds are discarded -> they are all 0s
        return timedelta(hours=hours, minutes=minutes)

    def _make_day_of_week(self):
        weekday = self.date.weekday()
        if weekday == 0:
            return Weekday.MONDAY
        if weekday == 1:
            return Weekday.TUESDAY
        if weekday == 2:
            return Weekday.WEDNESDAY
        if weekday == 3:
            return Weekday.THURSDAY
        if weekday == 4:
            return Weekday.FRIDAY
        if weekday == 5:
            return Weekday.SATURDAY
        return Weekday.SUNDAY

    def _make_tags(self, tags):
        # Helper to check if valid colour
        def _all_dmc_colours():
            dmc_file = "flosscolours.csv"
            all_dmc_names = []
            with open(dmc_file, 'r') as f:
                csvreader = csv.reader(f)
                # Skip the first line
                next(csvreader)
                for line in csvreader:
                    all_dmc_names.append(line[0])
            return set(all_dmc_names)

        # Helper to return valid activities
        def _valid_activities():
            return ["gridding"]

        # Assigning the tags
        tags = [x.strip() for x in tags.split(",")]
        processed_tags = {}
        for tag in tags:
            # location, starts with: "on", "at"
            if tag.lower().startswith("on") or tag.lower().startswith("at"):
                processed_tags[TagType.LOCATION] = " ".join(tag.split(" ")[1:])
            # activity, chosen from valid options
            if tag.lower() in _valid_activities():
                processed_tags[TagType.ACTIVITY] = tag
            # colour, valid dmc according to file (file located in home dir)
            if tag in _all_dmc_colours():
                processed_tags[TagType.COLOUR] = tag
                processed_tags[TagType.ACTIVITY] = "stitching"
            # page, starts with: "page"
            if tag.lower().startswith("page"):
                processed_tags[TagType.PAGE] = " ".join(tag.split(" ")[1:])
            # background activity, starts with "watching"
            if tag.lower().startswith("watching"):
                processed_tags[TagType.BACKGROUND] = tag
        return processed_tags

    def __init__(self,
                 d,
                 start_time,
                 end_time,
                 time_spent,
                 description,
                 tags):
        self.date = self._make_date(d)
        self.start_time = self._make_time(start_time)
        self.end_time = self._make_time(end_time)
        self.time_spent = self._make_time_difference(time_spent)
        self.tags = self._make_tags(tags)
        self.day_of_week = self._make_day_of_week()
