from itertools import *
k=0
for i in product("КРСЛ", "КРЕСЛО", "КРЕСЛО", "ЕО"):
    k+=1
print(k)