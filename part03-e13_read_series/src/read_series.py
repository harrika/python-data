#!/usr/bin/env python3
import numpy as numpy
import pandas as pd

def read_series():
	ix = []
	wd = []
	while 1:
		a = input("enter index and word:  ")
		if a == "":
			break
		aa = a.split()
		if len(aa) != 2:
			raise Exception('you input was malformed ')
		ix.append(aa[0])
		wd.append(aa[1])
	return pd.Series(wd, index=ix)

def main():
	pds = read_series()
	print(pds)

if __name__ == "__main__":
    main()
