#!/usr/bin/env python3
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    df = df[~df['LW'].isin(['New', 'Re'])]
    dff = df[df['Pos'] > df['LW'].astype(int)]
    return dff

def main():
    dd = special_missing_values()
    print(dd)

if __name__ == "__main__":
    main()

