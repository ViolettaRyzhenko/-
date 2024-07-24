#15 9 22
#9
c=set(range(1,51,1))
print("Числа от 1 до 50:", *c)

Fib = set()
a, b = 0, 1
n = 15
for i in range(n):
    Fib.add(a)
    temp = a
    a = b
    b = temp + b
print(Fib)

d=set()
for x in c:
    if x in Fib:
        d.add(x)
print(len(d))

