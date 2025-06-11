#1번
sum = 0
for i in range(1, 101):
    sum+=i
    if sum >= 1000:
        break
print(i)
#2번
sum = 0
for i in range(1, 101):
    if i%3==0:
        continue
    sum=sum+i
print(sum)
#3번
mult = 1
for a in range(1, 100):
    if a%2==0:
        continue
    print(f'{mult} * {a} = {mult*a}')
    mult = mult*a
    if mult >= 100:
        break
