def Listeleme(dosyaadi):
    with open(dosyaadi) as f:
        for satir in f :
            print(int(satir))
def Kaydet(dosyaadi):
    with open(dosyaadi,"w") as f:
        sayi = 0
        while sayi != 999:
            sayi = int(input(" Lütfen bir sayı giriniz. (Çıkış için 999) : "))
            if sayi != 999:
                f.write(str(sayi)+ "\n")
            else:
                break

def main():
    kontrol = False
    while not kontrol:
        secim = input("K)aydet L)isteleme S)onlandır : ")
        if secim =="K" or secim == "k":
            Kaydet(input("Kayıt edilecek dosya adını giriniz : "))
        elif secim == "L" or secim =="l":
            Listeleme(input("Kayıtların okunacağı dosya adını giriniz :"))
        elif secim == "S" or secim == "s":
            kontrol = True

main()

