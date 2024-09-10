# 5-букв слова из КОМПЬЮТЕР, сколько слов с нечетным номером , которые не начинаются с Ь и содержит 2 буквы К
from itertools import *
k=0
l=0
for x in product(sorted('КОМПЬЮТЕР'), repeat=5):
    s=''.join(x)
    k+=1
    if k%2!=0 and s[0]!='Ь' and s.count("К")==2:
        l+=1
        print(k,s)
print(l)