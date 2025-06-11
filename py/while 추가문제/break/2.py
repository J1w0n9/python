import random
print("구구단을 외자! 구구단을 외자!")
while 1:
    a = random.randint(1,9)
    b = random.randint(1,9)
    answer = int(input(f'{a}*{b}?'))
    if (a*b)!=answer:
        print(f"땡! 정답은 {a*b}")
        break