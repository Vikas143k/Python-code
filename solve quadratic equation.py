#Python Program to Solve Quadratic Equation
import math
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
e=(b**2)-(4*a*c)
if e>0 or e==0:
    D=math.sqrt(e)
    value_1=(-(b)+D)/(2*a)
    value_2=(-(b)-D)/(2*a)
    print(f"the roots are {value_1}, {value_2}")
else:
    print("the equation has no real roots")