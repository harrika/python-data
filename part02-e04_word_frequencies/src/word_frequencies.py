#!/usr/bin/env python3

def word_frequencies(filename):
	words = {}
	with open(filename, 'r') as f:
		for line in f:
			lnray = line.split()
			for wd in lnray:
				wad = wd.strip("""!"#$%&'()*, -./:;?@[]_""")
				if wad in words:
					words[wad] = words[wad] + 1
				else:
					words[wad] = 1
	for e in words:
		print(f"{e}\t{words[e]}")
	return words

def main():
	word_frequencies('src/alice.txt')
	

if __name__ == "__main__":
    main()
