#!/user/bin/python
from sys import argv
from os import path
import ConfigParser
import RssLib

class Article(object):
    def __init__(self, title, url, date):
        self.title = title
        self.url = url
        self.date = date

    def date(self):
        return self.date

    def title(self):
        return self.title

    def link(self):
        return self.url

class Feed(object):
    def __init__(self, url):
        self.rss = RssLib.RssLib(url).read()
    
    def articles(self):
        final = []
        for r in self.rss['title']:
            index = self.rss['title'].index(r)
            final.append(Article(r, self.rss['link'][index], self.rss['pubDate'][index]))

        return final



class Section(object):
    def __init__(self, section):
        self.section = section
        self.config = ConfigParser.ConfigParser()
        self.config.read(path.expanduser('~/.termnews'))
        
    def feeds(self):
        final = []

        for f in self.config.items(self.section):
            final.append(Feed(f[1]))

        return final

    def list(self):
        for s in self.config.sections():
            print s

class ParamParser(object):
    
    def process(self, section, feed, limit):
        return Section(section)

def show_help():
    print """
The best way to use this is:

termnews [section] [feed] [limit]
ex:
  termnews blog buddy all - this shows all posts in the feed.
  termnews blog buddy 3   - this only shows 3 posts in the feed.
  termnews all all all    - this shows everything from everything.

You can also list your sections:
  
  termnews list

"""

def start():
    
    if len(argv) != 2 and len(argv) != 4:
        print "Please try using --help"
        exit()
    elif len(argv) == 2:
        script, section = argv
        if section == "list":
            Section(section).list()
            exit()
        elif section == "--help":
            show_help()
            exit()
    elif len(argv) == 4:
        script, section, feed, limit = argv
    
    content = ParamParser().process(section, feed, limit)

    for f in content.feeds():
        for a in f.articles():
            print a.title

start()
