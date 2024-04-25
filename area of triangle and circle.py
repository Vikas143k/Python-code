#Python Program to Calculate the Area and Perimeter of Triangle and Circle.
import math


def area_triangle(x, y, z, l):
    area=0.5*x*y*math.sin(z)
    perimeter=x+y+l
    print(f"Area of triangle is {round(area,2)}metre square")
    print(f"perimeter of triangle is {round(perimeter,2)}metre ")


def area_circle(r):
    area=(math.pi)*(r**2)
    perimeter=2*math.pi*r
    print(f"Area of circle is {round(area)}metre square")
    print(f"perimeter of circle is {round(perimeter)}metre ")

while True:
    print("Pls choose the Option:-")
    print("    1.area and perimeter of circle")
    print("    2.area and perimeter of triangle")
    print("    3.area and perimeter of both")
    print("    4.exit")
    n = int(input(">>"))
    if n == 1:
        radius=int(input("enter the radius in metres "))
        area_circle(radius)

    elif n==2:
        a=int(input("Enter the length of a in metres "))
        b=int(input("Enter the length of b in metres "))
        rt=int(input("Enter the length of c in metres "))
        c=int(input("Enter the angle c in degree"))
        d=c*(math.pi/180)
        area_triangle(a, b, d, rt)
    elif n==3:
        print("-----------FOR CIRCLE-----------")
        radius = int(input("enter the radius in metres "))
        area_circle(radius)
        print("-----------FOR TRIANGLE-----------")
        a = int(input("Enter the length of the a in metres "))
        b = int(input("Enter the length of b in metres "))
        c = int(input("Enter the length of c in metres "))
        d = int(input("Enter the angle c in degree "))
        e=d*(math.pi/180)
        area_triangle(a, b,e,c)
    elif n==4:
        print("Thankyou:)")
        break
    else:
        print("pls choose the correct option")



