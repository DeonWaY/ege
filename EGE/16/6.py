def f(n):
    if n<=15: return 2*n**2+4*n+3
    if n>15 and n%3 == 0: return f(n-1)+n**2+3
    if n>15 and n%3!=0: return f(n-2)+n-6
k=0
for n in range(1,1001):
    if all(int(d)%2!=0 for d in str(f(n))): #делаеются списки, преобраз в инт и проверяються на нечётность
        k+=1
print(k)
#и выводиться сколько нечетных чисел
