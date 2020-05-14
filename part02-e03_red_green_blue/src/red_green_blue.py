#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
	malist = []
	with open(filename, 'r') as f:
		next(f)
		for line in f:
			ln = line.strip()
			bb = re.search("^.*\t", ln).group(0)
			bbs = bb.split()
			bbs2 = '-'.join(bbs)
			ln = re.sub("^.*\t", bbs2+'-', ln)
			ln = re.sub('-', '\t', ln)

			malist.append(ln)
	return malist


def main():
	print(red_green_blue())

if __name__ == "__main__":
    main()
