a =1231231233213
# print(a%10)
# print(a//10)
count = 0
while a>0:
    if a%10 == 3:
        count +=1
    a = a // 10
print(count)