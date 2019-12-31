
def gcd(s1,s2):
    min1= s1 if s1<s2 else s2
    ebop = 1
    for i in range(1,min1):
         if s1%i == 0 and s2%i==0:
             ebop = i
    return ebop

def sayigir():
    return int(input("Lütfen bir sayı giriniz : "))

def main():
    s1 = sayigir()
    s2 = sayigir()
    print("Girdiğiniz ilk sayı ",s1,"Girdiğiniz ikinci sayı ", s2,"En büyük ortak bölen =", gcd(s1,s2))

main()