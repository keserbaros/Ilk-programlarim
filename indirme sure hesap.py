# bazı oyun servis sağlayıcıları indirme süresini göstermediği için bu programı kullandığım zamanlar oluyor.


from hesaplamalar import Saat


class Inecek_Boyut(Exception):
    mesaj = "Toplam boyut, inen boyuttan büyük olmalı"


def Yanitlayici(mesaj):
    print(mesaj,"\n","*".center(50,"*"),"\n")    


while (1):
    print('Sırasıyla "toplam boyutu, ,inen boyutu, indirme hızını" birimleriyle birlikte giriniz:')
    print("Örn:120.5 GB 500 mb 1 GB")
    print("!Sadece indirme hızın biriminde büyük küçük harf duyarlı! (Örn: MB, Mb)")
    print("Yukarı ok yönü tuşuyla bir önceki değerlerinizi görebilirsiniz")
    veri = str(input())
    ilk_boyut = veri.lower().split()
    hiz = veri.split()
    try:
        if ilk_boyut[1] == "gb" and ilk_boyut[3] == "gb":
            son_boyut = (float(ilk_boyut[0]) - float(ilk_boyut[2]))*1024
        elif ilk_boyut[1] == "gb" and ilk_boyut[3] == "mb":
            son_boyut = float(ilk_boyut[0])*1024 - float(ilk_boyut[2])
        elif ilk_boyut[1] == "mb" and ilk_boyut[3] == "mb":
            son_boyut = float(ilk_boyut[0]) - float(ilk_boyut[2])
        elif ilk_boyut[1] == "mb" and ilk_boyut[3] == "gb":
            son_boyut = float(ilk_boyut[0]) - float(ilk_boyut[2])*1024
        else:
            print("Program veri boyutunu GB veya MB şeklinde desteklemekte")
        if son_boyut < 0:
            raise Inecek_Boyut
        if hiz[5] == "MB":
            sure = son_boyut / float(hiz[4])
        elif hiz[5] == "Mb":
            sure = son_boyut / (float(hiz[4])/8)
        elif hiz[5] == "KB":
            sure = son_boyut / (float(hiz[4])/1024)
        elif hiz[5] == "Kb":
            sure = son_boyut / (float(hiz[4])/8192)
        elif hiz[5] == "GB":
            sure = son_boyut / (float(hiz[4])*1024)
        elif hiz[5] == "Gb":
            sure = son_boyut / (float(hiz[4])*128)
        else:
            raise TypeError
        Yanitlayici(f"Yaklaşık {Saat(sure)} kaldı")


    except (IndexError, TypeError, NameError ):  # programda ilk doğru ifade girip sonra hızın boyutunu yanlış girince hatayı göstermiyor. Önceki. sonucu gösteriyor
        mesaj = "Boyutu hatalı girdiniz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.")

    except (ZeroDivisionError):
        mesaj = "İndirme hızı 0 olamaz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.")
    
    except ValueError:
        mesaj = "Sayıyı hatalı girdiniz"
        Yanitlayici(mesaj)
        input("Devam etmek için Enter'a basın.")

    except Inecek_Boyut as nesne:
        Yanitlayici(nesne.mesaj)
        input("Devam etmek için Enter'a basın.  ")