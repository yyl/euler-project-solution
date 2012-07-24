import math

# given number m, return a list of divisors of m
def findDivisor(m):
  D = [1,m]
  for i in range(2,int(math.floor(math.sqrt(m)))):
    if m%i == 0:
      d += 2
      D.append(i)
      if m/i == i:
        d -= 1
      else:
        D.append(m/i)
  return D

