from itertools import *
k=0
for x in permutations("КАЛИЙ", 5): #5 - это количество букв в слове
    s=''.join(x)
    if s[0]!='Й' and 'ИА' not in s:
        k+=1
print(k)
