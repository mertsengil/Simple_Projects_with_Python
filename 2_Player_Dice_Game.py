import time
import random
import tkinter as tk
pencere = tk.Tk()
pencere.geometry("350x50+70+70")
etiket = tk.Label(text="Oyun başlatılıyor. . .",font="44")
etiket.pack()
pencere.mainloop()

class zar_oyunu():

    def __init__(self,zar_liste = [1,2,3,4,5,6],score=0):
        self.zar_liste = zar_liste
        self.score=score


    def zar_atma(self):
        self.score = random.sample(self.zar_liste,1)
        return self.score





zar = zar_oyunu()
print("---------------- ZAR OYUNU ----------------\n")
player_1 = input("1. oyuncu lutfen nickinizi giriniz:")
player_2 = input("2. oyuncu lutfen nickinizi giriniz:")
print("Oyun Başlıyor. . .")
time.sleep(1.5)
print("**************************************************")
time.sleep(0.7)

print("1.oyuncu :",player_1," *******-VS-******* 2.oyuncu",player_2)
player_1_hak = 0
player_2_hak = 0
player_1_skor = 0
player_2_skor = 0


while (player_1_hak < 3 and player_2_hak < 3):

    islem = input("1. oyuncu ---> 'q'\n2. oyuncu ---> 'e'\n")

    if (islem == "q"):
        player_1_skor = zar.zar_atma()
        print("Zar Atılıyor...")
        time.sleep(1)
        print(player_1,":",player_1_skor)
        continue
    elif(islem == "e"):
        player_2_skor = zar.zar_atma()
        print("Zar Atılıyor...")
        time.sleep(1)
        print(player_2,":",player_2_skor)

    else:
        print("Geçersiz işlem...")


    if(player_1_skor > player_2_skor):
        player_1_hak += 1
        print("-------------------------------------------------------")
        print("Durum = {} - {}".format(player_1_hak, player_2_hak))
        print("-------------------------------------------------------")
    elif(player_2_skor > player_1_skor):
        player_2_hak += 1
        print("-------------------------------------------------------")
        print("Durum = {} - {}".format(player_1_hak, player_2_hak))
        print("-------------------------------------------------------")
    else:
        print("Eşit değer. . .")
        print("-------------------------------------------------------")
        print("Durum = {} - {}".format(player_1_hak, player_2_hak))
        print("-------------------------------------------------------")


if (player_1_hak > player_2_hak):
    print(player_1,"kazandı. . .Tebrikler ^_^")
else:
    print(player_2,"kazandı. . .Tebrikler ^_^")










