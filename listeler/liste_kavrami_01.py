def main ():

    print("Lütfen 5 adet sayı giriniz. Bunların ortalaması alınacaktır : ")
    n1 = float(input("Birinci sayi : "))
    n2 = float(input("İkinci sayi : "))
    n3 = float(input("Üçüncü sayi : "))
    n4 = float(input("Dördüncü sayi : "))
    n5 = float(input("Beşinci sayi : "))
    print("Girdiğiniz sayilar : ",n1,n2,n3,n4,n5,"Toplamları = ",(n1+n2+n3+n4+n5),sep="_")
    print("Girdiğiniz sayıların ortalaması = ",(n1+n2+n3+n4+n5)/5)

main()