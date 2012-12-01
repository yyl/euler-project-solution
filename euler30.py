
def euler30():
  result = 0
  for num in xrange(2, 1000000):
    l = list(str(num))
    if num == sum([int(n)**5 for n in l]):
      print num
      result += num

  print "result, ", result

euler30()

