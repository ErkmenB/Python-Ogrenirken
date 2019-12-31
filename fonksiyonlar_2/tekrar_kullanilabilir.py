from Kontrol import Asalkontrol

sayi = int(input("Asal kontrolü için bir sayı giriniz : "))

if Asalkontrol(sayi):
    print(sayi,"Asaldır.")
else:
    print(sayi,"Asal değildir.")