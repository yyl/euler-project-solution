#!/usr/bin/env python
#encoding: utf-8

import math

def sumsquare(n):
	return n*(n+1)*(2*n+1)/6
	
def squaresum(n):
	return math.pow((n*(n+1)/2),2)
	
def main():
	sum_square = 0
	square_sum = 0
	sum_square = sumsquare(100)
	square_sum = squaresum(100)
	print "square_sum is", square_sum
	print "sum_square is", sum_square
	diff = square_sum - sum_square
	print diff

if __name__ == '__main__':
	main()