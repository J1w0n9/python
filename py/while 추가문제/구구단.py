import random
print("구구단을 외자! 구구단을 외자!")
while 1:
    a = random.randint(1,9)
    b = random.randint(1,9)
    answer = int(input(f'{a}*{b}?'))
    if (a*b)==answer:
        print("정답입니다!")
    else:
        print("틀렸습니다!")