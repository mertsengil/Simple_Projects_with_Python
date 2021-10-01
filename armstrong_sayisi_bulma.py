#  Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan
#  herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )
#  o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    basamak = gecici_sayı % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayı //= 10

if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
else:
    print(sayı, "bir armstrong sayısı değildir.")
