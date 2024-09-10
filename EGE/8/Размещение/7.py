from itertools import *
k=0
for x in product('БЕРКЛИЙ', repeat=4):
    s=''.join(x)
    if s[0]!='Й' and ('И' in s or "Е" in s):
        k+=1
print(k)