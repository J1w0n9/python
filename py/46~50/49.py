#1번
bts = ["정국", "뷔", "지민", "슈가", "진", "RM", "제이홉"]
i = 0
while i < len(bts):
    print(bts[i])
    i+=1
#2번
dan = int(input("원하는 단은:"))
d = 1
while d <= 9:
    print(f'{dan}*{d}= {dan*d}')
    d+=1
#3번
import random
com = random.randint(1,100)
while 1:
    player = int(input("1부터 100사이의 숫자야, 맞춰봐> "))
    if player < com:
        print("UP")
    elif player > com:
        print("DOWN")
    elif player==com:
        print("정답!")
        break

