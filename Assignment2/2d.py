"""
2d
23b0932 Tejas Narendra Chaudhari
Avinash Chaudhari
Siddhanth Mulkikar
"""
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

def simulate_galton(h:int, N:int) -> np.ndarray:
	"""
 	Simulate the Galton board with N balls and h rows
	Here we use np.random.choice to generate the decision for the ball at each level. 
	If the decision is -1, the ball goes left, if it is 1, the ball goes right.
	We sum the decisions at each level to get the final bin number.
 	The return shape will be (N,)
  	"""
	return random.choice([-1,1], size=(N,h)).sum(axis=1) 

N = 10**5

h = 10
bins = np.arange(-h,h+1)
plt.hist(simulate_galton(h, N), bins=bins, alpha=0.5, label='h=10')
# plt.savefig('2d1.png')
# plt.clf()

h = 50
bins = np.arange(-h,h+1)
plt.hist(simulate_galton(h, N), bins=bins, alpha=0.5, label='h=50')
# plt.savefig('2d2.png')
plt.plot()
# plt.clf()

h = 100
bins = np.arange(-h,h+1)
plt.hist(simulate_galton(h, N), bins=bins, alpha=0.5, label='h=100')
# plt.savefig('2d3.png')
plt.plot()
# plt.clf()

