import numpy as np
import matplotlib.pyplot as plt

# Custom Epanechnikov KDE class
class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None

    def fit(self, data):
        """Fit the KDE model with the given data."""
        self.data = np.array(data)  # shape (n_samples,dim=2)

    def epanechnikov_kernel(self, x, xi):
        """Epanechnikov kernel function."""
        if (np.linalg.norm(x - xi) / self.bandwidth) > 1:
            return 0
        return (2/np.pi) * (1 - np.linalg.norm(x - xi) ** 2 / self.bandwidth ** 2)

    
        
    def evaluate(self, x):
        """Evaluate the KDE at single point x."""
        if self.data is None:
            raise ValueError("Model not fitted yet.")
        return np.mean([(self.epanechnikov_kernel(x, xi)/(self.bandwidth)**2    ) for xi in self.data])
    
# Load the data from the NPZ file
data_file = np.load('transaction_data.npz')
data = data_file['data']

# TODO: Initialize the EpanechnikovKDE class
estimator = EpanechnikovKDE(bandwidth=1.0)

# TODO: Fit the data
estimator.fit(data)

# TODO: Plot the estimated density in a 3D plot
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        Z[i, j] = estimator.evaluate([X[i, j], Y[i, j]])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Density')
plt.title('Estimated Density Usign Epanechnikov KDE')

# TODO: Save the plot 
plt.savefig('transaction distribution.png')
