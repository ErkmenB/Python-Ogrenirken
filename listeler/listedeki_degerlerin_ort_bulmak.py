def main():

    toplam = 0.0
    GirilecekSayiAdedi = 5
    sayilar = []

    print("Lütfen ",GirilecekSayiAdedi,"adet sayı giriniz : ")
    for i in range (0,GirilecekSayiAdedi):
        sayi = float(input(str(i+1) + ". sayıyı giriniz "))
        sayilar += [sayi]
        toplam += sayi

    for sayi in sayilar:
        print(end="Girilen sayılar :")
        print(sayi,end=" ")
        print()
    print("Ortalama = ", toplam/GirilecekSayiAdedi)

main()