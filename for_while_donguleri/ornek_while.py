sayac = 0
giris = "Y"
while giris !="n" and giris !="N":
    print(sayac)
    giris=input("Devam etmek için Y - Çıkmak için N ye basınız. ")
    if giris =="Y" or giris=="y":
        sayac+=1
    elif giris !="N" and giris !="n":
        print(""+giris+"    Değeri doğru değildir")