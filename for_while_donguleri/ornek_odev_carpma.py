sayi = 1
carpim = 1
print("Bir sayı giriniz. Girilen sayı 0 dan farklı olduğu sürece çarpılacaktır : ")

while sayi!=0:
   sayi=int(input())
   if sayi==0:
       break
   else:
       carpim= carpim*sayi
print("Sonuç = ",carpim)