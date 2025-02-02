"""
# İndirme süresini hesaplama
Bu program, bazı oyun servis sağlayıcıları indirme süresini göstermediği için indirme süresini manuel şekilde hesaplamızı sağlıyor.

# Kurulum
indirme sure hesap.py dosyasını indirin ve dosyayı python'la çalıştırın

# Kullanım
Sırasıyla "toplam boyutu, ,inen boyutu, indirme hızını" birimleriyle birlikte girin.
Örn:120.5 GB 500 mb 1 GB
Sadece indirme hızın biriminde büyük küçük harf duyarlı! (Örn: MB, Mb)
Yukarı ok yönü tuşuyla bir önceki değerlerinizi görebilirsiniz.

Uygulama sadece tek seferlik süreyi gösteriyor. Zamanlayıcı başlatmıyor. Anlık Kalan süreyi veya indirilen dosya miktarını göstermiyor.

Toplam verinizi farklı indirme hızlarında kaç dk'da indirileceğini görmek için her seferinde veri miktarınızı yazmanıza gerek yok.


# Düzenlenecekler/Eklenecekler
Hata kodları düzenlenecek
indirilen boyut kısmına bir şey girmeden ( 0 olarak algılanacak )işleme devam edilecek.
indirilecek boyut kısmında matematiksel işlem yapılacak. Kişi 10+5+3 gb yazacak.
küsürleri . yerine , ile de ayırabilecek

"""

class Inecek_Boyut(Exception):
    mesaj = "Toplam boyut, inen boyuttan büyük olmalı"


def Saat(sure):
    'Saniye olarak gelen veriyi "a saat b dakika c saniye" string olarak döndürür'
    saat = int(sure // 3600)
    dakika = int((sure % 3600)//60)
    saniye = int(sure % 60)
    return f"{saat} saat {dakika} dakika {saniye} saniye"

def BoyutHesap(verinin_ilk_boyutu):
    'Liste olarak gelen veriden verinin boyutunu hesaplar. Float olarak döndürür'
    try:
        if verinin_ilk_boyutu[1] == "gb" and verinin_ilk_boyutu[3] == "gb":
            verinin_son_boyutu = (float(verinin_ilk_boyutu[0]) - float(verinin_ilk_boyutu[2]))*1024
        elif verinin_ilk_boyutu[1] == "gb" and verinin_ilk_boyutu[3] == "mb":
            verinin_son_boyutu = float(verinin_ilk_boyutu[0])*1024 - float(verinin_ilk_boyutu[2])
        elif verinin_ilk_boyutu[1] == "mb" and verinin_ilk_boyutu[3] == "mb":
            verinin_son_boyutu = float(verinin_ilk_boyutu[0]) - float(verinin_ilk_boyutu[2])
        elif verinin_ilk_boyutu[1] == "mb" and verinin_ilk_boyutu[3] == "gb":
            verinin_son_boyutu = float(verinin_ilk_boyutu[0]) - float(verinin_ilk_boyutu[2])*1024
        else:
            print("Program veri boyutunu GB veya MB şeklinde desteklemekte")

        if verinin_son_boyutu < 0:      # eğer kişi veri boyutuna istenmeyen bir şey girerse burası NameError hatası veriyor.
            raise Inecek_Boyut
        
        return verinin_son_boyutu
    
    except (IndexError, TypeError, NameError ):
        mesaj = "Boyutu hatalı girdiniz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.\n")

    except Inecek_Boyut as nesne:
        Yanitlayici(nesne.mesaj)
        input("Devam etmek için Enter'a basın.\n")

    except ValueError:
        mesaj = "Sayıyı hatalı girdiniz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.\n")


def HizHesap(hiz):
    'Liste olarak gelen veriden verinin hızını hesaplar. Float olarak döndürür'

    try:
        if hiz[5] == "MB":
            sure = verinin_son_boyutu / float(hiz[4])
        elif hiz[5] == "Mb":
            sure = verinin_son_boyutu / (float(hiz[4])/8)
        elif hiz[5] == "KB":
            sure = verinin_son_boyutu / (float(hiz[4])/1024)
        elif hiz[5] == "Kb":
            sure = verinin_son_boyutu / (float(hiz[4])/8192)
        elif hiz[5] == "GB":
            sure = verinin_son_boyutu / (float(hiz[4])*1024)
        elif hiz[5] == "Gb":
            sure = verinin_son_boyutu / (float(hiz[4])*128)
        else:
            raise TypeError
        mesaj = f"Yaklaşık {Saat(sure)} kaldı"
        return mesaj
    
    except (IndexError, TypeError):
        mesaj = "Boyutu hatalı girdiniz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.\n")

    except (ZeroDivisionError):
        mesaj = "İndirme hızı 0 olamaz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.\n")

    except ValueError:
        mesaj = "Sayıyı hatalı girdiniz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.\n")




def Yanitlayici(mesaj):
    'Yazdırmak istenilen mesajın altına yıldız çizer'
    print("\n",mesaj,"\n","*".center(50,"*"),"\n")    


bastan = True

while (1):

    while (1):           # Eğer girilen değerlerde hata varsa tekrar kullanıcının veriyi girmesi için gereken döngü
        if bastan:          # Programın başlangıcındaki değerlerinin verildiği bölüm
            print('Sırasıyla "toplam boyutu, ,inen boyutu, indirme hızını" birimleriyle birlikte giriniz:')
            print("Örn:120.5 GB 500 mb 1 GB")
            print("!Sadece indirme hızın biriminde büyük küçük harf duyarlı! (Örn: MB, Mb)")
            print("Yukarı ok yönü tuşuyla bir önceki değerlerinizi görebilirsiniz")
        
            veri = str(input())
            veriBoyutHesap = veri.lower().split()
            veriHizHesap = veri.split()

            verinin_son_boyutu = BoyutHesap(veriBoyutHesap)
            if verinin_son_boyutu == None:          # Eğer verinin boyutunun hesaplanmasında sorun varsa döngüyü baştan başlatır
                continue
            else:
                break


        else:           # Sadece indirme hızının değiştirildiği bölüm
            del veriHizHesap[4:]            # Önceki indirme hızıyla ilgili bölüm silinir
            print("İndirme Hızını ve büyüklüğünü giriniz.")
            print("Örn:5 Mb")
            print("!İndirme hızının birimi büyük küçük harf duyarlı! (Örn: MB, Mb, Gb)")
            yeniHiz = str(input()).split()
            veriHizHesap[4:] = yeniHiz          # Yeni indirme hızı verisi eklenir
            break

    mesaj = HizHesap(veriHizHesap)

    if mesaj == None:           # Eğer indirme hızının hesaplanmasında sorun varsa döngüyü baştan başlatır.
        continue


    Yanitlayici(mesaj)          # indirme hızını yazdırır
    bastan = False

    print("Aynı inecek toplam boyuttan devam etmek için Enter'a basın.")
    print("İnecek toplam boyutu değiştirebilmek için 1 yazın")
    print("Çıkış yapmak için q yazın")

    secim = str(input(""))
    while (not(secim == "q" or secim == "1" or secim == "")):           # İşlem sonrası kullanıcıdan 3 farklı seçim alır
        print("Hatalı seçim yaptınız.")
        print("Aynı inecek toplam boyuttan devam etmek için Enter'a basın.")
        print("İnecek toplam boyutu değiştirebilmek için 1 yazın")
        print("Çıkış yapmak için q yazın")

        secim = str(input(""))
    
    if secim == "q":            # Programı sonlandırır
        break
    elif secim == "1":          # Tekrardan indirilecek veriyi girmeyi sağlayacak ayarı yapar
        bastan = True
        Yanitlayici("")