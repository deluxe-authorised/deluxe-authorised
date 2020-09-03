enter='Enter your CA grade for week ', ' <A/B/C/D/F/X/LOA> : ','A - 4.0, B - 3.0, C - 2.0, D - 1.0, F - 0.0, X - 0.0,  LOA - Not counted towards average total'
wk01 = raw_input(enter[0] + '1' + enter[1])
wk02 = raw_input(enter[0] + '2' + enter[1])
wk03 = raw_input(enter[0] + '3' + enter[1])
wk04 = raw_input(enter[0] + '4' + enter[1])
wk05 = raw_input(enter[0] + '5' + enter[1])
wk06 = raw_input(enter[0] + '6' + enter[1])
wk07 = raw_input(enter[0] + '7' + enter[1])
wk08 = raw_input(enter[0] + '8' + enter[1])
wk09 = raw_input(enter[0] + '9' + enter[1])
wk10 = raw_input(enter[0] + '10' + enter[1])
wk11 = raw_input(enter[0] + '11' + enter[1])
wk12 = raw_input(enter[0] + '12' + enter[1])
wk13 = raw_input(enter[0] + '13' + enter[1])
print enter[2]
con = 'Your daily grade for 13 weeks: ', 'Your daily score for 13 weeks: '
show_grade = [wk01, wk02,wk03,wk04,wk05,wk06,wk07,wk08,wk09,wk10,wk11,wk12,wk13]
print con[0], show_grade
copy = show_grade
n = 0
while n < 13:
    if copy[n] == 'A':
        copy[n] = 4.0
    elif copy[n] == 'B':
        copy[n] = 3.0
    elif copy[n] == 'C':
        copy[n] = 2.0
    elif copy[n] == 'D':
        copy[n] = 1.0
    elif copy[n] == 'F':
        copy[n] = 0.0
    elif copy[n] == 'X':
        copy[n] = 0.0
    elif copy[n] == 'LOA':
        copy[n] = "LOA"
    else:
        copy[n] = 0.0
    n=n+1
show_score = copy
print con[1], show_score

raw_input()
