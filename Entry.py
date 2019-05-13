class Entry:
    """
    This stores data relating to each timed entry collected.

    Attributes:
        date (datetime.date): the date this entry was started on.
            Equivalent to Date in csv.
        start_time (datetime.time): the time this entry was started
            Equivalent to Start time in the csv.
        end_time (datetime.time): the time we stopped working this entry.
            Equivalent to End time in the csv.
        time_spent (datetime.time): The time we actually spent stitching with
            this (not counting break times).
            Equivalent to rel. Duration in the csv.
        tags (Dictionary<TagType, Tag>): A dictionary of tags associated with
            this entry. These include the enum of the type of data mapped to
            the information about them.
            Equivalent to Tags in the csv.
        day_of_week (Weekday): the day of the week on which this Entry
            occurred.
    """

    def __init__(self,
                 date,
                 start_time,
                 end_time,
                 time_spent,
                 description,
                 tags):
        pass
