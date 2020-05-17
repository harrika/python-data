#!/usr/bin/env python3

import pandas as pd

def snow_depth():
	df = pd.read_csv('src/kumpula-weather-2017.csv')
	dessd = df.describe()['Snow depth (cm)']
	sd = dessd.loc['max']
	return sd

def main():
	sd = snow_depth()
	print('Max snow depth: {:2.1f}'.format(sd))

if __name__ == "__main__":
    main()
