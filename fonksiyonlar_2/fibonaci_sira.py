def fibonaci(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-2)+fibonaci(n-1)

sira = int(input("Görmek istediğiniz fibonaci sıra numarasını giriniz : "))

print(fibonaci(sira))