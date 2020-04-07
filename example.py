from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

# Number of independent experiments in each trial
n = 50
# Probability of success for each experiment
p = 0.1
fig, ax = plt.subplots(1, 1)
x = range(0,50)
ax.plot(x, binom.pmf(x, n, p), 'ro', label='actual binomial distribution')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='r', lw=5, alpha=0.5)
plt.legend()
plt.show()
