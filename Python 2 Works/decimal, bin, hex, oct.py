var=1
while var==1:
    inter=int(input("decimal: -, oct: 0, hex: 0x, bin: 0b"))
    bs10=int(inter)
    bs16=hex(inter)
    bs8=oct(inter)
    bs2=bin(inter)
    print(bs10)
    print(bs16)
    print(bs8)
    print(bs2)
    if inter==0:
        var=0
    

    
