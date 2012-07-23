#!/usr/bin/env python
#encoding: utf-8

'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number
 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def euler20(n):
	num = factor(n)
	sum = 0
	while num > 0:
		digit = num - 10*(num/10)
		num = (num - digit)/10

		sum+=digit
	
	print sum
	
	
def factor(n):
	if n == 1:
		return 1
	else:
		return factor(n-1)*n

		
if __name__ == '__main__':
	euler20(100)