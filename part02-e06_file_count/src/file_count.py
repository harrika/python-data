#!/usr/bin/env python3

import sys

def file_count(filename):
	lns = 0
	wrds = 0
	cars = 0
	with open(filename, 'r') as f:
		for line in f:
			lns += 1
			words = line.split()
			wrds += len(words)
			for c in line:
				cars += 1
				
			# for w in words:
			# 	cars += len(w)

	return lns, wrds, cars

def main():
	ss = sys.argv[1:]
	for q in ss:
		l, w, c = file_count(q)
		print(f"{l}\t{w}\t{c}\t{q}")

if __name__ == "__main__":
    main()
