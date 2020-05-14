#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
	dd = []
	m,n = a.shape	
	for e in range(m):
		cc = a[e,:].reshape(1,n)
		dd.append(cc)
	return dd

def get_column_vectors(a):
	ddx = []
	m,n = a.shape	
	for p in range(n):
		cc = a[:,p].reshape(m,1)
		ddx.append(cc)
	return ddx

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
