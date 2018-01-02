# coding=utf-8

"""
    Bilgisayar bilgilerini öğrenme
    Bu benim bilgisayarım için doğru bir şekilde çalıştı.
    Ama sizin bilgisayarınızda farklılık gösterebilir veya çalışmayadabilir.
    Eğer Ubuntu kullanıyorsanız %75 doğru çalışacaktır.

"""

import platform

f= platform.version()
e= platform.platform()
d= platform.uname()
c= platform.system()
b= platform.processor()
a= platform.machine()

print """
    İşletim sistemi : {} {}
    Bilgisayar adı  : {}
    Model           : {}
    Sürüm           : {}
    Sürüm tarihi    : {}
""".format(
    a, b,
    c,
    d,
    e,
    f
)


"""
    Uygulamayı çalıştırdığınızda böyle bir sonuç elde etmeniz lazım


    İşletim sistemi : Linux x86_64
    Bilgisayar adı  : MY-LINUX
    Model           : 14.04.1-Ubuntu
    Sürüm           : 3.19.0-47-generic
    Sürüm tarihi    : Ubuntu SMP Mon Jan 18 16:09:14 UTC 2016

"""