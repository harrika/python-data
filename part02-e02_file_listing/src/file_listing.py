#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
	with open(filename, 'r') as f:
		master = []
		for line in f:
			tuplst = []
			print(line)
			sz = re.search(r'\s*(\d\d+)\s*', line).group(0)
			tuplst.append(int(sz))
			
			
			mnthp = re.search(r'\s+(\w\w\w)\s+\d+\s+\d\d:\d\d\s+\w*.\w*', line).group(0)
			mnthp = mnthp.strip()
			mnthpr =  mnthp.split()
			mnthpr[1] = int(mnthpr[1])
			tim = mnthpr[2].split(':')
			mnthpr[2] = int(tim[0])
			mnthpr.insert(3, int(tim[1]))
			tuplst.extend(mnthpr)
			
			tup = tuple(tuplst)
			master.append(tup)

		return master
    # return []

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
