kelime = input("Bir metin giriniz (Çıkış için X / x ) : ")
sesliharf = 0
for harf in kelime :
            if harf == "A" or harf == "a" or harf == "E" or harf == "e" \
            or harf == "O" or harf == "o" or harf == "Ö" or harf == "ö" \
            or harf == "I" or harf == "ı" or harf == "İ" or harf == "i" \
            or harf == "U" or harf == "u" or harf == "Ü" or harf == "ü":
               print(harf,",",end=" ",sep=" ")
               sesliharf=sesliharf+1
            elif harf =="x" or harf=="X":
               break
print("(",sesliharf,"adet sesli harf vardır.",sep="")
