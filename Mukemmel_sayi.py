#Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse
#bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
sayi =int(input("bir sayi giriniz:"))

i=1
toplam=0
while (i< sayi):
    if (sayi % i == 0):
        toplam += i
    i += 1
if(toplam == sayi):
    print(sayi,"Mükemmel sayidir")
else:
    print(sayi,"mükemmel sayi değildir")