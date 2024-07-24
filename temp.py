from math import *
x,y,z=2.735,3.823,0.666
a=exp(abs(x-y))+abs(sqrt(x)+y)**(x+y)    
b=(1+cos(y-2))/(x**3+pow(sin(z),2))                                
print("a =",a)
print("b =",b)
print("Исходные данные: x = {}, y = {}, z = {}\na = {:6.2F}\nb ={:5.2F}".format(x,y,z,a,b))
 
#вариант 2
 
x1=int(input("Введите координату x1: "))
y1=int(input("Введите координату y1: "))
x2=int(input("Введите координату x2: "))
y2=int(input("Введите координату y2: "))
x3=int(input("Введите координату x3: "))
y3=int(input("Введите координату y3: "))

a=sqrt((x2-x1)**2+(y2-y1)**2)
b=sqrt((x3-x2)**2+(y3-y2)**2)
c=sqrt((x1-x3)**2+(y1-y3)**2)

P=int(a+b+c)
p=(a+b+c)/2
S=int(sqrt(p*(p-a)*(p-b)*(p-c)))


print("Периметр треугольника равен ",P)
print("Площадь треугольника равна ",S)



