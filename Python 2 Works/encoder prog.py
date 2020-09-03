codeList = '1qaz!QAZ2wsx@WSX3edc#EDC4rfv$RFV5tgb%TGB6yhn^YHN7ujm&UJM8ik,*IK<9ol.(OL>0p;/)P:?'
list1 = list(codeList)
list2 = list(codeList)
list2.append(list1[0])
list2.remove(list1[0])
save = []
i=0
while i == 0: 
    message = raw_input('Type in message for encoding (quit to exit, save to view, clear to clear): ')
    msg = list(message)
    code = []
    n=0
    while n < len(msg):
        o=0
        while o < len(codeList):
            if msg[n] == list1[o]:
                code.append(list2[o])
            o=o+1
        n=n+1
    print "".join(code)
    save.append("".join(code))
    if message == 'quit':
        i=1
        raw_input()
    if message == 'save':
        print ' '.join(save)
    if message == 'clear':
        save = []
