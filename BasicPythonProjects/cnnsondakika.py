# -*- coding: utf-8 -*-
import feedparser

url = "http://www.cnnturk.com/feed/rss/news"
haber = feedparser.parse(url)

i = 0
for haber in haber.entries:
    i += 1
    print i
    print haber.title
    print haber.link
    print haber.summary
    print "\n"

