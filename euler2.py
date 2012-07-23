#!/usr/bin/env python
#encoding: utf-8


def main():
	fibo = [1,2]
	ans = 2
	for i in range(3,100):
		temp = fibo[i-2]+fibo[i-3]
		if temp > 4e6:
			print fibo[i-2], "is where we end"
			break
		fibo.append(temp)
		if temp%2 is 0:
			ans += temp
	print ans, "is the answer"
	for i in fibo:
		print i

		
if __name__ == '__main__':
	main()