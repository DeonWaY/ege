from itertools import *
k=0
for x in permutations("КОЛУН", 5): #5 - это количество букв в слове
    s = ''.join(x)
    s = s.replace("Л","К").replace('Н','К').replace('У','О')
    if 'ОО' not in s and 'КК' not in s:
        k+=1
print(k)