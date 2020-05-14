#!/usr/bin/env python3

def posv(x):
	return x>0

def positive_list(L):
	return list(filter(posv, L))

def main():
    aa = [2,-2,0,-14,23,2,-10]
    print(positive_list(aa))

if __name__ == "__main__":
    main()
