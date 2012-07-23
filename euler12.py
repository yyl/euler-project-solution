#!/usr/bin/env python
#encoding: utf-8
from math import sqrt, floor

def euler12():
  D = 0
  n = 1
  step = 2
  while D < 500:
    n += step
    step += 1
    D = findDivisor(n) 
  return n

def triangle(n):
  return n*(n+1)/2

def findDivisor(m):
  d = 2
  for i in range(2,int(floor(sqrt(m)))):
    if m%i == 0:
      d += 2
      if m/i == i:
        d -= 1
  return d

if __name__ == '__main__':
  print euler12()
# print len(findDivisor(triangle(10000)))
