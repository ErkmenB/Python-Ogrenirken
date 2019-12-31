deger = int(input("0 ile 5 aralığında bir değer giriniz : "))

if deger < 0 :
    print("Çok küçük bir değer girdiniz.")

else :
    if deger == 0 :
        print("Girdiğiniz değer sıfır")
    else:
     if deger == 1 :
        print("girdiğiniz değer Bir")
     else :
        if deger == 2 :
            print("Girdiğiniz değer iki")
        else:
            if deger == 3 :
                print("Girdiğiniz değer üç")
            else:
                if deger == 4 :
                    print("Girdiğiniz değer dört")
                else:
                    if deger == 5 :
                        print("girdiğiniz değer beş ")
                    else:
                        print("Çok büyük bir değer girdiniz")