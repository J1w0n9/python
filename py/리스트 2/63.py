#1-1
abc = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(abc)
abc = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(abc)
#1-2
abc = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(abc[0])
print(abc[1])
print(abc[2])

print(abc[0][1])
print(abc[1][2])
print(abc[2][2])

#2-1
abc = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for row in abc:
    print(row)
#2-2
abc = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for row in abc:
    print(row[0])
#2-2
abc = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for col in abc:
    print(col, end=" ")
print()