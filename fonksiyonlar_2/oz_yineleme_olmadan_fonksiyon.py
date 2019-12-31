def faktoriyel(n):
    sonuc = 1
    while n:
        sonuc*= n
        n-=1
    return sonuc

def main():
    print("5! = ",faktoriyel(5),"dir.")

main()