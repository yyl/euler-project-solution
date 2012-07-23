#!/usr/bin/env python
#encoding: utf-8

#euler pro 10: find sum of all primes under 2 million

import timeit, math

def euler10(n):
	c=[2,3]
	fsum=5

	for i in range(4,n+1):
		flag=0
		#Sum+=i
		threshold=math.sqrt(i)
		j=0
		
		while c[j]<=threshold:
			if i%c[j] is 0:
				flag=1
				break
			j+=1
		if flag is 0:
			c.append(i)
			fsum+=i
			
	#fsum=Sum-sum
	return fsum
	
if __name__ == '__main__':
	#t=timeit.Timer("euler10.euler10(2000000)", "import euler10")
	#print t.repeat(1,1)
	a=euler10(2000000)
	print a