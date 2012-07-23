#!/usr/bin/env python
#encoding: utf-8

'''
no.8: Find the greatest product of five consecutive digits
in the 1000-digit number.
'''

def euler8(n):
	fi=open("input8.txt","r")
	previous=1
	a=[]
	
	fi.seek(1,0)
	digit=fi.read(1)
	while digit != '':
	#for k in range(0,1018):
		if digit != '\n':
			a.append(digit)
		digit=fi.read(1)
	print a

	for i in range(0,len(a)-n):
		product=1
		for j in range(0,n):
			product*=int(a[i+j])
		print i+j,':',product
		if product>previous:
			previous=product
	print previous

if __name__ == '__main__':
	euler8(5)