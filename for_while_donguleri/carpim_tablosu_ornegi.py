sayi = int(input("Lütfen tablo için bir ölçü giriniz : "))

for satir in range(1, sayi +1) :
    for sutun in range(1, sayi + 1):
        deger = satir*sutun
        print("{0:3}".format(deger),end=" ")
    print()