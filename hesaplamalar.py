def Fakt(a):
    "Faktöriyel döndürür"
    if a == 1: return 1
    else: return Fakt(a-1) * a

def Perm(n,r):
    "Permitasyonu döndürür"
    per = 1
    for i in range(int(n),int(n)-int(r),-1):
        per = per*i
    return per

def Komb(n,r):
    "Kombinasyon döndürür"
    return Perm(n,r)/Fakt(r)

def Asal(a):
    "Asallığını döndürür"
    if a == 2: return True
    elif a%2 == 0: return False
    elif a < 2: return False
    for i in range(3,int(a**0.5+2),2):
        if a%i == 0: return False
    return True

def Asalbul(a,b):
    "Girilen aralıktaki asal sayıları liste şeklinde döndürür"
    asallar = []
    for i in range(a,b):
        if Asal(i):
            asallar += [i]
    return asallar

def Ekok(a,b):
    "Ekok döndürür"
    for i in range(min(a,b),1,-1):
        if a%i == 0 and b%i == 0:
            return i

def Ebob(a,b):
    "Ebob döndürür"
    return (a/Ekok(a,b))*b

def Yazilisi(sayi):
    "100k ye kadar olan sayılara kadar yazılışlarını döndürür"
    birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
    if sayi > 10000: 
        return onlar[sayi//10000] + birler[sayi%10000//1000] + "Bin" + birler[sayi%1000//100] + "Yüz" + onlar[sayi%100//10] + birler[sayi%10]
    elif sayi > 2000:
        return birler[sayi//1000] + "Bin" + birler[sayi%1000//100] + "Yüz" + onlar[sayi%100//10] + birler[sayi%10]
    elif sayi > 1000:
        return "Bin" + birler[sayi%1000//100] + "Yüz" + onlar[sayi%100//10] + birler[sayi%10]
    elif sayi > 200:
        return birler[sayi//100] + "Yüz" + onlar[sayi%100//10] + birler[sayi%10]
    elif sayi > 100:
        return "Yüz" + onlar[sayi%100//10] + birler[sayi%10]
    else:
        return onlar[sayi//10] + birler[sayi%10]

def Dost(a,b):
    "Hatalı çalışıyor"
    bolenler_1 = bolenler_2 = 1
    for i in range(2,int(a**.5)+2):
        if a%i == 0:
            bolenler_2 += i
            if i != a/i:
                bolenler_2 += a/i
    for i in range(2,int(b**.5)+2):
        if b%i == 0:
            bolenler_1 += i
            if i != b/i:
                bolenler_1 += b/i
    if bolenler_1 == bolenler_2:
        return "Dost sayılar"
    else: 
        return "dost sayı değiller",bolenler_1,bolenler_2

def Saat(sure):
    'Saniye olarak giren sayıyı "a saat b dakika c saniye" olarak döndürür'
    saat = int(sure // 3600)
    dakika = int((sure % 3600)//60)
    saniye = int(sure % 60)
    return f"{saat} saat {dakika} dakika {saniye} saniye"