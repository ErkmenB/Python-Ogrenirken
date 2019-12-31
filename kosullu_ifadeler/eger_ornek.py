print("Lütfen bölme işlemi için iki sayı giriniz...")

bolunen = int(input("Bolunecek olan sayıyı giriniz :"))
bolen = int(input("Bolen sayıyı giriniz : "))

if bolen!=0:
    print(bolunen,"/",bolen,"=",bolunen/bolen)
else :
    print("Bölen sayı 0 olamaz")