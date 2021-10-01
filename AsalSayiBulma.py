#kullanıcıdan aldığınız bir sayının asal sayı olup olmadığını test eden program
def asal_mi(sayi):
    if (sayi == 1):
        return False
    elif(sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False
        return True


while True:
    sayi = input("Bir sayi giriniz:")
    if (sayi == "q"):
        break
    else:
        sayi = int(sayi)
        if(asal_mi(sayi)):
            print(sayi,"ASALDIR")
        else:
            print(sayi,"ASAL DEGILDIR")
