giftList = ['$10 vouchers', 'Keychain',
            'Umbrella', 'Tote Bag',
            '$50 vouchers', '25% rebate for all purchases',
            'DKNY perfume 25ml','$20 vouchers',
            'Kose Mask White 50ml', 'Pearl Necklace']


while len(giftList) > 0:
    gre = 'We have ' + str(len(giftList)) + ' gifts to be given away!'
    inp = 'Enter a number from 0 to ' + str(len(giftList)-1) + ' '
    print(gre)
    n = input(inp)
    con = 'Congratuations, you have won a ' + str(giftList[n])
    print(con)
    giftList.pop(n)

raw_input()
