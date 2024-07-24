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
 
C=[]
for row in A:
    c=min(row)
    C.append(c)
print("Массив с минимальными элементами каждой строки матрицы А:")
for elem in C:
    print(f"{elem:4d}", end=' ')
print()
print()

B = []
for i in range (n):
    for j in range (n):
        if i+j >= n:
            B.append(A[i][j])
print("Массив B, содержащий элементы матрицы A, расположенные ниже побочной диагонали:")
for elem in B:
    print(f"{elem:4d}", end=' ')
print()
 
C1=0
for i in range (n):
    C1+=A[i][i]
print("Сумма элементов главной диагонали матрицы А (C1):", C1)
 
num=len(B)
M=[]
for i in range (num):
    for k in range (num-1):
        if B[k]<B[k+1]:
            B[k],B[k+1]=B[k+1],B[k]
M.extend(B)
print("Массив M с упорядоченными по убыванию числами массива B:", M)
