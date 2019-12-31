kelime = input("Bir kelime giriniz :")
karakter = input("Bir karakter giriniz :")

print(kelime.rjust(20,karakter))
print(kelime.ljust(20,karakter))
print(kelime.center(20,karakter))
print(kelime.count("a"))
print(kelime.find("a"))
print(kelime.__getitem__(2))
print(len(kelime))
for i in range (len(kelime)):
    print("[",kelime[i],"]", sep="", end=" ")
print()
for ch in kelime:
    print("<",ch,">",sep="",end=" ")
print()
