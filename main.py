import math
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
D = b*b-4*a*c
if D > 0:
    x = (-b+math.sqrt(D))/(2*a)
    xx = (-b-math.sqrt(D))/(2*a)
    print(f"Два корня х1 = {x} х2 = {xx}")
if D == 0:
    x = -b/(2*a)
    print("Один корень =", x)
if D < 0:
    print("Корней нет ")
