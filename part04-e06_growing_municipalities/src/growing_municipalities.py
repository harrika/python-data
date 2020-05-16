#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
	den = len(df.index)
	mm = df["Population change from the previous year, %"]>0.0
	df2 = df[mm]
	num = len(df2.index)
	ratio = num/den
	return ratio

def main():
	df = pd.read_csv('src/municipal.tsv', sep="\t", index_col=0)	
	ratio = growing_municipalities(df)
	print("Proportion of growing municipalities: {:2.1f}%".format(ratio))




if __name__ == "__main__":
    main()
