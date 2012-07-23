#!/usr/bin/env python
#encoding: utf-8
#find prime number untill n

import timeit

def fprime(n):
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
	
if __name__ == '__main__':
	#t=timeit.Timer("fprime.fprime(10)", "import fprime")
	#print t.timeit()
	a=fprime(10001)
	print a[10000]