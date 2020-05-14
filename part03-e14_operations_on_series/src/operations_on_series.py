#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
	ix = ['a','b','c']
	s1 = pd.Series(L1, index=ix)
	s2 = pd.Series(L2, index=ix)
	return (s1,s2)
    
def modify_series(s1, s2):
	print(s1)
	s1['d'] = s2['b']
	del s2['b']
	return s1,s2
    
def main():
	l1 = [23,24,25]
	l2 = [44,43,45]
	s1,s2 = create_series(l1,l2)
	gg = modify_series(s1, s2)
	print(gg)
	gg2 = s1+s2
	print(gg2)





	# return
    
if __name__ == "__main__":
    main()
