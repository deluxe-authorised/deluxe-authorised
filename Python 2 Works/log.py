import math
x = 2
y = 2
e = float(math.e)
x = input('input number to log: ')
print('if base is maths e, type e')
y = input('input base of log: ')

if y == e:
    print(math.log(x,e))
    
elif y == 10:
    print(math.log10(x))
    
else:
    print(math.log(x,y))

raw_input()
