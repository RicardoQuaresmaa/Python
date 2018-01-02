import urllib.request
import re

try:

    site_adresi = input("Site adresini girin :")
    print("\n")

    html = urllib.request.urlopen(site_adresi)
    html = html.read()
    html = str(html)

    # REGEX ile istediğimiz etiketin tanımını yaptık..
    tanim ="<title>(.*?)</title>"

    # REGEX ile etiketi kaynak kodları içerisinde arıyoruz..
    ara =re.search(tanim,html)

    # Eğer etiket kaynak kodları içerisinde bulunduysa

    if ara:
        etiket = ara.group(0)
        # İstediğimiz etiketi HTML kodu ile birlikte getirdik.
        icerik = ara.group(1)
        # İstediğimiz etiketin sadece içeriğini getirdik.

        print("Etiket :"+etiket)
        print("İçerik :"+icerik)

    else:
        print("İstediğiniz etiket kaynak kodları içerisinde bulunmuyor.")

except:
    print("Beklenmeyen bir hata oluştu.")
