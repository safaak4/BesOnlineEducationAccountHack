from twill.commands import *
go('https://besuzaktanegitim.com/')

linklerdosyası = open("linklertxt.txt", "w")

isim = ["Mehmet Bozkurt", "Dilara Katılmış", "Zeynep Sarıkaya", "Senanur Topuz", "Ender Emre Hayırlıoğlu", "Berke Rafet Uluocak" , "Zeynep Özel",
"Cuma Şafak Kara", "Aleyna Yağmur Dinç", "İsmail Çalışkan", "Sarp Kaya", "Hasan Tolga Akkaya", "Ümit Arda", "İrem Tuğçe",
"Sahra Nur Yıldırım", "Melis Nur Türen", "HÜSEYİN EMRE ÇINAR", "EMRE CİNGİLER", "Abdulkerim Güler", "Tuğçe İnce", "Rojin Çelik", "Ahmet Ay", "Lütfü Emir Alakoca",
"Özlem Sel"]

kullaniciadi = ["350296", "350397", "350298", "350299", "350300", "350301", "350302", "350303", "350305", "350306",
                "350307", "350308", "350309", "350310", "350311", "350312", "350314", "350315", "350316", "350317",
                "350318", "350319", "350320", "350321"]

sifre = ["1714MB", "1741DK", "1770ZS", "1771ST", "1775EEH", "1781BRU", "1782ZÖ", "1783CŞK", "1785AYD", "1787İÇ",
         "1789SK", "1793HTA", "1796ÜAT", "1798İTU", "1799SNY", "1802MNT", "1821HEÇ", "1828EC", "1847AG", "1879Tİ",
         "1910RÇ", "1965AA", "1967LEA", "2000ÖS"]

sayac = 0
while sayac <= 23:

    fv("1", "giris_no", kullaniciadi[sayac])
    fv("1", "parola", sifre[sayac])
    submit('1')
    try:
        url(should_be="besuzaktanegitim.com/ogrenci-panel.ntr")
    except:
        print(sifre[sayac], "Kullanici adi veya sifre yanlis.")
        back()
    else:
        print(sifre[sayac], "hesabına girildi. Linkler aliniyor:")
        try:
            print(isim[sayac])
            showlinks()
        except:
            print(sifre[sayac], "linkler alinamadi. geri dönülüyor.")
            back()
        else:
            #linklerdosyası.write(str(isim[sayac]) + "\n" + str(showlinks()) + "\n-----------------------------\n")
            print("link dosyaya alındı!")
            back()
    sayac += 1
