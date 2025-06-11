#1
a = [7, 6, 5, 4]
b = [1, 2, 3]
print(a+b)
print(a+(b*2))
print(b[:2]+(a[:2]*3))

#2
a = [1, 2, 3, 4, 5]
if str(a) in "1":
    print("1이 존재합니다.")
else:
    print("1이 존재하지 않습니다.")

#3
a = [1, 2, 3, 4, 5]
if str(a) not in "0":
    print("0이 존재하지 않습니다.")
else:
    print("0이 존재합니다.")

#4
import random
alist = []
num = random.randint(1, 100)
i = 1
while i <= 5:
    num = random.randint(1, 100)
    alist.append(num)
    i+=1
if str(alist) in "50":
    print("50이 존재합니다.")
else:
    print("50이 존재하지 않습니다.")
print(f"리스트 숫자 => {alist}")