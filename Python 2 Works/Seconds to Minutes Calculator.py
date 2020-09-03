print(" Program designed by DXChiam, Chiam Da Xiang")
print("   (C) Copyright are all rights reserved")
print("         For educational uses only")
print("This is a calculator for calculating how many seconds to minutes and beyond")
x=input("Whole number: ") # Input whole number
dayf = x / 86400 # No. of days
daym = x % 86400 # Remainder in secs after removing days
hourf = daym / 3600 # no. of hours
hourm = daym % 3600 # Remainder in secs after removing hours
minf = hourm / 60 # No. of mins
secf = hourm % 60 # No. of secs
day = str(dayf) # Converting days from int to str
hour = str(hourf) # convert hour from int to str
min = str(minf) # convert min from int to str
sec = str(secf) # convert sec from int to str
if dayf==0 and hourf==0 and minf==0:
   print(sec + " second(s)") # Display result
elif dayf==0 and hourf==0:
   print(min + " minute(s) " + sec + " second(s)") # Display result
elif dayf==0:
   print(hour + " hour(s) " + min + " minute(s) " + sec + " second(s)") # Display result
elif dayf!=0:
   print(day + " day(s) " + hour + " hour(s) " + min + " minute(s) " + sec + " second(s)") # Display result
else:
   print(day + " day(s) " + hour + " hour(s) " + min + " minute(s) " + sec + " second(s)") # Display result
raw_input() # Prevents cmd from closing after last command is executed
