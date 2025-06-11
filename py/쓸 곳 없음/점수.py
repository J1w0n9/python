while 1:
    score = int(input("점수를 입력하시오. >"))
    if 100>=score>=80:
        print("합격입니다.")
        break
    elif 80>score>=0:
        print("불합격입니다.")
        break
    else:
        print("다시 입력하세요.")
