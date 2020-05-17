#!/usr/bin/env python3

import pandas as pd

def average_temperature():
	df = pd.read_csv('src/kumpula-weather-2017.csv')
	cols2drop = ['Year','d','Time','Time zone','Precipitation amount (mm)','Snow depth (cm)']
	df = df.drop(cols2drop, axis=1)
	df = df.loc[df['m'] == 7]
	desc = df.describe()['Air temperature (degC)']	
	return desc['mean']

def main():
	avt = average_temperature()
	print('Average temperature in July: {:2.1f}'.format(avt))

if __name__ == "__main__":
    main()
