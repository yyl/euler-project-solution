#!/usr/bin/env python
#encoding: utf-8


def euler13(d, n, dir):	
	num = file2num(n, dir)
	summ = sumUp(num)
	digits = sum2digit(d, summ)
	return digits
		
def file2num(n, dir):
	f = open(dir, 'r')
	a = []
	line = f.readline()
	while line != '':
		if line[-1] == '\n':
			line = line[:-1]
		a.append(int(line))
		line = f.readline()			
	return a
	
def sumUp(numbers):
	suma = 0
	for an in numbers:
		suma += an
	return suma
			
def sum2digit(di, dsum):
	ssum = str(dsum)
	digits = ssum[0:10]
	return digits
	
if __name__ == '__main__':
	d = 'input13.txt'
	digits = euler13(10, 50, d)
	print digits