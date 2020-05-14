#!/usr/bin/env python3

import numpy as np

def get_rows(a):
	dd = []
	rr = a.shape[0]
	for e in range(rr):
		dd.append(a[e,:])
	return dd

def get_columns(a):
	cc = []
	ee = a.shape[1]
	for p in range(ee):
		cc.append(a[:,p])
	return cc

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
