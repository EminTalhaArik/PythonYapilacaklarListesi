# -*- coding: utf-8 -*-

devamEdiyorMu = True    

def ListeyiGöster(): # Listedeki Elemanlar Gösterildi.
    print("Yapılacaklar Listesi Açıldı.")
    print("------------------")
    for eleman in liste:
        print(eleman)
        
    print("-------------------")
    print("Liste Başarıyla Görüntülendi.")
    print(" ")


def GorevEkle(): # Listeye Yeni Bir Eleman Eklendi.
    
    deger = str(input("Lütfen Bir Görev Giriniz : "))
    liste.append(deger)
    print("Görev Başarıyla Eklendi.")
    print(" ")


def GorevKaldir(): # Listeden Girilen Değerdeki Görev Kaldırıldı.
      
    silinecekDeger = int(input(" Lütfen Kaldırılacak Öğenin Sırasını Giriniz : "))
    
    liste.pop(silinecekDeger -1 )
    print("Görev Başarıyla Kaldırıldı.")
    print(" ")
    
def ListeyiTemizle(): # Listedeki Bütün Görevler Temizlendi.
    liste.clear()
    print("Liste Temizlendi.")
    print(" ")


print("----------------Yapılacaklar Listesi Programımıza Hoşgeldiniz.--------------")


liste = []


while devamEdiyorMu == True: 
    
    print("1 - Listeyi Görüntüle , 2 - Görev Ekle , 3 - Görev Kaldır , 4 - Listeyi Temizle , 0 - Çıkış Yap")
    
    secenek = int(input("Lütfen Bir İşlem Seçiniz : "))

    if secenek == 1:
        ListeyiGöster()
        
    elif secenek == 2:
        GorevEkle()
 
    elif secenek == 3:
        GorevKaldir()
        
    elif secenek == 4:
        ListeyiTemizle()
        
    elif secenek == 0:
        devamEdiyorMu = False 
        print("Çıkış Yapıldı.")
        
















