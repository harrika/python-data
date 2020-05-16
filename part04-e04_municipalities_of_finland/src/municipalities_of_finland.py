#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
	df = pd.read_csv('src/municipal.tsv', sep="\t", index_col=0)
	df1 = df.iloc[1:312]
	return df1
    
def main():
	aa = municipalities_of_finland()
	print(aa)

    
if __name__ == "__main__":
    main()
