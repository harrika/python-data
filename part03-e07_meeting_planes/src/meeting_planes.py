#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # z=a1y+b1x+c1
    # z=a2y+b2x+c2
    # z=a3y+b3x+c3

    # a1 b1 -1  y   -c1
    # a2 b2 -1  x   -c2
    # a3 b3 -1  z   -c3

    # aa = np.array([[a1,b1,-1], [a2,b2,-1], [a3,b3,-1]])
    aa = np.array([[b1,a1,-1], [b2,a2,-1], [b3,a3,-1]])
    cc = np.array([-c1,-c2,-c3])
    return np.linalg.solve(aa,cc)

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
