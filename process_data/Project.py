class Project:
    """ This stores data relating to each project.

    Attributes:
        name (String): the name of this project
        entries (List<Entry>): a list of different entries that contribute
            towards this project
    """
    def __init__(self,
                 name,
                 entries):
        self.name = name
        # NOTE: could perhaps open the file based on the project name and add
        # entries here instead of read_data
        self.entries = entries
