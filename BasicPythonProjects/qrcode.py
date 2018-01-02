import urllib.parse
import urllib.request

try:
    print("\n")

    size = input("Resim Boyutu :")
    veri = input("İçerik :")

    veriler = {
        'size' : size + "x" + size,
        'data' : veri
    }

    # url yapısına uygun şekilde verilerimizi şifreledik.
    parametreler = urllib.parse.urlencode(veriler)

    #api linkimizi oluşturduk
    api_link = "https://api.qrserver.com/v1/create-qr-code/?" + parametreler

    # resim dosyasını indirdik
    urllib.request.urlretrieve(api_link,"kare_kod.png")

    print("\n")
    print("Kare kod başarıyla oluşturuldu.")
    print("kare_kod.png isimli dosyadan ulaşabilirsiniz.")
    print("\n")

except:

    print("Beklenmeyen bir hata oluştu.")