#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
	m,n = a.shape
	k = int(n/2)
	x1 = a[:,0:k]
	x2 = a[:,k:]
	sx1 = np.sum(x1, axis=1)
	sx2 = np.sum(x2, axis=1)
	tr = sx1>sx2
	aa = a[tr]
	return aa

def main():
	np.random.seed(110)
	ee = np.random.randint(1,50,(3,8))
	print(ee)
	print()
	print(first_half_second_half(ee))

if __name__ == "__main__":
    main()
 