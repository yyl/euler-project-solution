#!/usr/bin/env python
#encoding: utf-8

from fprime import*

def euler5(n):
	a=[]
	b=[]
	c=[]
	num=1
	
	for i in range(1,n+1):
		a.append(0)
		b.append(0)
		
	c=fprime(n)
			
	for j in range(2,n+1):
		for k in c:
			temp=j
			a[k]=0
			while temp%k is 0:
				a[k]+=1
				temp=temp/k
			if a[k]>b[k]:
				b[k]=a[k]
			
	print a
	print b
	
	for i in range(1,len(b)):
		if b[i] is not 0:
			for j in range(1,b[i]+1):
				num=num*i
				
	print num
		
if __name__ == '__main__':
	euler5(20)