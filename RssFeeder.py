import feedparser
import validators
import sys
from Feeder import Feeder
from Feed import Feed
import pprint

class RssFeeder(Feeder):
    """ 
    `Author`: Eliakah kakou

    This class generates a list of feed instances containing relevant data about the file 
    """

    def __init__(self, file):
        """
        `Author`: Eliakah kakou

        The constructor, initializes the RssFeeded instance 

        `file`: path to file containing list of links 
        """
        Feeder.__init__(self, file)
        self.feeds = []
        self.links = []
        self.path = file
        self.__getLinks(file)

    def load_feeds(self):
        """
        `Author`: Eliakah kakou

        returns 'feeds' which contains all of the feed instances 
        """
        self.fetch()
        return self.feeds

    def __getLinks(self, file):
        """
        `Author`: Eliakah kakou

        This method inserts each link from the file as an entry into the 'links' list 

        `file`:path to file containing list of links 
        """
        input_file = open(file)
        try:
            for i, line in enumerate(input_file):
                self.links.append(line)
                # print line,
        finally:
            input_file.close()

    def fetch(self):
        """
        `Author`: Eliakah kakou

        This method appends all of the feed instances to 'feeds'
        """
        for i in range(len(self.links)):
            self.feeds.extend(self.__getFeeds(self.links[i]))

    def __getFeeds(self, url):
        """
        `Author`: Eliakah kakou

        This method generates a Feed instance from the url given

        `file`: full file path

        `return`: Feed generated from file
        """
        flag = validators.url(url)
        if flag:
            feeds = feedparser.parse(url)
        else:
            sys.exit("Invalid Url: Please try again!")

        list = feeds['entries']
        for i in range(len(list)):
            list[i] = Feed(list[i])
            feeds = list

        return feeds

if __name__ == "__main__":
    feeder = RssFeeder('links.txt')
    feeder.fetch()
    feeds = feeder.feeds

    for i in range(len(feeds)):
        pprint.pprint(feeds[i].extract())
