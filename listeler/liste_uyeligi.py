liste = list(range(0,21,2))

for i in range (0,22):
    if i in liste:
        print(i,"elemanı",liste,"listesinin bir üyesidir")
    if i not in liste:
        print(i,"elemanı",liste,"listesinin bir üyesi değildir")