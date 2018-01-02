import urllib.request

site_adresi=input("Web site url :")

header_kodlarım={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
}

istek=urllib.request.Request(site_adresi,headers=header_kodlarım)

html1=urllib.request.urlopen(site_adresi)

html=urllib.request.urlopen(istek)

print("\n İstediğiniz sitenin kaynak kodu : \n\n")

print(html.read())

print("\n İstediğiniz sitenin kaynak kodu1 : \n\n")

print(html1.read())
