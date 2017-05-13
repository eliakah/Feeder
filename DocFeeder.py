import fnmatch
import platform
import time
import os
from Feeder import Feeder
from Feed import Feed
import pprint

class DocFeeder(Feeder):
    """ 
     `Author`: Eliakah kakou

     This class recursively access each file in a given directory,
     then generates a list of feed instances containing relevant data about the file 
    """

    def __init__(self, file):
        """
        `Author`: Eliakah kakou

        The constructor, initializes the DocFeeded instance 

        `file`: directory path
        """
        Feeder.__init__(self, file)
        self.feeds = []
        self.paths = []
        self.path = file
        self.__getPaths(file)

    def __getPaths(self, file):
        """
        `Author`: Eliakah kakou

        This method inserts each link from the file as an entry into the 'paths' list

        `file`: path to original directory
        """
        # print "getting Paths"
        matches = []
        for filename in self.__find_files(file, "*.*"):
            matches.append(filename)
        self.paths = matches

    def __find_files(self, directory, pattern):
        """
        `Author`: Eliakah kakou

        This method yields every single file in the directory matching the pattern

        `directory`: directory path

        `pattern`: file name pattern

        `return`: file paths matching pattern
        """
        # print "finding files"
        for root, dirs, files in os.walk(directory):
            for basename in files:
                if fnmatch.fnmatch(basename, pattern):
                    filename = os.path.join(root, basename)
                    yield filename

    def fetch(self):
        """
        `Author`: Eliakah kakou

        This method appends all of the feed instances to 'feeds'
        """
        # print "fetching ..."
        for i in range(len(self.paths)):
            self.feeds.append(self.__getFeeds(self.paths[i]))

    def load_feeds(self):
        """
        `Author`: Eliakah kakou

        `return`: 'feeds' which contains all of the feed instances 
        """
        # print "Loading feeds"
        self.fetch()
        return self.feeds

    def __getFileName(self, path):
        """
        `Author`: Eliakah kakou

        This method extracts the file name from the path

        `path`: full path to the file 

        `return`: the file name 
        """
        drive, path = os.path.splitdrive(path)
        path, filename = os.path.split(path)
        name = filename.split(".")
        return name[0]

    def __getFeeds(self, file):
        """
        `Author`: Eliakah kakou

        This method generates a Feed instance from the file given

        `file`: full file path

        `return`: Feed generated from file
        """
        title = self.__getFileName(file)
        input_file = open(file)
        try:
            content = input_file.read()
        finally:
            input_file.close()

        stamp = time.ctime(self.__creation_date(file))

        f = {'id': file, 'published': stamp, 'title': title, 'link': file, 'summary': content}
        f = Feed(f)
        return f

    def __creation_date(self, file):
        """
        `Author`: Eliakah kakou

        This method returns the creation date of the file, 
        or replaces with the last modified if the former is unavailable 

        `return`: date on which file was created
    ...
        """
        if platform.system() == 'Windows':
            return os.path.getctime(file)
        else:
            stat = os.stat(file)
            try:
                return stat.st_birthtime
            except AttributeError:
                return stat.st_mtime

if __name__ == "__main__":
    feeder = DocFeeder('../../')
    feeds = feeder.load_feeds()

    for i in range(len(feeds)):
        pprint.pprint(feeds[i].extract())