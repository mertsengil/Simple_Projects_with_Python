import math
from time import sleep
print("""
  |*****************************************|
  |Hesap makinesi (Developed by Mert Şengil)|
  |*****************************************|
""")
print("""Yapmak istediğiniz işlemi seçiniz:
1 - {Toplama}
2 - {Çıkarma}
3 - {Çarpma}
4 - {Bölme}
5 - {Kök Alma}
6 - {10 Tabanında Logaritma Alma}
7 - {Faktoriyel Alma}
8 - {X Tabanında Y'nin Logaritmasını Bulma}
-----------------------------------------
q - {Çıkış}""")
while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz:")
    if (işlem == "q"):
        print("Programdan Çıkılıyor...")
        sleep(1)
        print("Çıkış yapıldı. İyi Günler...")
    elif (işlem == "1"):
        print("***Toplama işlemi seçtiniz***")
        a = int(input("1. Sayı:"))
        b = int(input("2. Sayı:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("{} + {} = {}".format(a,b,a+b))
    elif (işlem == "2"):
        print("***Çıkarma işlemi seçtiniz***")
        a = int(input("1. Sayı:"))
        b = int(input("2. Sayı:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("{} - {} = {}".format(a, b, a - b))
    elif (işlem == "3"):
        print("***Çarpma işlemi seçtiniz***")
        a = int(input("1. Sayı:"))
        b = int(input("2. Sayı:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("{} * {} = {}".format(a, b, a * b))
    elif (işlem == "4"):
        print("***Bölme işlemi seçtiniz***")
        a = int(input("1. Sayı:"))
        b = int(input("2. Sayı:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("{} / {} = {}".format(a, b, a / b))
    elif (işlem == "5"):
        print("***Kök Alma işlemi seçtiniz***")
        a = int(input("Kökünü Almak İstediğiniz Sayı:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        a = a ** 0.5
        print("--->",a)
    elif (işlem == "6"):
        print("*** 10 Tabanında logaritma alma işlemi seçtiniz***")
        a = int(input("10 tabanında logaritmasını almak istediğiniz sayıyı giriniz:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("--->",math.log10(a))
    elif (işlem == "7"):
        print("*** Faktoriyel işlemini seçtiniz ***")
        a = int(input("Faktoriyelini almak istediğiniz sayıyı giriniz:"))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("---> ", math.factorial(a))
    elif (işlem == "8"):
        print("*** X Tabanında Y'nin Logaritmasını Bulma İşlemini Seçtiniz ***")
        x = int(input("x tabanı: "))
        y = int(input("Y: "))
        print("Hesaplanıyor. . .")
        sleep(1)
        print("---> ", math.log(y,x))
    else:
        print("Geçersiz işlem... Lutfen işlem menüsünü tekrar inceleyiniz. . .")








