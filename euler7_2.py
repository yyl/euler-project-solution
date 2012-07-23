#!/usr/bin/env python
#encoding: utf-8

import timeit

def prob_7(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                num += 2
                break
        else:
            primes.append(num)
            num += 2
    print(primes[n - 1])

if __name__ == '__main__':
	t=timeit.Timer("euler7_2.prob_7(1000001)", "import euler7_2")
	print t.repeat(1,1)