# Лабораторная работа "Программная реализация обработки одномерных массивов"
# Задача 1: Образовать два массива Х и Y, состоящие из 12 вещественных чисел.
import math
import random
N=12
X=[random.uniform(-50,50) for j in range (N)]
formatted_X = ", ".join(f"{x:.1f}" for x in X)
print(f"Массив X = [{formatted_X}]")
 
Y=[random.uniform(-50,50) for j in range (N)]
formatted_Y = ", ".join(f"{y:.1f}" for y in Y)
print(f"Массив Y = [{formatted_Y}]")
 
# Задача 2: Образовать массив Z по правилу Z[k]=X[k]+m*Y[k]. При этом, m=k при sin(k) <= 0.3 и m=-k при sin(k) > 0.3
Z=[0]*N
for j in range(N):
 if math.sin(j) <= 0.3: m=j
 else: m=-j
 Z[j]=X[j]+m*Y[j]
formatted_Z= ", ".join(f"{z:.1f}" for z in Z)
print(f"Массив Z = [{formatted_Z}]")
 
# Задача 3: Найти среднее арифметическое значение элементов массива Z; k = 1, 12.
sr=0
sum=0
for i in range (N):
    sum=sum+Z[i]
sr=sum/N
print("Среднее арифметическое элементов Z={0:.2F}".format(sr))
 
# Задача 4: Найти произведение всех элементов массива X, удовлетворяющих условию
proizv=1
for x in X:
    if -3.5<x<3.5:
        proizv = proizv*x
print("Произведение элементов массива X удовлетворяющих условию -3.5 < x < 3.5: {0:.1F}".format(proizv))

# Задача 5: Вычислить суммы отдельно отрицательных и положительных элементов массива Z.
pos_sum=0
neg_sum=0
for z in Z:
    if z<0:
        neg_sum=neg_sum+z
    elif z>0:
        pos_sum=pos_sum+z
print("Сумма всех отрицательных чисел массива Z = {0:.2F}".format(neg_sum))
print("Сумма всех положительных чисел массива Z = {0:.2F}".format(pos_sum))
 
# Задача 6:  Упорядочить массив Y по убыванию значений его элементов.
for j in range (N):
    for k in range (N-1):
        if Y[k]<Y[k+1]:
            Y[k],Y[k+1]=Y[k+1],Y[k]
formatted_Y=", ".join(f"{y:.1f}" for y in Y)
print(f"Отсортированный список Y по убыванию: [{formatted_Y}]")

# Лабораторная работа "Программная реализация обработки двумерных массивов"
# Задача 1: Сформировать матрицу А(18,18) случайными целыми числами в диапазоне [-100,100].
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
 
# Задача 2: Найти минимальные элементы каждой строки матрицы А, образовав массив С.
C=[min(row) for row in A]
print("Массив C, содержащий минимальные элементы каждой строки матрицы A:")
for elem in C:
    print(f"{elem:4d}", end=' ')
print()
 
# Задача 3: Переписать в массив В все элементы матрицы А, расположенные ниже побочной диагонали.
B = []
for i in range(n):
    for j in range(n - i, n):
        B.append(A[i][j])
print("Массив B, содержащий элементы матрицы A, расположенные ниже побочной диагонали:")
for elem in B:
    print(f"{elem:4d}", end=' ')
print()

# Задача 4: Найти сумму С1 из элементов главной диагонали матрицы А.
C1=0
for i in range (n):
    C1+=A[i][i]
print("Сумма элементов главной диагонали матрицы А (C1):", C1)

# Задача 5: Упорядочить массив В по убыванию, образовав массив М.
num=153
M=[]
for i in range (num):
    for k in range (num-1):
        if B[k]<B[k+1]:
            B[k],B[k+1]=B[k+1],B[k]
M.extend(B)
print("Массив M с упорядоченными по убыванию числами массива B:", M)
