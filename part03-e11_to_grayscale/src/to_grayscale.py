#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def to_grayscale(imej):
	picha = plt.imread(imej)
	x,y = picha.shape[:2]
	gpicha = np.empty([x,y])
	aa = picha[:,:,0] * 0.2126
	bb = picha[:,:,1] * 0.7152
	cc = picha[:,:,2] * 0.0722
	gpicha[:] = aa+bb+cc
	return gpicha
	

def main():
	mm = to_grayscale('src/painting.png')
	# plt.figure(figsize=(11,11))
	plt.imshow(mm, cmap='gray')
	

if __name__ == "__main__":
    main()

