from random import randint
n = 18
A = [[0] * n for i in range(n)]
print("Исходный массив A")
for i in range(n):
 for j in range(n):
    A[i][j]=randint(-100, 100)
for i in range(n):
 for j in range(n):
    print("%4d" % A[i][j], end = '')
 print()
print()
 
C=[min(row) for row in A]
print("Массив C, содержащий минимальные элементы каждой строки матрицы A:")
for elem in C:
    print(f"{elem:4d}", end=' ')
print()


D=[]
for row in A:
    c=min(row)
    D.append(c)
print("массив с минимальными элементами")
for elem in D:
    print(f"{elem:4d}", end=' ')
print()