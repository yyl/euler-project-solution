pairs = [(a,b) for a in xrange(2, 101) for b in xrange(2, 101)]
pool = [a**b for (a,b) in pairs]
print len(set(pool))
