#!/usr/bin/env python
#encoding: utf-8


def euler4(d):
	minimum=pow(10,d-1)
	maximum=0
	for i in range(d):
		maximum+=(9*pow(10,i))
	
	temp=0
	for k in range(maximum+1,minimum,-1):
		for j in range(maximum+1,minimum,-1):
			n=k*j
			m=reverse(n)
			if m==n and n>temp:
				temp=n
		
		if k==50:break
		
	print temp

def reverse(temp):
	r=[]
	i=1
	while temp is not 0:
		modu=(temp%(pow(10,i)))/pow(10,i-1)
		r.append(modu)
		temp=temp-temp%(pow(10,i))
		i+=1
		
	output=0
	for j in range(len(r)-1,-1,-1):
		output+=r[j]*pow(10,len(r)-(j+1))
	return output
		
if __name__ == '__main__':
	euler4(3)