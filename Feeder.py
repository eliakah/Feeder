class Feeder:
    """
    `Author`: Bill Clark

    An interface to fulfill a strategy pattern design in the Grapher with feeders.
    An implementation of this interface will be usable with the Grapher so long as
    it provides the appropriate returns. 

    Feeder instances should be created with a link to some sort of file. The result
    to come out of it's methods will be used by the Parser Module to generate topics
    about the information in the Feed. A Feed represents a single article of related
    data. The implementation should generate Feed objects as defined above in order
    to be encapsulated. 
    """

    def __init__(self, file):
        """
        A feeder should be initialized to read from it's source when commanded to
        via the load_feeds method. Feeds is a list of Feed objects specifically, 
        and is interacted with in the feeds generator call. 

        `file`: The file to process later. 
        """
        self.feeds = []
        self.path = file

    def contents(self):
        """
        Returns the feeds the Feeder is holding on to via a generator structure.  
        """
        for feed in self.feeds:
            yield feed
            # feeds = []

    def fetch(self):
        """
        Calling this method should retrieve information using the file provided
        at initialization. Following that, that information will be standardized
        into a Feed object and stored in the feeds instance variable. This is going
        to be implemented in very different ways, depending on the file type used. 
        """
        pass

