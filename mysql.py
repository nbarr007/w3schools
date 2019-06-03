print(" this app tells the year you are gonna be 100 years old")
""" This part is the part that tells the date of today"""
from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
date = " year %d, day %d, month %d" % (current_year, current_day, current_month)
""" This part is the personal input part"""
name = input(" what is your name?")
print(" your name is" + name)
age = input(" what\'s your age?")
for key in age:
    if key.isdigit():
        print(" your age is " + age)
else:
    print(" please try again")
""" The part of naming and age ends here then we move to persons aging part"""
year = str((current_year - int(age)) + 100)
birthyear = str( current_year - int(age))
print( name + " your birth year is " + birthyear)
print( "and you will be 100 years old in the year " + year)