hex2bin = {"0":"0000", "1":"0001", "2":"0010", "3":"0011",
            "4":"0100", "5":"0101", "6":"0110", "7":"0111",
            "8":"1000", "9":"1001", "A":"1010", "B":"1011",
            "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def isPalindrom(n):
  digits = list(str(n))
  size = len(digits)
  old = digits[:]
  digits.reverse()
  if old == digits:
    return True
  else:
    return False

def isPalindrom_base2(n):
  base2 = "".join([hex2bin[h] for h in '%X'%n]).lstrip('0')
  new = list(base2[:])
  new.reverse()
  old = list(base2)
  if old == new:
    return True
  else:
    return False
  

sum = 0
# even number will be skipped
for j in xrange(1, 1000000, 2):
#  isPalindrom(j)
#  isPalindrom_base2(j)
  if isPalindrom(j) and isPalindrom_base2(j):
    sum += j

print sum
