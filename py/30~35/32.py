#1번
num = int(input("정수 입력> "))
if num<0:
    print("음수입니다.")
elif num==0:
    print("0입니다.")
else:
    print("양수입니다.")

#2번
money=int(input("돈 입력> "))
if money>=5000:
    print("택시를 타고 가라")
elif money>=2000:
    print("버스를 타고 가라")
else:
    print("걸어 가라")

#3번
score=int(input("당신의 점수는 몇점인가요?"))
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("F")

#4번
age=int(input("나이를 입력해 주세요> "))
if age<=7:
    print("미취학")
elif age<=13:
    print("초등학생")
elif age<=16:
    print("중학생")
elif age<=19:
    print("고등학생")
else:
    print("성인")