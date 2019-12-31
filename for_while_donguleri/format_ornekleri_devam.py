kelime = input("Bir cümle giriniz : ")

sesliharfsayisi = 0
bosluk = 0

for harf in kelime:
    if  harf =="A" or harf=="a" or harf=="E" or harf=="e"  \
    or  harf =="O" or harf=="o" or harf=="Ö" or harf=="ö"  \
    or  harf =="I" or harf=="ı" or harf=="İ" or harf=="İ"  \
    or  harf =="U" or harf=="u" or harf=="Ü" or harf=="ü"  :
        sesliharfsayisi+=1

print("sesli harf sayınız {} tanedir.".format(sesliharfsayisi))

for harf in kelime:
    if harf == " " :
        bosluk+=1
print("Cümlenizde {} tane boşluk bulunmaktadır.".format(bosluk))
print("Cümleniz {} kelimeden oluşmaktadır.".format(bosluk+1))
