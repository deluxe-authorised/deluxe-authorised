# The script was completed by Chiam Da Xiang, if using it for exams, use with caution
# Errors have been found, try not to use for dates near leap years such as 2000
print("Errors have been found, try not to use for dates near leap years such as 2000")
print(" Program designed by DXChiam, Chiam Da Xiang") # DXChiam Program
print("   (C) Copyright are all rights reserved") # Copyright
print("         For educational uses only") # May have inaccurate results
print("This is a calculator to calculate the day of the week given the date")
year=input("        Year as in YYYY (1901-2099): ") # Input the year
print("                             Year is " + str(year)) # Display year
month=input("             Month as in MM (01-12): ") # Input the month
print("                            Month is " + str(month)) # Display month
print("01    03    05    07 08    10    12: 31 days") # Months with 31 days
print("         04    06       09    11   : 30 days") # Months with 30 days
print("   02                              : 28 days, 29 for leap year") # Feburary
day=input("               Day as in DD (01-31): ") # Input the day
print("                              Day is " + str(day)) # Display day
print("working...")
# Zellers cong values that does not change due to leap year
g = int(7) # Zeller cong later involves mod7
Z = int(0) # Giving initial value Z as 0
q = int(day) # Zeller cong day=q
J = int(year / 100) # zeller cong year's century

# Following ensures month value input is not less than 1 or more than 12
if month==1: # Janurary
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month + 12)
        K = int(year % 100) - 1
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==2: # Feburary
    if 1<=day<=29: # Day input from 1 to 29
        m = int(month + 12)
        K = int(year % 100) - 1
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==3: # March
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==4: # April
    if 1<=day<=30: # Day input from 1 to 30
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==5: # May
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==6: # June
    if 1<=day<=30: # Day input from 1 to 30
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==7: # July
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==8: # August
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==9: # September
    if 1<=day<=30: # Day input from 1 to 30
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==10: # October
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==11: # November
    if 1<=day<=30: # Day input from 1 to 30
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
elif month==12: # December
    if 1<=day<=31: # Day input from 1 to 31
        m = int(month)
        K = int(year % 100)
        g = int(7)
    else: # If invalid value is entered
        g = int(0)
        print("Error")
else: # When month value entered is not within integers 1 to 12
    g = int(0)
    print("Error")

# Formulating zellers cong
a = int(13 * int(m + 1)) / 5 # The month offset due to difference in month last day
s = int(K / 4) # The year offset due to leap year
d = int(J / 4) # The century offset due to leap year
f = int(5 * J) # -2J calculation replaced with +5J to prevent negative may affect mod7
print('working...')
h = int(q + a + K + s + d + f) - 1 # Zeller Cong step one
Z = int(h % g) # Step two is Ans mod7

if Z==0: # Sunday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Sunday.")
elif Z==1: # Monday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Monday.")
elif Z==2: # Tuesday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Tuesday.")
elif Z==3: # Wednesday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Wednesday.")
elif Z==4: # Thursday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Thursday.")
elif Z==5: # Friday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Friday.")
elif Z==6: # Saturday
    print(str(year) + " " + str(month) + " " + str(day) + " is a Saturday.")
else: # If invalid value is entered
    print("Error")
raw_input() # To prevent cmd from closing after last command
