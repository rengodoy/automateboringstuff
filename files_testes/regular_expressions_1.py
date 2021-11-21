'''
Date Detection

Write a regular expression that can detect dates in the DD/MM/YYYY format. 
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. 
Note that if the day or month is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. 
April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days.
February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
'''

import re

dateRegex = re.compile(r'''
(([0-2][0-9]|3[0-1])     # 01-31
\/                       # /
(0[0-9]|1[0-2])          # 01-12
\/                       # /
([1-2][0-9][0-9][0-9]))  # 1000-2999
''', re.VERBOSE)
result = dateRegex.findall('''
12/13/9990 - não
34/12/1000 - não
01/03/2000 - sim
01/13/2000 - não
21/11/2000 - sim
56/12/2000 - não
01/56/2000 - não
30/12/2015 - sim
31/12/2040 - sim
31/04/2041 - não
31/22/2040 - não
01/12/0999 - não
04/12/1979 - sim

29/02/1996 - sim
29/02/2096 - sim

''')

i = 0
for date,day,month,year in result:
    if month in ["04","06","09","11"] and day > "30":
        result.remove(result[i])
    leap = 0
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
    if not(int(year)%4):
        leap = 1
        if not(int(year)%100):
            leap = 0
            if not(int(year)%400):
                leap = 1
    
    if month == "02" and day > "28" and leap == 0:
        result.remove(result[i])
    i+=1

print(result)
