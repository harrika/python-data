#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
	# print(a)
	x = a[:,0]
	y = a[:,1]
	y2 = x**3+x**2+6*x
	plt.subplot(1,2,1)	
	# plt.plot(x,y2)
	plt.plot(x,y)
	plt.title('Exs10: subfigures')
	plt.xlabel('the x axis')
	plt.ylabel('y: x^3+x^2+6x')

	colors = a[:,2]
	sizes = a[:,3]
	plt.subplot(1,2,2)
	plt.style.use('seaborn')
	plt.scatter(x,y, cmap='Greens', edgecolor='black',
				s = sizes, c = colors, alpha = 0.75, linewidth=1)
	plt.show()



def main():
	aa = np.random.randint(1,70, (14,4))
	subfigures(aa)


if __name__ == "__main__":
    main()
