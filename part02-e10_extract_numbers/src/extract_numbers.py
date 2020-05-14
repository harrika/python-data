#!/usr/bin/env python3

def extract_numbers(s):
	zz = []
	ss = s.split()
	for a in ss:
		try:
			n = int(a)			
		except ValueError:
			print(f'{a} not an int')
			try:
				n = float(a)
			except ValueError:
				print(f'{a} also not a float')
				continue
			else:
				zz.append(n)
		else:
			zz.append(n)		
	return zz

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
