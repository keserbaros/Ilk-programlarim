while (1):
    islem=int(input("Yapmak istediğiniz işlemi seçin:\n1)Vücut kütle indeksi hesaplama\n2)İstediğin kategoriye göre kaç kilo olman gerektiğini öğrenme\n"))
    boy=float(input("Boyunuzu giriniz (Örnek: 1.72): "))
    if islem==1:
        kilo=float(input("Kilonuzu giriniz: "))
        indeksi=kilo/(boy*boy)
        if 18.5>=indeksi:
            print("Vücut kütle indeksiniz: ",indeksi,"Zayıf.","Alman gereken kilo:",18.5*boy*boy-kilo)
        elif 25>=indeksi and indeksi>18.5:
            print("Vücut kütle indeksiniz:",indeksi,"Normal")
        elif 30>=indeksi and indeksi>25:
                print("Vücut kütle indeksiniz:",indeksi,"Kilolu.","Vermen gereken kilo:",kilo-25*boy*boy)
        elif 35>=indeksi and indeksi>30:
            print("Vücut kütle indeksiniz:",indeksi,"Şişman.","Vermen gereken kilo:",kilo-25*boy*boy)
        elif indeksi>35:
            print("Vücut kütle indeksiniz:",indeksi,"Obez.","Vermen gereken kilo:",kilo-25*boy*boy)
    elif islem==2:
        sınıf=int(input("Olmak istediğiniz kategoriyi seçin.\n1)Zayıf\n2)Normal\n3)Kilolu\n4)Şişman\n4)Obez\n"))
        if sınıf==1:
            print("En fazla",18.5*boy*boy,"kg olman gerek")
        elif sınıf==2:
            print("En fazla",25*boy*boy,"kg olman gerek")
            print("En az",18.5*boy*boy,"kg olman gerek")
        elif sınıf==3:
            print("En fazla",30*boy*boy,"kg olman gerek")
            print("En az",25*boy*boy,"kg olman gerek")
        elif sınıf==4:
            print("En fazla",35*boy*boy,"kg olman gerek")
            print("En az",30*boy*boy,"kg olman gerek")