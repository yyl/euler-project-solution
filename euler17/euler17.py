'''
Euler project problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import re

def numbase():
  dic = []
  for line in open('1to99.txt', 'r'):
    match = re.search(r'\d+? = ([\w-]+)', line)
    if match:
      dic.append(match.group(1).replace("-", ""))

  return dic

# only works for 1000
def approach1():
  dic = []
  result = 0
  for line in open('1to99.txt', 'r'):
    match = re.search(r'\d+? = ([\w-]+)', line)
    if match:
      dic.append(match.group(1))

  dic = [line.replace("-","") for line in dic]

  from1to99 = sum([len(line) for line in dic])
  result += from1to99
  print from1to99

  for i in dic[:9]:
    print i
    # 100 and 101 - 199
    add = (len(i) + 7 + 3) * 99 + len(i) + 7
    result += (add + from1to99)

  #1000
  result += 11
  print result

def approach2(n):
  dic = numbase()
  result = 0
  size = len(str(n))

  if size < 3:
    result = sum([len(number) for number in dic[:n]]
  elif size < 4:
    for i in range(n%100):
      
