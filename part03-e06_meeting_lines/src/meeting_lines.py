#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
	# y = a1x + b1
	# y - a2x + b2
	
	# -a1x + y = b1
	# -a2x + y = b2

	# -a1  1 		x 	b1
	# -a2  1		y	b2	
	A = np.array([[-a1,1],[-a2,1]])	
	b = np.array([b1,b2])
	# x,y = np.linalg.solve(A,b)
	return np.linalg.solve(A,b)

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
