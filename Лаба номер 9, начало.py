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

#15
d=set()
for x in c:
    if x in Fib:
        d.add(x)
print(len(d))

names={'Вася', 'Володя', 'Ира»', 'Лида', 'Марина', 'Миша', 'Наташа', 'Олег', 'Оля', 'Света', 'Юля'}
spisok=[{'Вася', 'Володя', 'Ира»'},
        {'Володя', 'Ира»', 'Лида'},
        {'Марина', 'Миша', 'Наташа','Володя'},
        {'Наташа', 'Олег', 'Оля','Володя'},
        {'Олег', 'Оля', 'Света', 'Володя'},
        {'Оля', 'Света', 'Юля'}]
samyi_obshitelnyi=names.intersection(*spisok)
if samyi_obshitelnyi:
    for x in samyi_obshitelnyi:
        print("Самый(-ые) общительный(-ые):", x)
else:
    print("Нет человека, который побывал у всех остальных.")
    
#22
znaki=['.','?',',',',','!','!',':',';',';','!']
new=set()
newpovtor=set()

for p in znaki:
    if p in new:
        newpovtor.add(p)
    else:
        new.add(p)
print("Повторяющиеся символы:", newpovtor)

