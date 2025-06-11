#1번
id = "ilovepython"
s = input("아이디를 입력하시오: ")
if id == s:
    print("환영합니다.")
else:
    print("아이디를 찾을 수 없습니다.")
#2번
id = "ilovepython"
pw = 123456
s = input("아이디를 입력하시오: ")
p = int(input("비밀번호를 입력하시오: "))
if id == s and pw == p:
    print("환영합니다.")
elif id != s and pw == p:
    print("아이디를 찾을 수 없습니다.")
else:
    print("아이디와 비밀번호가 일치하지 않습니다.")
#3번
id = "ilovepython"
pw = 123456
aid="admin"
apw= 111111
s = input("아이디를 입력하시오: ")
p = int(input("비밀번호를 입력하시오: "))
if id == s and pw == p:
    print("환영합니다.")
elif id != s and pw == p:
    print("아이디를 찾을 수 없습니다.")
elif id == aid and p == apw:
    print("관리자가 로그인하였습니다.")
else:
    print("아이디와 비밀번호가 일치하지 않습니다.")
#4번
y = int(input("연도를 입력해 주세요."))
if y%400==0 or (y%4==0 and y%100 != 0):
    print(y, "은/는 윤년입니다.")
else:
    print(y, "은/는 윤년이 아닙니다.")