"""
2c
23b0932 Tejas Narendra Chaudhari
23b1064 Chaudhari Avinash Janardhan
23b0956 Siddhanth Mulkikar
"""
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

def sample(loc: float,scale: float) -> float:
    """
    Sample from the normal distribution with given loc and scale
    We have proved in the previous part that in order sample from the normal distribution using uniform distribution, we can use the inverse of the CDF of the normal distribution.
    stats.norm.ppf is the aproximation for the inverse of the CDF of the normal distribution (the exact inverse is not computable in closed form).
x    """
    x = np.random.rand();
    return stats.norm.ppf(x, loc=loc, scale=scale)

N = 10**5
# the sample function is called N times to generate N samples, and the samples are stored in the samples1, samples2, samples3, samples4 arrays. 

for i in range(N):
	if i == 0:
		samples1 = sample(0,math.sqrt(0.2))
	else:
		samples1 = np.append(samples1, sample(0,math.sqrt(0.2)))
plt.subplot(2,2,1)
plt.hist(samples1, bins=1000,  color='black', linewidth=1, edgecolor='blue', density=True)
plt.title('mean=0 and variance=0.2')

for i in range(N):
    if (i==0):
        samples2 = sample(0,math.sqrt(1))
    else:
        samples2 = np.append(samples2,sample(0,math.sqrt(1)))
plt.subplot(2,2,2)
plt.hist(samples2, bins=1000,  color='black', linewidth=1, edgecolor='blue', density=True)
plt.title('mean=0 and variance=1')

for i in range(N):
	if (i==0):
		samples3 = sample(0,math.sqrt(5))
	else:
		samples3 = np.append(samples3,sample(0,math.sqrt(5)))
plt.subplot(2,2,3)
plt.hist(samples3, bins=1000,  color='black', linewidth=1, edgecolor='blue', alpha=0.8, density=True)
plt.title('mean=0 and variance=5')
# plt.show()

for i in range(N):
	if (i==0):
		samples4 = sample(-2,math.sqrt(0.5))
	else:
		samples4 = np.append(samples4,sample(-2,math.sqrt(0.5)))
plt.subplot(2,2,4)
plt.hist(samples4, bins=1000,  color='black', linewidth=1, edgecolor='blue', alpha=0.8, density=True)
plt.title('mean=-2 and variance=0.5')
plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9, wspace=0.4,hspace=0.4)

plt.savefig('2c.png') 
# plt.show()


#plotting the histograms in the same plot
plt.clf()
plt.hist(samples3, bins=1300, color='green', linewidth=1, alpha=0.8, density=True, label='mean=0, variance=5', fill=True, histtype='stepfilled')
plt.hist(samples2, bins=1300, color='red', linewidth=1, alpha=0.8, density=True, label='mean=0, variance=1', fill=True, histtype='stepfilled')
plt.hist(samples4, bins=1300, color='blue', linewidth=1, alpha=0.8, density=True, label='mean=-2, variance=0.5', fill=True, histtype='stepfilled')
plt.hist(samples1, bins=1300, color='black', linewidth=1, alpha=0.8, density=True, label='mean=0, variance=0.2', fill= True, histtype='stepfilled')
plt.legend()
#restcit the x axis
plt.xlabel('x')
plt.ylabel('p(x)')
plt.xlim(-5,5)
plt.show()