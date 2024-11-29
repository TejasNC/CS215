"""
2d
23b0932 Tejas Narendra Chaudhari
23b1064 Chaudhari Avinash Janardhan
23b0956 Siddhanth Mulkikar
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
bins = np.arange(-h/2,h/2+2)
counts, bins, patches = plt.hist(simulate_galton(h,N)/2 , bins=bins, color='black', linewidth=1, edgecolor='blue', align='left')
for patch in patches:
    patch.set_width(0.9 * patch.get_width())
plt.savefig('2d1.png')
plt.clf()

h = 50
bins = np.arange(-h/2,h/2+2)
counts, bins, patches = plt.hist(simulate_galton(h,N)/2 , bins=bins, color='black', linewidth=1, edgecolor='blue', align='left')
for patch in patches:
    patch.set_width(0.7 * patch.get_width())
plt.savefig('2d2.png')
plt.clf()

h = 100
bins = np.arange(-h/2,h/2+2)
counts, bins, patches = plt.hist(simulate_galton(h,N)/2 , bins=bins, color='black', linewidth=1, edgecolor='blue', align='left')
for patch in patches:
    patch.set_width(0.6 * patch.get_width())
plt.savefig('2d3.png')
plt.clf()

