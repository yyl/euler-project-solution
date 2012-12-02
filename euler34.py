import math

def factorial(x):
  return math.factorial(x)

result = 0

for n in xrange(3, 1000000):
  digits = [int(i) for i in list(str(n))]
  if sum([factorial(d) for d in digits]) == n:
    print n
    result += n

print result
