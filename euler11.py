#!/usr/bin/env python
#encoding: utf-8


def euler11(fl, n):
	matrix = readfile(fl)
	m = 0
	
	for row in matrix:
		x = matrix.index(row)
		for e in row:
			count = 0
			y = row.index(e)
			sum_honrizontal = 1
			sum_vertical = 1
			sum_diagnal1 = 1
			sum_diagnal2 = 1
			
			while count < n:
				if len(row) - y >= n:
					sum_honrizontal *= int(row[y+count])
				if len(row) - y >= n and len(matrix) - x >= n:	
					sum_diagnal1 *= int(matrix[x+count][y+count])
				if len(matrix) - x >= n and y >= n:
					sum_diagnal2 *= int(matrix[x+count][y-count])
				if len(matrix) - x >= n:
					sum_vertical *= int(matrix[x+count][y])
				count += 1
					 
			if sum_honrizontal > m:
				m = sum_honrizontal
			if sum_diagnal1 > m:
				m = sum_diagnal1
			if sum_diagnal2 > m:
				m = sum_diagnal2
			if sum_vertical > m:
				m = sum_vertical			
	print m
		
def readfile(dir):
	f = open(dir, 'r')
	a = []
	
	line = f.readline()
	while line != '':
		a.append(line.split(' '))
		line = f.readline()		
	for suba in a:
		suba[len(suba)-1]=suba[len(suba)-1][0:2]

	return a
		
if __name__ == '__main__':
	files = 'input11.txt'
	euler11(files, 4)