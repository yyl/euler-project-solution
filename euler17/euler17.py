'''
Euler project problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import re

# return a list of english words of numbers
def numbase():
  dic = []
  for line in open('1to99.txt', 'r'):
    match = re.search(r'\d+? = ([\w-]+)', line)
    if match:
      dic.append(match.group(1).replace("-", ""))

  return dic

# only works for 1000
def approach1():
  result = 0
  dic = numbase()

  # the number of characters in words one to 99
  from1to99 = sum([len(line) for line in dic])
  result += from1to99

  for i in dic[:9]:
    # 100 and 101 - 199
    add = (len(i) + 7 + 3) * 99 + len(i) + 7
    result += (add + from1to99)

  #1000
  result += 11
  print "one to one thousand: ", result

approach1()
