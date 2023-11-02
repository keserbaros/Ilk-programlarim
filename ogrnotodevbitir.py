#Bitmedi

from tkinter import *

def ekle(a):
    if a == 1:
        list_ogr.insert(END, f"{ogr_no_2.get()} {ad_2.get()} {soyad_2.get()}")        # .get() komutu ile çağırdığın zaman str olarak geliyor
    elif a == 2:
        list_drs.insert(END, f"{drs_kod_2.get()} {drs_ad_2.get()}")
    elif a == 3:
        list_not.insert(END, f"{vize_n_2.get()} {final_n_2.get()}")
def sil(a):
    if a == 1:
        print(list_ogr.index("a a a"))

pen = Tk()

frame_ogr = Frame(pen,relief= SUNKEN,border= 5)                                             # Eğer gridleri ayrı yazmassan etki etmiyor
frame_ders = Frame(pen,relief= SUNKEN,border= 5)
frame_not = Frame(pen,relief= SUNKEN,border= 5)

frame_ogr.grid(row= 0,column= 0)
frame_ders.grid(row= 0,column= 1)
frame_not.grid(row= 0,column= 2)

baslik_1 = Label(frame_ogr,text= "Öğrenciler",font= "calibri 18")
ogr_no_1 = Label(frame_ogr,text= "Öğrno:",anchor= E,width= 7)
ogr_no_2 = Entry(frame_ogr)
ad_1 = Label(frame_ogr,text= "Adı:",anchor= E,width= 7)
ad_2 = Entry(frame_ogr)
soyad_1 = Label(frame_ogr,text= "Soyadı:",anchor= E,width=7)
soyad_2 = Entry(frame_ogr)
list_ogr = Listbox(frame_ogr,selectmode= MULTIPLE)
ekle_1 = Button(frame_ogr,text= "Ekle", command= lambda:ekle(1))
sil_1 = Button(frame_ogr,text= "Seçili olanları sil", command= lambda:sil(1))

baslik_1.grid(row= 0,column= 0,columnspan= 2)
ogr_no_1.grid(row= 1,column= 0)
ogr_no_2.grid(row= 1,column= 1)
ad_1.grid(row= 2,column= 0)
ad_2.grid(row= 2,column= 1)
soyad_1.grid(row= 3,column= 0)
soyad_2.grid(row= 3,column= 1)
ekle_1.grid(row= 4,column= 1)
list_ogr.grid(row= 5,column= 1)
sil_1.grid(row= 6,column= 1)



baslik_2 = Label(frame_ders,text= "Dersler",font= "calibri 18")
drs_kod_1 = Label(frame_ders,text= "Ders Kodu:",anchor= E,width= 10)
drs_kod_2 = Entry(frame_ders)
drs_ad_1 = Label(frame_ders,text= "Ders Adı:",anchor= E,width= 10)
drs_ad_2 = Entry(frame_ders)
ekle_2 = Button(frame_ders,text= "Ekle", command= lambda:ekle(2))
list_drs = Listbox(frame_ders,selectmode= MULTIPLE)
sil_2 = Button(frame_ders,text= "Seçili olanları sil", command= lambda:sil(2))

baslik_2.grid(row= 0,column= 0,columnspan= 2)
drs_kod_1.grid(row= 1,column= 0)
drs_ad_1.grid(row= 2,column= 0)
drs_kod_2.grid(row= 1,column= 1)
drs_ad_2.grid(row= 2,column= 1)
ekle_2.grid(row=3,column= 0,columnspan= 2)
list_drs.grid(row= 4,column= 1)
sil_2.grid(row= 5,column= 0,columnspan= 2)



baslik_3 = Label(frame_not,text= "Notlar",font= "calibri 18")
vize_n_1 = Label(frame_not,text= "Vize Notu:",anchor = E,width= 11)
vize_n_2 = Entry(frame_not)
final_n_1 = Label(frame_not,text= "Final Notu:",anchor= E,width= 11)
final_n_2 = Entry(frame_not)
ekle_3 = Button(frame_not,text= "Ekle", command= lambda:ekle(3))
list_not = Listbox(frame_not,selectmode= MULTIPLE)
sil_3 = Button(frame_not,text= "Seçili olanları sil",  command= lambda:sil(3))

baslik_3.grid(row= 0,column= 0,columnspan= 2)
vize_n_1.grid(row= 1,column= 0)
vize_n_2.grid(row= 1,column= 1)
final_n_1.grid(row=2,column= 0)
final_n_2.grid(row= 2,column= 1)
ekle_3.grid(row= 3,column= 0,columnspan= 2)
list_not.grid(row= 4,column= 1)
sil_3.grid(row= 5, column= 0, columnspan= 2)



pen.mainloop()