#!/usr/bin/env python3

def sum_equation(L):
	ss = sum(L)
	if ss != 0:
		aa = list(map(lambda x:str(x), L))
		aa = ' + '.join([e for e in aa])
	else:
		aa = "0"
	aa = aa+" = "+str(ss)
	return aa

def main():
	aa = [22,33,44,51]
	# aa = []
	print(sum_equation(aa))

if __name__ == "__main__":
    main()
