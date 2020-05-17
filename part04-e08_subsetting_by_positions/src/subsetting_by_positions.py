#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
	df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep="\t", index_col=0)
	cols = ['Title', 'Artist']
	df = df.iloc[0:10]
	return df[cols]

def main():
	gg = subsetting_by_positions()
	print(gg)

if __name__ == "__main__":
    main()
