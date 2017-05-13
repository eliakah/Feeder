class Feed:
    """
    `Author`: Eliakah kakou

    This class allows for more functionality in regards
    to the dictionary entered in the constructor
    """

    def __init__(self, feed):
        """
        `Author`: Eliakah kakou

        The constructor 

        `feed`: dict instance containing set of information about feed
        """
        self.feed = feed

    def extract(self):
        """
        `Author`: Eliakah kakou

        This method returns a subset of the dictionary
        """
        return {k: self.feed[k] for k in ('id', 'published', 'title', 'link', 'summary')}

    def record_content(self):
        return self.feed['link'], self.feed['published']
