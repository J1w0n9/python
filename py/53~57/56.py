#1번
#import turtle
#t = turtle.Turtle()
#for ci in range(1, 7):
    #t.circle(100)
    #t.right(60)
#turtle.done()
#2번
#import turtle
#t = turtle.Turtle()
#for c in range(1, 5):
    #t.forward(100)
    #t.right(90)
#turtle.done()
#3번
#import turtle
#t = turtle.Turtle()
#n = int(input("정수 입력>"))
#for i in range(1, n+1):
    #t.forward(100)
    #t.left(180*(n-2))
#turtle.done()
#4번
#import turtle
#t = turtle.Turtle()
#for n in range(1, 6):
    #t.forward(100)
    #t.right(144)
#turtle.done()
#5번
num = int(input("정수 입력>"))
fa = 1
for f in range(1, num+1):
    fa *=f
print(fa)