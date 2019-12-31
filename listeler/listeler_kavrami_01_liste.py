def main():

    toplam = 0
    girileceksayiadedi = 5
    print("Lütfen ",girileceksayiadedi,"sayı giriniz")
    for i in range(0,girileceksayiadedi):
        sayi = float(input("Lütfen " + str(i+1)+ ". sayıyı giriniz :"))
        toplam += sayi
    print("Ortalama =", toplam/girileceksayiadedi)

main()