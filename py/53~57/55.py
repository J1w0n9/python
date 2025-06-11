#1번
dan = int(input("원하는 단은:"))
for d in range(1, 10):
    print(f'{dan}*{d}= {dan*d}')
#2번
sum = 0
for n in range(1, 101):
    sum+=n
print(sum)
#3번
count = 0
s = input("문자열을 입력하시오.")
for a in s:
    if a == "a":
        count+=1
print(count)
#4번
n1 = int(input("숫자 입력:"))
print(n1)
for z in range(0, n1+1):
    print(z, end=" ")
#5번
num = int(input("* 출력 횟수 >"))
print(num)
for c in num:
    print("*"*c)
#6번
array = [273, 74, 103, 57, 52]
o = 0
for i in array:
    print(o, i)
    o+=1