'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


from datetime import date, timedelta
import calendar

def approach1():
  start = date(1901, 1, 1)
  end = date(2000, 12, 31)
  step = timedelta(days=1)
  count = 0

  while start <= end:
    if start.isoweekday() == 7 and start.day == 1:
      count += 1
      print start, "is a sunday and also the first of a month"
    start += step

  print count

def approach2():
  total = 0
  for y in range(1901,2001):
    for m in range(1,13):
      if(calendar.weekday(y,m,1) == 6):
        total = total + 1
  print total

approach2()
