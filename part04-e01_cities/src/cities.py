#!/usr/bin/env python3

import pandas as pd

def cities():
	l1 = [643272, 279044, 231853, 223027, 201810]
	l2 = [715.48, 528.03, 689.59, 240.35, 3817.52]
	s1 = pd.Series(l1)
	s2 = pd.Series(l2)
	ix =['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']
	df = pd.DataFrame({'Population': s1, 'Total area': s2})
	df.index = ix
	return df

    
def main():
	aa = cities()
	print(aa)
    
if __name__ == "__main__":
    main()
