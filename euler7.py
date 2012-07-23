#!/usr/bin/env python
#encoding: utf-8
#find nth prime number

import timeit

def euler7(n):
	c=[2,3]
	i=5
	count=2

	while count<n:
		flag=0
		for m in range(2, int(i**0.5) + 1):
 			if i%m is 0:
				flag=1
				break
		if flag is 0:
			c.append(i)
			count+=1
		i+=1
			
	return c
	
if __name__ == '__main__':
	t=timeit.Timer("euler7.euler7(10001)", "import euler7")
	print t.repeat(1,1)
	#print t.timeit()
	#a=euler7(10001)
	#print a[10000]