#!/usr/bin/env python3
import math
import sys

def summary(filename):
	with open(filename, 'r') as f:
		mray = []
		for line in f:
			try:
				ee = float(line)
			except ValueError:
				ee = -999999
			if ee != -999999:
				mray.append(ee)
		sm  = sum(mray)
		ll = len(mray)
		avg = sm/ll
		devsum = 0
		for e in mray:
			dev = (e-avg)**2
			devsum += dev
		sd = math.sqrt(devsum/(ll-1))
		tupo = sm, avg, sd
	return tupo

def main():	
	ss = sys.argv[1:]
	for qq in ss:
		sm, av, sd = summary(qq)
		print(f"File: {qq} Sum: {sm :.6f} Average: {av :.6f} Stddev: {sd :.6f}")


if __name__ == "__main__":
    main()
