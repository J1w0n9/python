# 1번
carspeed = int(input("현재 속도 입력>"))
if carspeed >= 50:
    print("과속입니다.\n속도를 줄여주세요.")
else:
    print("정상 속도입니다.")

# 2번
import random
a = random.randint(1,9)
b = random.randint(1,9)
answer = int(input(a, '*', b, '는 무엇일까요?'))
if (a*b)==answer:
    print("정답입니다.")
else:
    print("구구단 공부합시다.")
# 3번
import random
print("동전 던지기 게임을 시작합니다.")
coin=random.randint(0,1)
answer=int(input("앞면(0)/뒷면(1)을 입력해 주세요>"))
if coin==answer:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
if coin==0:
    print("앞면입니다.")
else:
    print("뒷면입니다.")
