'''Yuu code.py axe'''
def axe(x,y,xy):
    a=x+y
    b=x-y
    c=xy*x*y
    ans=a*b*c-x-y-1/xy
    return ans

'''Yuu code.py gun'''
def gun(x,y,z,t):
    a=x*y-z
    b=x*z-y
    c=y*z-x
    az=a/z+a-1/z
    by=b/y+b-1/y
    cx=c/x+c-1/x
    xyz=az*by*cx+az+by+cx-1/az-1/by-1/cx
    all=a/t+b/t**2+c/t**3+az/t+by/t**2+cx/t**3+xyz/t**4
    return all

'''Yuu code.py yuubari'''
def yuubari(a,b):
    a=a*axe(a,a,a)
    b=b*gun(b,b,b,b)
    run=a*b
    return run

'''Ex trial.py mod'''
def mod (x):
    x=float(x)
    a=x*1.5
    k=x*2.5
    g=x*3.5
    v=x*5.5
    d=x*6.5
    q=x*8.5
    s=x*9.5
    E=x
    A=a
    K=k
    G=g
    V=v
    D=d
    Q=q
    S=s
    return (E,A,K,G,V,D,Q,S)

'''Dictionary Magic.py Tage'''
def Tage():
    n={}
    o=1
    while o <= 38:
        if o <= 4:
            n[0.0+o/100.0]=o/4.0
        if o <= 6:
            n[1.0+o/100.0]=o/6.0
        if o <= 10:
            n[2.0+o/100.0]=o/10.0
        if o <= 14:
            n[3.0+o/100.0]=o/14.0
        if o <= 22:
            n[4.0+o/100.0]=o/22.0
        if o <= 26:
            n[5.0+o/100.0]=o/26.0
        if o <= 34:
            n[6.0+o/100.0]=o/34.0
        n[7.0+o/100.0]=o/38.0
        o=o+1
    return n

'''Yuu code.py main'''
a=input('Yuu code.py a')
b=input('Yuu code.py b')
result=yuubari(a,b)
print result
raw_input()

'''Ex trial.py main'''
run = mod(input('Ex trial.py run'))
print run
raw_input()

'''VariableNameCreator.py main'''
strout=['Enter a long sentence to be converted into a single line: ']
line=raw_input(strout[0])
line=line.split(' ')
edit=line[0]
edit=edit.lower()
edit=list(edit)
edit=''.join(edit)
line[0]=edit
if len(line)!=1:
    i=1
    while i != len(line):
        edit=line[i]
        edit=edit.lower()
        edit=list(edit)
        edit[0]=edit[0].upper()
        edit=''.join(edit)
        line[i]=edit        
        i=i+1
line=''.join(line)
print line
raw_input()

'''Dictionary Magic.py main'''
t=Tage()
for key in sorted(t):
    print '%s %s'%(key,t[key])
raw_input()
