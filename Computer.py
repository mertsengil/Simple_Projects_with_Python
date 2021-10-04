import time


class pc():

    def __init__(self, pc_durum = "kapalı", pc_ses=0, app_list= ["bu bilgisayar","Çöp Kutusu"], apps=["herhangi bir uygulama açık değil"], hafiza=256):
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.app_list = app_list
        self.apps= apps
        self.hafiza = hafiza
    def pc_ac(self):
        if(self.pc_durum == "açık"):
            print("bilgisayar zaten açık")
        else:
            print("Bilgisayar açılıyor. . .")
            time.sleep(1)
            self.pc_durum = "açık"
            print("pc başarıyla açıldı!")
    def pc_kapa(self):
        if (self.pc_durum == "kapalı"):
            print("Bilgisayar zaten kapalı")
        else:
            print("Bilgisayar kapanıyor. . .")
            time.sleep(1)
            self.pc_durum = "kapalı"
            print("pc başarıyla kapandı!")
    def pc_ses_ayarlari(self):
        while True:
            komut = input("komutlar:\n'+'\n'-'\n'q'")
            if(komut == "+"):
                if(self.pc_ses != 30):
                    self.pc_ses +=1
                    print("ses seviyesi: {}".format(self.pc_ses))
            elif(komut == "-"):
                if(self.pc_ses != 0):
                    self.pc_ses -= 1
                    print("ses seviyesi : {}".format(self.pc_ses))
            else:
                print("çıkış yapılıyor. . .")
                time.sleep(1)
                print("Ses seviyesi güncellendi: {}".format(self.pc_ses))
                break
    def uygulama_indir(self,uygulama_ismi):
        if (self.hafiza != 0):
            print("uygulama indiriliyor. . .")
            time.sleep(1)
            print("...")
            self.app_list.append(uygulama_ismi)
            self.hafiza -= len(self.app_list)
            print("Başarıyla indirildi!")
        else:
            print("hafıza dolu")

    def __len__(self):
        return len(self.app_list)
    def __str__(self):
        return "Pc durum:{}\nSes seviyesi:{}\nUygulamalar:{}\nŞuanki açık uygulama:{}\ndepolama alanı:{}".format(self.pc_durum,self.pc_ses,self.app_list,self.apps,self.hafiza)
    def format(self):
        print("Format atılıyor. . .")
        time.sleep(1.5)
        self.app_list = ["bu bilgisayar","Çöp Kutusu"]
        self.hafiza = 256
        print("Başarıyla formatlandı")
    def uygulama_ac(self,uygulama_ismi):
        print("açılıyor. . .")
        time.sleep(1)
        self.apps[0] = uygulama_ismi
        print("Şuanki açık olan uygulama:",self.apps)

pc = pc()
print("""
Mertin bilgisayarı:
Yapmak istediğiniz işlemi seçiniz:
1-)pc aç
2-)pc kapa
3-)pc ses ayarları
4-)uygulama indir
5-)uygulama sayısı öğrenme
6-)pc durum görme
7-)uygulama aç (Henüz çalışmıyor)
8-)format
Çıkış yapmak için 'q'... 
""")
while True:
    islem = input("İşlem seçiniz:")
    if(islem == "q"):
        print("Çıkış Yapılıyor. . .")
        time.sleep(1)
        break
    elif(islem == "1"):
        pc.pc_ac()
    elif (islem == "2"):
        pc.pc_kapa()
    elif (islem == "3"):
        pc.pc_ses_ayarlari()
    elif (islem == "4"):
        uygulama_adi = input("uygulama isimlerini aralarında ',' olacak şekilde giriniz...")
        uygulama_listesi = uygulama_adi.split(",")
        for indirilecekler in uygulama_listesi:
            pc.uygulama_indir(indirilecekler)
    elif (islem == "5"):
        print("uygulama sayisi:",len(pc))
    elif (islem == "6"):
        print(pc)
    elif (islem == "7"):
        uygulama =input("Açmak istediğiniz uygulamanın adini giriniz (Listede olan):")
        pc.uygulama_ac(uygulama)
    elif (islem == "8"):
        pc.format()











