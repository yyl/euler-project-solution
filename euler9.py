#!/usr/bin/env python
#encoding: utf-8
'''
There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.
Find the product abc.
'''

def euler9(d):
	for m in range(1,501):
		#m must be a float in division to assure correctness
		n=d/(2*float(m))-m
		a=m*m-n*n
		b=2*m*n
		c=m*m+n*n
		if n%1 == 0 and m>n>0:
			print a,b,c,a+b+c,a*b*c
		
if __name__ == '__main__':
	euler9(1000)