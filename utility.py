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

# given number n, return all abundant number in the range 1-n
def getAbundants(n):
  return [i for i in range(1, n+1) if isAbundant(i)]

# find a list of prime number untill n
def findPrime(n):
	c=[2,3]
	num=1

	for i in range(5,n+1):
		flag=0
		for m in c:
 			if i%m is 0:
				flag=1
				break
		if flag is 0 and i is not 1:
			c.append(i)
			
	return c

# subroutine for findPrime2
def isPrime(n):
  for i in xrange(2, int(math.ceil(math.sqrt(n))) + 1):
    if n%i == 0:
      return False
  return True

# another way to find a list of primes until n
# returns a generator
def findPrime2(n):
  for i in xrange(1, n):
    if isPrime(i):
      yield i
