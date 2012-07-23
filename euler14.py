#!/usr/bin/env python
#encoding: utf-8


def decision(d):
	if d%2 == 0:
		return d/2
	else:
		return 3*d+1

def chains(n):
	count = 0
	while n>1:
		n = decision(n)
		count += 1
	return count

def euler141(n):
	distance = 499999
	differ = distance
	maxindex = 0
	maximum = 0
	while distance > 1:
		term = chains(n-distance)
		if term > maximum:
			maxindex = differ - distance
			maximum = term
		distance-=2
	maxnum = n - differ + maxindex
	return maximum, maxnum

############################tempt 2			
def findnextnum(d, c):
	c+=1
	if d == 1:
		return c
	elif d%2 == 0:
		return findnextnum(d/2, c) 
	else:
		return findnextnum(3*d+1, c)

def euler142(n):
	cuont = 0
	maximum = 0
	maxnum = 0
	while n > 500000:
		count = findnextnum(n, 0)
		if count > maximum:
			maximum = count
			maxnum = n
		n-=1
	return maximum, maxnum
	
			
if __name__ == '__main__':
	#print euler14(1000000)
	print euler142(1000000)