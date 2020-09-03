joinedCodeList = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
codeList = list(joinedCodeList)
pointList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
pointList = pointList + pointList
i=0
while i == 0: 
    rawMsg = raw_input('Type in the word or q to exit: ')
    if rawMsg == 'q':
        i=1
    msg = list(rawMsg)
    points=0
    n=0
    while n < len(msg):
        o=0
        while o < len(codeList):
            if msg[n] == codeList[o]:
                points=points+pointList[o]
                print 'The letter '+msg[n]+" is "+str(pointList[o])+" points."
            o=o+1
        n=n+1
    print "The word "+rawMsg+" is "+str(points)+" points."
