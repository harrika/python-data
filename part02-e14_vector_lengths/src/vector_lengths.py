#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
	g = np.sum(a**2, axis=1)
	return np.sqrt(g)


def main():
	a = list(range(25))
	a = np.array(a)
	a = a.reshape(5,5)
	print(vector_lengths(a))

if __name__ == "__main__":
    main()
