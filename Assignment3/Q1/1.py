# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Only take the first 1500 rows
first1500 = df.head(1500)

# Take the rows with D < 4
df_filtered = first1500[first1500['D (Mpc)'] < 4]

def bin_count(h : float, data: np.array):
	bin_edges = np.arange(min(data), max(data) + h, h)
	counts, bin_edges = np.histogram(data, bins=bin_edges)
	return counts

# The histogram with just 10 bins
plt.hist(df_filtered['D (Mpc)'], bins=10)

data = np.array(df_filtered['D (Mpc)'])
probs = bin_count((max(data) - min(data))/10, data)/len(data)
print('The estimated probabilities for each bin are:')
for i in range(10):
	print('Bin', i, '[', round(min(data) + i*((max(data) - min(data))/10), 2), ',', round(min(data) + (i+1)*((max(data) - min(data))/10), 2), ')', ':', round(probs[i], 4))

plt.savefig('10binhistogram.png')

print('The 10 bin histogram looks oversmoothed')
print('10binhistogram.png has been saved')

plt.show()

# Return the frequency in each bin


# Calculate the loss for each number of bins from 1 to 1000
# data = np.array(df_filtered['D (Mpc)'])
n = len(data)
loss = np.array([])
for i in range(1, 1001):
	h = (max(data) - min(data))/i
	hist = bin_count(h, data)
	hist_sum_square = np.sum(np.square(np.divide(hist, n)))
	term1 = 2 / ((n - 1) * h)
	term2 = (n + 1) / ((n - 1) * h) * hist_sum_square
	loss_i = term1 - term2
	loss = np.append(loss, loss_i)

# Find the optimal number of bins
optimal_bins = np.argmin(loss) + 1
print('Optimal number of bins:', optimal_bins)
print('Optimal bandwidth:', (max(data) - min(data))/optimal_bins)

plt.plot(range(1, 1001), loss)
plt.savefig('crossvalidation.png')
print('crossvalidation.png has been saved')
plt.show()

# Plot the histogram with the optimal number of bins
plt.hist(df_filtered['D (Mpc)'], bins=optimal_bins)
plt.savefig('optimalhistogram.png')
print('optimalhistogram.png has been saved')

plt.show()