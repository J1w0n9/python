#1번
import random
import time
wlist = ["cat", "dog", "fog", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
print('[타자게임]준비되면 엔터!')
input()
start = time.time()

com=random.choice(wlist)
n=1
while n <= 5:
    print(com)
    player=input()
    if com == player:
        print("통과!")
        n+=1
        com=random.choice(wlist)
    else:
        print("오타 다시 도전!")