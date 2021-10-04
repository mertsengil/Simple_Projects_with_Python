import random
import time


class kumanda():

    def __init__(self, tv_durum="kapalı", tv_ses=0, kanal_listesi=["Trt"], kanal=["Trt"]):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if (self.tv_durum == "açık"):
            print("tv zaten açık. . .")
        else:
            print("tv açılıyor. . .")
            time.sleep(1)
            self.tv_durum = "açık"
    def tv_kapa(self):
        if(self.tv_durum == "kapalı"):
            print("tv zaten kapalı. . .")
        else:
            print("tv kapanıyor. . .")
            time.sleep(1)
            self.tv_durum = "kapalı"
    def ses_ayarları(self):

        while True:
            cevap = input("sesi arttır: '>'\nsesi azalt: '<'\nçıkış: çıkış")
            if (cevap == ">"):
                if(self.tv_ses != 30):
                    self.tv_ses += 1
                    print("ses seviyesi:",self.tv_ses)
            elif (cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("ses seviyesi:",self.tv_ses)
            else:
                print("çıkış yapılıyor. . .")
                time.sleep(1)
                print("ses güncellendi:",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi. . .")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("şu anki kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durum: {}\n Tv ses: {}\n Kanal Listesi: {}\n Şuanki kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
    def sessiz_mod(self):
        self.tv_ses=0
        print("Ses seviyesi = 0")
kumanda = kumanda()
print("""
---Televizyon Kumandası---
1-)Tv aç
2-)Tv kapa
3-)Ses ayarları
4-)Kanal ekle
5-)Kanal sayısını öğrenme
6-)Rastgele kanala geçme
7-)Televizyon bilgileri
8-)sessiz mod aç
{Çıkış yapmak için 'q' ya basınız}
""")
while True:
    işlem = input("Yapmak istediğiniz işlemi seçiniz:")

    if (işlem == "q") :
        print("Çıkış yapılıyor. . .")
        break
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapa()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini arada ',' yazarak giriniz:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal sayısı",len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    elif (işlem == "8"):
        kumanda.sessiz_mod()
    else:
        print("geçersiz işlem")





