#1번
num=int(input("정수 입력> "))
if num<0:
    print("음수입니다.")
else:
    if num==0:
        print("0입니다.")
    else:
        print("양수입니다")

#2번
num1=int(input("첫번째 수 입력> "))
num2=int(input("두번째 수 입력> "))
if num1>num2:
    print("첫번쨰 수가 더 큽니다.")
else:
    print("두번째 수가 더 큽니다.")

#3번
money=int(input("돈 입력> "))
if money>=5000:
    print("택시를 타고 가라")
else:
    if money>=2000:
     print("버스를 타고 가라")
    else:
        print("걸어 가라")

#4번
y = int(input("연소득 입력> "))
w = int(input("재직기간 입력>"))
if y >= 40000000 and w >= 2:
    print("대출자격 있음")
else:
    if y>=40000000 and w <= 2:
        print("재직기간 2년 이상 필요")
    else:
        print("연소득 4000만원 이상 필요")