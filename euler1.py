#!/usr/bin/env python
# encoding: utf-8


def main():
	sum = 0
	for i in range(1,1000):
		if i%3 is 0 or i%5 is 0:
			sum += i
	print "the sum is", sum
		
if __name__ == '__main__':
	main()