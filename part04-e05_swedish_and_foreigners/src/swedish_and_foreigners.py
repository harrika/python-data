#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
	df = pd.read_csv('src/municipal.tsv', sep="\t", index_col=0)
	df = df.iloc[1:312]	
	m1 = df["Share of foreign citizens of the population, %"]>5.0
	df1 = df[m1]
	m2 = df1["Share of Swedish-speakers of the population, %"]>5.0
	df2 = df1[m2]
	cols = ['Population','Share of foreign citizens of the population, %',
			'Share of Swedish-speakers of the population, %']
	return df2[cols]

def main():
	gg = swedish_and_foreigners()
	print(gg)

if __name__ == "__main__":
    main()
21 