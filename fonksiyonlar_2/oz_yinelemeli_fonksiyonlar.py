def faktoriyel(n):

    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

def main():

    print("5! in değeri", faktoriyel(5)," dir. ")


main()