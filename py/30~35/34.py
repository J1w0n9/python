#1번
t = float(input("현재 온도를 입력하시오> "))
if t >= 25:
    print("반바지를 입으세요.")
else:
    print("긴바지를 입으세요.")

#2번
num = int(input("정수 입력> "))
num1 = int(input("정수 입력> "))
num2 = int(input("정수 입력> "))
if num > num1 > num2:
    print("가장 큰 수는", num)
if num < num1 > num2:
    print("가장 큰 수는", num1)
else:
    print("가장 큰 수는", num2)

#3번
num = int(input("정수 입력> "))
if num%2==0 and num%3==0:
    print("2와 3의 배수입니다.")
elif num%2!=0 and num%3==0:
    print("2의 배수아니고 3의 배수입니다.")
elif num%2==0 and num%3!=0:
    print("2의 배수이고 3의 배수가 아닙니다.")
else:
   print("2와 3의 배수가 아닙니다.")

#4번
n = input("주민등록번호 입력")
if n[7] == "1":
 print(f"19{n[0:2]}년에 태어난 남자 입니다.")
elif n[7] == "2":
 print(f"19{n[0:2]}년에 태어난 여자 입니다.")
elif n[7] == "3":
 print(f"20{n[0:2]}년에 태어난 남자 입니다.")
elif n[7] == "4":
 print(f"20{n[0:2]}년에 태어난 여자 입니다.")
else:
   print("다시 입력하세요")