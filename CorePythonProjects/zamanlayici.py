# -*- coding: utf-8 -*-
import time

zaman = time.localtime()
yil = zaman[0]
ay = zaman[1]
gun = zaman[2]
saat = zaman[3]
dakika = zaman[4]
saniye = zaman[5]

def tarih():
    print("""
    tarih: {}/{}/{}
    saat : {}:{}:{}
    """).format(gun, ay, yil, saat, dakika, saniye)

if __name__ == '__main__':
    tarih()