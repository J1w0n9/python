#1
friend = []
name = input('친구 이름 입력: ')
friend.append(name)
name = input('친구 이름 입력: ')
friend.append(name)
name = input('친구 이름 입력: ')
friend.append(name)
name = input('친구 이름 입력: ')
friend.append(name)
name = input('친구 이름 입력: ')
friend.append(name)
print(friend)

#2
menus = []
menu = input('메뉴를 입력하세요 > ')
menus.append(menu)
menu = input('메뉴를 입력하세요 > ')
menus.append(menu)
menu = input('메뉴를 입력하세요 > ')
menus.append(menu)
menu = input('메뉴를 입력하세요 > ')
menus.append(menu)
print(menus)

#2-1
del menus[3]
menus.append("감자튀김")
print(f'변경 => {menus}')

#2-2
delmenu = menus.pop(2)
print(f'삭제 => {menus}')
print(f'{delmenu} 메뉴가 삭제 되었습니다.')

#3 잘 모르겠다.
import random
number = [10, 20, 33, 40, 55, 60, 77, 80, 90, 100]
while 1:
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    answer = int(input(f"{number[i]}+{number[j]} = ?"))
    if answer == number[i] + number[j]:
        print("정답입니다.")
    else:
        print("틀렸습니다.")