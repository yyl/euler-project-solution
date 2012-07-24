'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''


def approach1(m):
  result = 0
  for i in range(1,m+1):
    result += i**i

  return str(result)[-10:]

print approach1(1000)

