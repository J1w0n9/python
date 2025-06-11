#1번
sum = 0
a = 1
while a <= 10:
    sum+=a
    a+=1
print(sum)
#2번
sum = 0
a = 1
n = int(input("N값 입력:"))
while a <= n:
    sum+=a
    a+=1
print(sum)
#3번
a=1
while a <= 100:
    if a%3==0:
        print("짝", end=" ")
    else:
        print(a, end=" ")
    a += 1
#4번
alist = [1, 2, 1, 2]
while alist.count(2) >= 0:
    alist.remove()
print(alist)