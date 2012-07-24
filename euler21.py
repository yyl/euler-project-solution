'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from utility import findDivisors

def approach1(m):
  result = 0
  for a in range(1, m):
    # find corresponding b
    b = sum(findDivisors(a)) - a
    # check if d(b) = a and b is not a
    if sum(findDivisors(b)) - b == a and b != a:
      print "pair: ", a, b
      result += (a+b)
  # cutting in half for duplicates
  print result/2


approach1(10000)
