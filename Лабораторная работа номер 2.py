from math import sqrt
x1,x2,x3=map(int,input('ВВедите значения координат x1,x2,x3=').split())
y1,y2,y3=map(int,input('ВВедите значения координат y1,y2,y3=').split())
a=sqrt((x2-x1)**2+(y2-y1)**2)
b=sqrt((x3-x2)**2+(y3-y2)**2)
c=sqrt((x1-x3)**2+(y1-y3)**2)
P=int(a+b+c)
p=(a+b+c)/2
S=int(sqrt(p*(p-a)*(p-b)*(p-c)))
print("Периметр треугольника равен = {},\nПлощадь треугольника равна = {}".format(P,S))