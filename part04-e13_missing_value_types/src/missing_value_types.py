#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
	stat = pd.Series(["United Kingdom","Finland","USA","Sweden","Germany","Russia"])
	ind = pd.Series([np.nan, 1917, 1776, 1523, np.nan, 1992])
	pres = pd.Series([None, "Niinisto", "Trump", None, "Steinmeier","Putin"])

	ss = {'State':stat, 'Year of independence':ind, 'President':pres}
	df = pd.DataFrame(ss)
	df = df.set_index('State')
	return df


               
def main():
	dd = missing_value_types()
	print(dd)

if __name__ == "__main__":
    main()
