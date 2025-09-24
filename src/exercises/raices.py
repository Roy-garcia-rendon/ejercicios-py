import math
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

discriminate =(b**2) - 4*a*c
if discriminate > 0:
    x1 = -b + math.sqrt(discriminate)/(2*a)
    x2 = -b - math.sqrt(discriminate)/(2 * a)
    print(f"x1={round(x1, 2)}\nx2={round(x2, 2)}")
elif discriminate == 0:
    x = -b/(2*a)
    print(f"x={x}")
else:
    print(f"<< No tiene solución >>")