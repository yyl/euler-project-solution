from utility import isPrime, findPrime2

count = 0
for prime in findPrime2(1000000):
  prime = str(prime)
  for i in xrange(0, len(prime) - 1):
    if not isPrime(int(prime[i+1:] + prime[:i+1])):
      break
  else:
    count += 1
print count
