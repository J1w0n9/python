#1번
u = str(input())
if u == "0100" or u == "0001" or u == "0010" or u == "1000":
    print("도")
elif u == "1100" or u == "0011" or u == "0110" or u == "1010" or u == "0101":
    print("개")
elif u == "0111" or u == "1011" or u == "1110" or u == "1101":
    print("걸")
elif u == "1111":
    print("윷")
elif u == "0000":
    print("모")
else:
    print("다시 입력하시오")

#2번
import random
l = random.randint(00,99)
answer = str(input('복권번호를 입력하시오(00~99)'))
l=str(l)
if answer[1]==l[1] or answer[0]==l[0]:
    print("상금 50만원!")
elif l==answer:
    print("상금 100만원!!")
else:
    print("상금이 없습니다.")

#3번
num = int(input("직선 입력> "))
num1 = int(input("직선 입력> "))
num2 = int(input("빗변 입력> "))
if num + num1 > num2:
    print("삼각형 가능")
elif num + num2 > num1:
    print("삼각형 가능")
elif num1 + num2 > num:
    print("삼각형 가능")
else:
    print("삼각형 불가능")

