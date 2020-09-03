import math

print("solve y = ax^2 + bx + c when y = 0")
a = float(input("Input a for ax^2 "))
print(a)
b = float(input("Input b for bx "))
print(b)
c = float(input("Input c "))
print(c)
print(" ")

d = b**2-4*a*c 
print("d = b**2-4*a*c ")
print(d)
print(" ")

if d < 0:
    print("no solution")
elif d == 0:
    print("math.sqrt(d)")
    print(math.sqrt(d))
    print(" ")
    x = (-b+math.sqrt(d))/(2*a)
    print("-b+math.sqrt(d)")
    print(-b+math.sqrt(d))
    print(" ")
    print("one solution")
    print(x)
    xmid=x
    y= (a*xmid**2)+(b*xmid)+(c)
    print("min or max point is " + str(xmid) + "," + str(y))

else:
    print("math.sqrt(d)")
    print(math.sqrt(d))
    print(" ")
    x1 = (-b+math.sqrt(d))/(2*a)
    print("-b+math.sqrt(d)")
    print(-b+math.sqrt(d))
    print(" ")
    x2 = (-b-math.sqrt(d))/(2*a)
    print("-b-math.sqrt(d)")
    print(-b-math.sqrt(d))
    print(" ")
    print("two solutions")
    print(x1)
    print(x2)
    xmid = (x1 + x2) /2
    y= (a*xmid**2)+(b*xmid)+(c)
    print("min or max point is " + str(xmid) + "," + str(y))

raw_input()
