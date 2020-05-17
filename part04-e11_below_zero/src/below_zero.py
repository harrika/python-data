#!/usr/bin/env python3

import pandas as pd

def below_zero():
	df = pd.read_csv('src/kumpula-weather-2017.csv')
	cols2drop = ['Year','m','Time','Time zone','Precipitation amount (mm)','Snow depth (cm)']
	df = df.drop(cols2drop, axis=1)
	df = df.loc[df['Air temperature (degC)'] < 0]
	return df.shape[0]

def main():
	num = below_zero()
	print('Number of days below zero: {:d}'.format(num))

if __name__ == "__main__":
    main()
