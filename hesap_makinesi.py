while(1):
    islem = int(input("1) Toplama, 2) Çıkarma, 3) Çarpma, 4) Bölme, 5) Çıkış: "))

    if islem == 5: break
    if islem == 4:
        bolen = float(input("Bölüneni girin: "))
        bolunen = float(input("Böleni girin: "))

        if bolunen == 0:
            print("Bölüm = sonsuz")
        else:
            print("Bölüm: ", int(bolen // bolunen))
            print("Kalan: ", int(bolen % bolunen))
    else:
        ilk_sayi = float(input("İlk sayıyı girin: "))
        ikinci_sayi = float(input("İkinci sayıyı girin: "))
        
        if islem == 1:
            print("Toplam: ", ilk_sayi + ikinci_sayi)
        elif islem == 2:
            print("Fark: ", ilk_sayi - ikinci_sayi)
        elif islem == 3:
            print("Çarpım: ", ilk_sayi * ikinci_sayi)