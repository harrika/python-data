#!/usr/bin/env python3
import pandas as pd

def inverse_series(s):
	ix = list(s.index)
	val = list(s.values)	
	ss = pd.Series(ix, index=val)
	return ss

def main():
	a = [1,2,3,4,5]
	b = [100,200,300,400,500]
	ss = pd.Series(b, index=a)
	print(ss)
	ss2 = inverse_series(ss)
	print(ss2)

if __name__ == "__main__":
    main()
