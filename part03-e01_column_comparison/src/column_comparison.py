#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
	x = a[:,1]
	y = a[:,-2]
	tr = x>y
	cc = a[tr]
	return cc
    
def main():
	np.random.seed(110)
	ee = np.random.randint(1,50,(3,4))
	print(column_comparison(ee))



	# column_comparison(aa)

if __name__ == "__main__":
    main()
