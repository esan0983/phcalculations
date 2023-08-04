# this program uses greedy permutation

import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

n = 1000 # sample size divided by 4, n for each side

ratio = 1 # 1 for square
height = 1 # half a height
width = ratio * height # half a width

border = 0.1

dataRectangle = np.random.random((4 * n, 2))

m = 1 #naming images

while (ratio <= 10):
    ratio = round(ratio, 2)
    print(ratio) #debugging
    width = ratio * height
    for i in range(1, n + 1): # left side
        dataRectangle[i-1][0] = np.random.uniform(-width - border, -width + border)
        dataRectangle[i-1][1] = np.random.uniform(-height, height)

    for i in range(n + 1, 2 * n + 1): # right side
        dataRectangle[i-1][0] = np.random.uniform(width - border, width + border)
        dataRectangle[i-1][1] = np.random.uniform(-height, height)

    for i in range(2 * n + 1, 3 * n + 1): # down side
        dataRectangle[i-1][1] = np.random.uniform(-height - border, -height + border)
        dataRectangle[i-1][0] = np.random.uniform(-width, width)

    for i in range(3 * n + 1, 4 * n + 1): # up side
        dataRectangle[i-1][1] = np.random.uniform(height - border, height + border)
        dataRectangle[i-1][0] = np.random.uniform(-width, width)

    diagrams = ripser(dataRectangle, n_perm=round(4 * n / 5))['dgms'] # Ripser plotting with greedy permutation

    plt.plot()
    plt.title("ratio = " + str(ratio))
    plot_diagrams(diagrams, plot_only=[1], xy_range=[0,2.1,0,2.1], show=False, lifetime=False)
    plt.savefig(str(m)) # when saving is finished, you can just create a new folder and put all the images in there, it should be in order so the gif making should be easy

    m += 1 # updates file name for next image
    ratio += 0.05 #updates ratio 