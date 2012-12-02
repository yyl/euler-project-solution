import re

from utility import findDivisors

def approach1():
  abundants = []
  result = 0
  for i in range(1, 20162):
    if isAbundant(i):
      abundants.append(i)
#print abundants

  for i in range(1, 20162):
    if notTwoAbundants(i, abundants):
      result += i

  print result

def approach2():
  correct = []
  abundants = getAbundants(28123)
  two_abundants = [i+j for i in abundants for j in abundants if (i+j) < 28124]
  #x_nodups = dict(map(lambda i: (i,1), two_abundants)).keys()
  two_nodups = list(set(two_abundants))
  if any([1141, 1771, 7621]) in two_nodups:
    print True
  all = list(set(range(1, 28124)) - set(two_abundants))
  result = sum(range(1, 28124)) - sum(two_nodups)
  for line in open('b048242.txt', 'r'):
    number = re.search(r' (\d+)', line)
    if number:
      correct.append(int(number.group(1)))

  print "in my answer but not in correct file:\n"
  for number in all:
    if number not in correct:
      print number

  print "in correct file but not in my answer:\n"
  for number in correct:
    if number not in all:
      print number

  print sum(correct)

def approach3():
  abundants = getAbundants(28123)
  def abundantsum(i):
        return any(i-a in abundants for a in abundants)
  print sum(i for i in range(1,28124) if not abundantsum(i))


def notTwoAbundants(i, abundants):
  dic = [a for a in abundants if a < i]
  for a in dic:
    if (i-a) in dic:
      if i == any([1141, 1771, 7621]):
        print i, a, i-a
      return False
  else:
    return True

def isAbundant(i):
  D = findDivisors(i)
  if sum(D) > 2*i:
    return True
  else:
    return False

def getAbundants(n):
  return [i for i in range(1, n+1) if isAbundant(i)]

approach2()
