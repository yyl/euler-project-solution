import math

CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# given number m, return a list of divisors of m
def findDivisors(m):
  D = [1,m]
  for i in range(2,int(math.ceil(math.sqrt(m)))):
    if m%i == 0:
      D.append(i)
      if m/i != i:
        D.append(m/i)
  return D

def isAbundant(i):
  D = findDivisors(i)
  if sum(D) > 2*i:
    return True
  else:
    return False

#given number n, return all abundant number in the range 1-n
def getAbundants(n):
  return [i for i in range(1, n+1) if isAbundant(i)]


