#evvelinde pip install feedparser komutuyla feedparser kutuphanesinin yuklenmesi gerekmektedir...
import feedparser
url = 'http://news.google.com.br/news?pz=1&cf=all&ned=us&hl=en&output=rss' 
# just some GNews feed - I'll use a specific search later

feed = feedparser.parse(url)
for post in feed.entries:
   print post.title
   print post.keys()