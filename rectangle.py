# this program uses greedy permutation

import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

n = 500 # sample size divided by 4, n for each side

ratio = 1 # 1 for square
height = 1 # half a height
width = ratio * height # half a width

border = 0.1

dataRectangle = np.random.random((4 * n, 2))
xRectangle = np.random.random((4 * n, 1))
yRectangle = np.random.random((4 * n, 1))

for i in range(1, n + 1): # left side
    dataRectangle[i-1][0] = np.random.uniform(-width - border, -width + border)
    xRectangle[i-1] = dataRectangle[i-1][0]
    dataRectangle[i-1][1] = np.random.uniform(-height, height)
    yRectangle[i-1] = dataRectangle[i-1][1]

for i in range(n + 1, 2 * n + 1): # right side
    dataRectangle[i-1][0] = np.random.uniform(width - border, width + border)
    xRectangle[i-1] = dataRectangle[i-1][0]
    dataRectangle[i-1][1] = np.random.uniform(-height, height)
    yRectangle[i-1] = dataRectangle[i-1][1]

for i in range(2 * n + 1, 3 * n + 1): # down side
    dataRectangle[i-1][1] = np.random.uniform(-height - border, -height + border)
    yRectangle[i-1] = dataRectangle[i-1][1]
    dataRectangle[i-1][0] = np.random.uniform(-width, width)
    xRectangle[i-1] = dataRectangle[i-1][0]

for i in range(3 * n + 1, 4 * n + 1): # up side
    dataRectangle[i-1][1] = np.random.uniform(height - border, height + border)
    yRectangle[i-1] = dataRectangle[i-1][1]
    dataRectangle[i-1][0] = np.random.uniform(-width, width)
    xRectangle[i-1] = dataRectangle[i-1][0]

diagrams = ripser(dataRectangle)['dgms'] # Ripser plotting
res = ripser(dataRectangle, n_perm=round(4 * n / 5)) # greedy permutation
subdiagrams = res['dgms']

plt.plot(xRectangle, yRectangle, 'o') # MatLab plotting
ax = plt.gca()
ax.set_aspect('equal')
plt.show()

# testing Ripser plots for sample and subsample

plt.subplot(121)
plot_diagrams(diagrams, lifetime=False) # you can toggle lifetime
plt.subplot(122)
plot_diagrams(subdiagrams, lifetime=False)
plt.show()