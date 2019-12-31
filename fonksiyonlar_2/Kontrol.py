from math import sqrt

def Asalkontrol(n):

    bolen = 2
    kok = sqrt(n)

    while bolen <= kok:
        if n % bolen == 0:
            return False
        bolen+=1
    return True


#print(Asalkontrol(12))