from decimal import Decimal
import math
import matplotlib.pyplot as plt
import numpy as np

def nPr(n, r):
    return math.factorial(n) // math.factorial(n - r) 

P_i = np.zeros(200)

for i in range(2, 202):
    p = Decimal(nPr(200, i-1)) * (i-1) / Decimal(200**i)
    P_i[i-2] = p

max_P_i = max(P_i)
max_pos = np.argmax(P_i) + 2
print("Maximum chance of receiving a free trade is at position",max_pos,"with a probability of", max_P_i)

plt.scatter(range(2, 202), P_i)
plt.xlabel('i',fontsize=15)
plt.ylabel('P_i',fontsize=15)
plt.title('Probability of receiving a free trade',fontsize=15)

plt.axvline(x=max_pos, color='red', linestyle='--')

# set x ticks at all positions divisible by 5
plt.xticks(np.arange(0, 202, 5))

plt.show()

