#!/usr/bin/env python3

def main():
	aa = [(i,j) for i in range(1,7) for j in range(1,7) 
		if i+j == 5 ]
	for e in aa:
		print(e)
    
if __name__ == "__main__":
    main()
