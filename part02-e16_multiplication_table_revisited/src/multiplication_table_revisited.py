#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
	row = np.arange(n)
	ones = [1]*n
	r1 = np.array(ones).reshape(n,1)
	mat = row*r1
	r2 = row.reshape(n,1)
	return mat*r2

def main():
    print(multiplication_table(4))
    print(multiplication_table(7))

if __name__ == "__main__":
    main()
