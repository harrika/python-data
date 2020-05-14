#!/usr/bin/env python3
import numpy as np

def diamond(n):
	cc = np.eye(n, dtype=int)
	zz = np.empty_like(cc)
	zz[:] = cc
	for e in range(2,n+1):
		ss = cc[:,-e].reshape(n,1)
		zz = np.concatenate((zz,ss), axis=1)

	# print('zz: \n', zz)
	zaz = np.empty_like(zz)
	zaz[:] = zz
	a,b = zz.shape
	for p in range(1,a):
		sas = zz[p,:].reshape(1,b)
		zaz = np.concatenate((sas,zaz))
	# print('zaz: \n', zaz)
	return zaz

def main():
	print(diamond(4))

if __name__ == "__main__":
    main()
