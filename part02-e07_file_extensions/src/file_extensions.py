#!/usr/bin/env python3

def file_extensions(filename):
	moja = []
	mbili = {}
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			ss = line.split(".")
			if len(ss) == 1:
				moja.append(ss[0])
			else:
				ext = ss.pop()
				if ext in mbili:
					mbili[ext].append(line)
				else:
					tt = []
					tt.append(line)
					mbili[ext] = tt
	jj = moja, mbili
	# print(jj)
	return jj

def main():
	aah, brah = file_extensions("src/filenames.txt")
	print(f'{len(aah)} files with no extension')
	for k in brah:
		print(f"{k}\t{len(brah[k])}")
    
if __name__ == "__main__":
    main()
