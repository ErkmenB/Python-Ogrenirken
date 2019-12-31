# 999 girilene kadar girilen pozitif sayıların toplamını alan program
# GİRİLEN NEGATİF SAYILAR İŞLEME ALINMAYACAKTIR

toplam = 0
durum  = False
while not durum:
    deger = int(input("Lütfen pozitif bir tam sayı giriniz (Çıkış için 999) : "))
    if deger < 0:
        print("Negatif değer girildi.",deger,"değeri işleme alınmadı.")
        continue
    if deger !=999:
        print("Eklenen deger",deger,"dir.")
        toplam +=deger
    else:
        durum=(deger==999)
print("Toplam = ",toplam)