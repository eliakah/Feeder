# * Created by Eliakah kakou
# Main.py
# This class allows you call and test all classes
import sys

from Feeder import Feeder


def main():

    feeder = Feeder('http://popculturebrain.com/rss')
   # feeder = Feeder('http://rss.cnn.com/rss/cnn_topstories.rss')
    feeds = feeder.load_feeds()

    for i in range(len(feeds)):
            print  feeds[i].extract()



main()
