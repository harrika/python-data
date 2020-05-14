#!/usr/bin/env python3
import re

def integers_in_brackets(s):
	ss = re.findall(r'\[s*\t?[+-]?\d+\s*\]',s)
	gg = []
	for a in ss:
		gg.append(re.search(r'[-]?\d+', a).group(0))
	# print(gg)
	# ss2 = map(int, gg)
	ss2 = [int(x) for x in gg]
	# return list(ss2)	
	return ss2


def main():
	# s = "afd [asd] [12 ] [a34] [a     +-43 ]tt [+12]xxx!"
	s = "afd [asd] [12 ] [a34] [	-43 ]tt [+12]xxx!"
	print(s)
	print(integers_in_brackets(s))


if __name__ == "__main__":
    main()

