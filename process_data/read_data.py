def collect_entries(file):
    """ Turns every line in the given file into an Entry object for later
        processing.

        Parameters:
            file (File): the file to read the list of entries from.

        Returns:
            entries (List<Entries>): a list of Entry objects for every line in
            the file.

    """
    pass


# This is just for my own testing
files = ["startingData1.csv",
         "startingData2.csv"]
for f in files:
    collect_entries(f)
