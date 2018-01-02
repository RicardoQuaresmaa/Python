# coding=utf-8

import feedparser


print ('''
    ######################################
    #    Ligtv Beşiktaş Haberleri     #
    ######################################
''')
haberler_besiktas = feedparser.parse('http://tr.beinsports.com/rss/takim/besiktas')

i = 1
for haber in haberler_besiktas.entries:
    print i, haber.title
    print "  ", haber.guid, "\n"
    i += 1
