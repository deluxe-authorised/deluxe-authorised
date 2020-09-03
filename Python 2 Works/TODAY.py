def power(x,y):
    result=1
    i=0
    while i<y:
        result=result*x
        i=i+1
    return result

def fact(n):
    i=1
    fact = 1
    while i <= n:
        fact=fact*i
        i=i+1
    return fact

list=[]
sum=0
i=0
while i == 0:
    if i == 0:
        n=input('input n: ')
        r=input('input r: ')
        p=input('input p: ')
        perRep = power(n,r)
        perWR = fact(n) / fact(n-r)
        comWR = (perWR) / fact(r)
        comRep = fact(n+r-1) / fact(n-r) / fact(r)
        n=float(n)
        r=float(r)
        bd = p**r * (1-p)**(n-r)
        bd = bd * comWR
        list.append(bd)
        sum=sum+bd
        print "answer is ",bd
        print "past history is ",list
        print "sum of all records is ", sum
    if n == 0:
        i=1
        raw_input('exit')
    