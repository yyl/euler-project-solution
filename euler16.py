"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibo_gen():
  a = 1
  b = 1
  while 1:
    yield a
    a, b = b, a+b


a = fibo_gen()
f = a.next()
count = 1
while 1:
  if len(str(f)) == 1000:
    print count
    break
  f = a.next()
  count += 1

'''
what is the sum of digits of 2^1000?
'''

number = str(2 ** 1000)
digits = [int(a) for a in number]
print sum(digits)

