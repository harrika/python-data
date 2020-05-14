#!/usr/bin/env python3
import numpy as np
from functools import reduce

def matrix_power(a, n):
	ae = np.linalg.inv(a)
	m = a.shape[0]
	aa = [a]*n
	bb = [ae]*n
	if n==0:
		return np.eye(m)
	if n==1:
		return a

	fn = lambda x,y: x@y
	if n<0:
		return reduce(fn, bb, np.eye(m))
	else:
		return reduce(fn, aa, np.eye(m))



def main():
	a = np.random.randint(1,10,(4,4))	
	print(matrix_power(a, 0))


if __name__ == "__main__":
    main()
