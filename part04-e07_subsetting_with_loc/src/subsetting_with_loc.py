#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
	df = pd.read_csv('src/municipal.tsv', sep="\t", index_col=0)
	# df = df.iloc[1:312]	
	df = df.loc['Akaa':'Äänekoski']	
	cols = ['Population','Share of Swedish-speakers of the population, %',
	'Share of foreign citizens of the population, %']
	return df[cols]


def main():
	gg = subsetting_with_loc()
	print(gg)

if __name__ == "__main__":
    main()
