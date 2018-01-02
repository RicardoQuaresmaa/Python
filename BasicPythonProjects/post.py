import urllib.request
import urllib.parse

site_adresi="http://criexe.com/"

header_kodlarım={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}

veriler = {
    "kullanici_adi" : "bunyamin",
    "sifre"         : "bunyamin2006",
    "email"         : "bunyamineymen@gmail.com",
    "isim"          : "Bünyamin Eymen Alagöz"
}

parametreler = urllib.parse.urlencode(veriler)
parametreler = parametreler.encode('utf-8')

istek =urllib.request.Request(site_adresi, data=parametreler,headers=header_kodlarım)

html =urllib.request.urlopen(istek)

print(html.read())






