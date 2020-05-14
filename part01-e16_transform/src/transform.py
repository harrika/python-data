#!/usr/bin/env python3
def transform(s1, s2):
	sl1 = list(map(int, s1.split()))
	sl2 = list(map(int, s2.split()))
	return list(map(lambda x: x[0] * x[1], zip(sl1, sl2)))

def main():
	aa = '22 33 44'
	bb = '122 133 144'
	print(transform(aa, bb))

if __name__ == "__main__":
    main()
