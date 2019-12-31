import Kontrol

sayi = int(input("Asal kontrolü için bir sayı giriniz : "))

if Kontrol.Asalkontrol(sayi):
    print(sayi,"Asaldır")

else:
    print(sayi,"Asal değildir.")