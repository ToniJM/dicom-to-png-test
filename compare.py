import timeit
import multiprocess
import singleprocess
import matplotlib.pyplot as plt
import numpy as np

def main(iterations=2):
	mptimes = []
	sptimes = []
	r = np.arange(iterations)
	for i in r:
		mptimes.append(timeit.timeit(multiprocess.main, number=1))
		sptimes.append(timeit.timeit(singleprocess.main, number=1))
  
	X = np.arange(iterations)
	fig = plt.figure()
	ax = fig.add_subplot(111)
	# ax = fig.add_axes([0,0,1,1]) 
	ax.bar(X + 0.00, mptimes, color = 'b', width = 0.3)
	ax.bar(X + 0.3, sptimes, color = 'g', width = 0.3)
	ax.legend(labels=['Multiprocess', 'Single process'])
	plt.xticks([], [])
	plt.xlabel('Iterations')
	plt.ylabel('Seconds')
 
	plt.savefig('result.png')
 
if __name__ == "__main__": 
	main() 