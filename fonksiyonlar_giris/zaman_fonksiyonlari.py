from time import perf_counter
toplam = 0
basla = perf_counter()
for n in range(1,1000001):
    toplam+=n
gecenzaman = perf_counter() - basla
print("Toplam gecen zaman = ",gecenzaman,"toplam değer =",toplam)