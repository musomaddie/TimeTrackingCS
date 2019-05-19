import csv
from Entry import Entry


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


# This is just for my own testing
# NOTE: this requires this to be run in the same location as these files
files = ["startingData1.csv",
         "startingData2.csv"]
for f in files:
    collect_entries(f)
