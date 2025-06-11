#1-1
scores = [[92, 80, 87],[94, 82, 86],[74, 65, 69],[87, 89, 81]]
m_total = 0
for row in scores:
    m_total = m_total + row[0]
print(m_total)
#1-2
avg = m_total/4
print(f"{(avg) : .2f}")
#1-3
for row in scores:
    s_total = 0
    for col in row:
        s_total += col
    print(s_total)
#1-4
for row in scores:
    s_total = 0
    for col in row:
        s_total = s_total + col
    s_avg = s_total/3
    print(f"{(s_avg) : .2f}")
#1-5
scores = [['김정호', 92, 80, 87],["박문수", 94, 82, 86],["이사부", 74, 65, 69],["장영실", 87, 89, 81]]
for row in scores:
    s_total = 0
    for col in row[1:]:
        s_total = s_total + col
    s_avg = s_total/3
    print(f"{row[0]}{(s_avg) : .2f}")

#2-1
medal = [[6, 4, 10], [38, 32, 19], [26, 14, 17]]
au = ag = cu =0

for i in range(3):
    for j in range(1):
        au+=medal[i][j]
print(f"금: {au}")
for i in range(3):
    for j in range(1,2):
        ag+=medal[i][j]
print(f"은: {ag}")
for i in range(3):
    for j in range(2,3):
        cu+=medal[i][j]
print(f"동: {cu}")
#2-2
medal = [['대한민국', 6, 4, 10], ['중국', 38, 32, 19], ['일본', 26, 14, 17]]
k = c = j = 0
for row in medal:
    total = 0
    for col in row[1:]:
        total = total + col
    print(row[0], total)


#3-1
daylist = [[0,1,0,0,1], [0,0,1,0,0], [0,1,0,1,0], [0,0,0,1,0], [0,0,0,0,0]]
count = 0
for row in range(5):
    for col in range(5):
        if daylist[row][col] == 1:
            count+=daylist[row][col]
print(count)
#3-2
count = 0
for row in range(5):
    if daylist[row][1] == 1:
        count+=daylist[row][1]
print(count)
#심화
n = int(input("학생수 입력"))
daylist = []
for i in range(n):
    att = input().split()
    daylist.append(att)
for row in range(5):
    for col in range(n):
        if daylist[row][col] == "1":
            count+=1