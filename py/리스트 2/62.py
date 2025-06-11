#1
email = input().split('@')
print(email[0])
#2
food = []
a = 0
fn = int(input("좋아하는 음식의 개수: "))
while a <= fn-1:
    ff = input().split()
    food.append(ff)
    a+=1
for i in food:
    print(i)

#3
total = 0
score = input().split()
score.append(score)
score[0] = int(score[0])
score[1] = int(score[1])
score[2] = int(score[2])
total += score[0]
total += score[1]
total += score[2]
print(f"{(total/3) : .2f}")

#좀더 알아보기
#1
alist = ["90", "80", "10"]
alist = list(map(int, alist))
print(alist)
#2
num = input().split()
t = 0
num = list(map(int, num))
for i in range(len(num)):
    if num[i]%2 == 0:
        t+=1
print(t)