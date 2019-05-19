import csv
import os
import sys

sys.path.insert(0,
                os.path.dirname(os.path.realpath(__file__))[
                    0:-len("process_data")])

from process_data.Entry import Entry
from process_data.Project import Project


def collect_entries(file):
    """ Turns every line in the given file into an Entry object for later
        processing.

        Parameters:
            file (File): the file to read the list of entries from.
                The contents of the file is as follows:
                    [Date,Start time,End time,Duration,
                    rel. Duration,Project,Description,Tags]

        Returns:
            entries (List<Entries>): a list of Entry objects for every line in
            the file.

    """
    entries = []
    with open(file, 'r') as f:
        csvreader = csv.reader(f)
        # Skip the first line
        next(csvreader)
        for line in csvreader:
            entries.append(Entry(line[0],  # date
                                 line[1],  # start time
                                 line[2],  # end time
                                 line[4],  # total stitching time
                                 line[6],  # description
                                 line[7])  # tags
                           )
    return entries


def make_projects():
    # NOTE: the content of this will change later, currently is just to allow
    # my own testing
    files = ["startingData1.csv",
             "startingData2.csv"]
    projects = {}
    p = ["Harry Potter Book Collage",
         "Hogwarts Crest"]
    i = 0
    for f in files:
        projects[p[i]] = Project(p[i], collect_entries(f))
        i += 1
    return projects
