def tambolenleribul(sayi):
    tambolenler = []

    for i in range(2,sayi):

        if (sayi % i == 0):
            tambolenler.append(i)
    return tambolenler

sayi = int(input("Sayi giriniz:"))
print("tam bölenler:",tambolenleribul(sayi))