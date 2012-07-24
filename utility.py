import math

CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# given number m, return a list of divisors of m
def findDivisors(m):
  D = [1,m]
  for i in range(2,int(math.floor(math.sqrt(m)))):
    if m%i == 0:
      D.append(i)
      if m/i != i:
        D.append(m/i)
  return D

