#!/usr/bin/env python3

class Prepend(object):
    def __init__(self, para1):
    	self.start = para1

    def write(self, para2):
    	print(self.start+para2)




def main():
    p = Prepend('just saying')
    p.write('hello')

if __name__ == "__main__":
    main()
