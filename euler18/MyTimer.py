import timeit

class Timer(object):
  def __init__(self, func, modu):
    self._func = func
    self._modu = "from __main__ import " + modu

  def timeit(self):
    t = timeit.Timer(self._func, self._modu)
    print "Time elapsed: %f second" % t.timeit(1)
