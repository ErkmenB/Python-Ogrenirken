# kullanıcıdan aldığımız sayının karekökünü bulacağız

from math import sqrt
from random import random

sayi = int(random()*10)

kok = sqrt(sayi)
print(sayi,"sayısının karekökü = ",kok,"tür.")
