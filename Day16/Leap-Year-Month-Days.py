'''
TITLE: Leap Year Months and Days
DESCRIPTION: A twist on the original leap year program I completed.
      This program allows the user to check if a year is a leap year or not. 
      It also can tell you how many days are within a specific month, based
      on the year the user is checking. 
USED: def functions, parameters, arguments, lists
'''

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leap_year = [29] 

  if is_leap(year) == True:
      month_name = month_days[int(month) - 1] + 1
      return month_name
  else:
      month_name = month_days[int(month) -1]
      return month_name
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
