# not hesabının yanında harf karşılığı olsun. altında finalden hangi aralıklarda alırsa hangi not karşılığı olacağı yazsın
# iki ayrı fonksiyon olsun biri not hesabı diğeri dönem sonu ort bulma
# mobil uygulamada üniversite seçme ekranı, bölüm seçme ekranı, dönem seçme ekranı olacak. dersler otomatik gelicek. %'lik en çok kullanı...

def harf_notu(notu):    
    # Bu programa ihtiyac duyabilecek kişilerin genellikle sınavı geçip geçmediğini öğrenmek isteyen kişiler olabileceğini düşündüğüm için sıralamayı 50'ye uzaklığa göre düzenledim düzenledim
    if 30 <= notu and notu < 40: harfNotu = "FD"
    elif 40 <= notu and notu < 60: harfNotu = "DD"
    elif 60 <= notu and notu < 65: harfNotu = "CC"
    elif notu < 30: harfNotu = "FF"
    elif notu < 70: harfNotu = "CB"
    elif notu < 80: harfNotu = "BB"
    elif notu < 90: harfNotu = "BA"
    else: harfNotu = "AA"
    return harfNotu


while (1):
    snv_sayisi = int(input("Girilecek sınav sayısını giriniz: "))
    basari_notu = float(input("Dersi geçmek için gereken notu giriniz: "))
    final_yuzde = 100              # finalin yüzdesini bulmak için for döngüsünde diğer derslerin yüzdelerini finalin yüzdesinden çıkartıyorum
    finalsiz_not = 0   
    for i in range(snv_sayisi-1):
        a = float(input(f"{i+1}. sınavın notu giriniz: "))
        b = float(input(f"{i+1}. sınavın yüzdesini giriniz: "))
        finalsiz_not += a*(b/100)
        final_yuzde -= b           # yüzdeyi hatalı girebilir onu kontrol etmek gerek. c'de do while döngüsü?
    if finalsiz_not >= basari_notu: 
        print("Son sınavdan 0 alsan da dersi geçebiliyorsun.\nNotun: %d\nHarf notun (Final girilmeden): %s", finalsiz_not, harf_notu(finalsiz_not))
    else:
        alman_gereken_not = (basari_notu - finalsiz_not)/(final_yuzde/100)
        print(f"Dersten başarılı olman için alman gereken en az not: {alman_gereken_not}\nHarf notun (Final girilmeden): {harf_notu(finalsiz_not)}")
    # buradan başa dönmek için bir şey koyabilirsin
    # 1 girdiğin zaman mesele
    # c ile yaz esc basınca direkt başa dönsün