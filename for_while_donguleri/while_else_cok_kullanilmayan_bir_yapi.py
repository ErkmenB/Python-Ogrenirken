# Girilen 5 sayının ortalamasını alan program
# Negatif sayı girildiğinde program sonlandırılır

sayac=0
toplam=0

print("Lütfen 5 adet sayı giriniz.")
while sayac < 5:
    sayi=float(input("Sayı giriniz : "))
    if sayi < 0:
        print("Negatif sayılar kabul edilmemektedir. Programdan çıkılıyor.")
        break
    sayac+=1
    toplam+=sayi
else:
    print("Ortalama = ",toplam/sayac)