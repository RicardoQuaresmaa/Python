# coding=utf-8

import urllib
import re

site = urllib.urlopen('http://www.haberler.com/rssd').read()

regex_hb = '<span class="spotlink">(.*)</span><span class="hbretkt"'
r_haber_basligi = re.compile(regex_hb)
for i in re.findall(r_haber_basligi, site):
    print i