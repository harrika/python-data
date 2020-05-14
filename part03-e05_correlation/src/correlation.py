#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    # print(data)
    sl0 = data[:,0]
    pl2 = data[:,2]
    res = scipy.stats.pearsonr(sl0,pl2) # a column of tuples
    # return res[:,0]
    return res[0]
    # return res

def correlations():
    data = load()
    sl0 = data[:,0]
    sw1 = data[:,1]
    pl2 = data[:,2]
    pw3 = data[:,3]
    # co = np.corrcoef(sl0,sw1,pl2,pw3)
    # co = np.corrcoef(sl0,sw1)
    co = np.corrcoef(data, rowvar=False)
    return co

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
