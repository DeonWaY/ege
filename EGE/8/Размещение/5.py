from itertools import *
k=0
for x in product('ЛЕТО', repeat=4):
    s=''.join(x)
    if s.count('Е')>=1:
        k+=1
print(k)