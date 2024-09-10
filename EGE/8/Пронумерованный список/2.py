#5-буквенные слова из АОУ в алфавитном порядке, укажите номер слова УАУАУ
from itertools import *
k=0
for x in product(sorted('АОУ'), repeat=5):
    s=''.join(x)
    k+=1
    if s=='УАУАУ':
        print(k,s)