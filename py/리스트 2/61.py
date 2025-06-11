#1-1
score = [80, 90, 75, 25, 50]
for i in score:
    print(i)
#1-2
for a in range(5):
    print(score[a])
    a+=1
#1-3
for a in range(5):
    print(score[a])
    a+=1

#2-1
print("Knowlegde is power and money".split())
print("Knowlegde is power and money".split('is'))
#2-2
a = "상상할 수 없는 꿈을 꾸고 있다면, 상상할 수 없는 노력을 해라."
print(a.split())
print(a.split(","))
#2-2
week = input().split()
print(week)