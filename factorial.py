print("""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************""")
while True:
    sayi =  input("Sayı:")
    if (sayi == "q"):
        print("Programdan çıkılıyor...")
        break
    sayi = int(sayi)

    faktoriyel = 1
    for i in range(2,sayi+1):
        print("Faktöriyel",faktoriyel,"i",i)
        faktoriyel *= i

    print("Faktoriyel:",faktoriyel)

