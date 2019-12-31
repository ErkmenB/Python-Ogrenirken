faktoriyel = 1
sayac = 1
sayi=int(input("Faktoriyel hesabı için bir sayı giriniz : "))
while sayac <= sayi:
    faktoriyel*=sayac
    sayac+=1
print(sayi,"sayısının faktoriyeli : ", faktoriyel)