#!/usr/bin/env python
#encoding: utf-8

from fprime import*

def euler6(n):
	factor=fprime(9000)
	primef=[]
	
	for f in factor:
		while n%f is 0:
			primef.append(f)
			n=n/f
			print 'n:',n
			
	print primef
			
		
if __name__ == '__main__':
	euler6(600851475143)