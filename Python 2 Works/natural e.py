import math

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
f = 1 + float(1)/fac(1) + float(1)/fac(2) + float(1)/fac(3) + float(1)/fac(4) + float(1)/fac(5) + float(1)/fac(6) + float(1)/fac(7) + float(1)/fac(8) + float(1)/fac(9) + float(1)/fac(10)
f2 = float(1)/fac(11) + float(1)/fac(12) + float(1)/fac(13) + float(1)/fac(14) + float(1)/fac(15) + float(1)/fac(16) + float(1)/fac(17) + float(1)/fac(18) + float(1)/fac(19) + float(1)/fac(20)
f3 = float(1)/fac(21) + float(1)/fac(22) + float(1)/fac(23) + float(1)/fac(24) + float(1)/fac(25) + float(1)/fac(26) + float(1)/fac(27) + float(1)/fac(28) + float(1)/fac(29) + float(1)/fac(30)

ffin = f + f2 + f3
print(ffin)

print(math.e)

raw_input()
