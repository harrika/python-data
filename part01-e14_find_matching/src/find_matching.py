#!/usr/bin/env python3

def find_matching(L, pattern):
	lst = []
	for i, k in enumerate(L):
		if pattern  in k:
			lst.append(i)

	return lst

def main():
	aa = ['mwana', 'mukagwa', 'anan']
	oo = find_matching(aa,'an')
	print(oo)

if __name__ == "__main__":
    main()
