import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

n = 1000 # sample size

ratio = 1 # set to 1 for circle
innerSemiMinor = 0.9
outerSemiMinor = 1.1

dataEllipse = np.random.random((n, 2)) # generates uninitialized points

m = 1 # naming images

while (ratio <= 20):
    ratio = round(ratio, 1) # makes the presentation look cleaner
    print(ratio) # debugging
    innerSemiMajor = innerSemiMinor * ratio # updates where points can be
    outerSemiMajor = outerSemiMinor * ratio 
    for i in range(1, n + 1): 
        x = np.random.uniform(-outerSemiMajor, outerSemiMajor)
        if np.random.randint(1, 3) == 1:# decides if the point goes above or below the x-axis
            coeff = 1
        else:
            coeff = -1
        # the following if-else statement places a random y coordinate and it makes sure it's in between the two ellipses
        if x <= innerSemiMajor and x >= -innerSemiMajor: #makes sure sqrt is positive
            y = coeff * np.random.uniform(innerSemiMinor * np.sqrt(1 - (x*x)/(innerSemiMajor*innerSemiMajor)), outerSemiMinor * np.sqrt(1 - (x*x)/(outerSemiMajor*outerSemiMajor)))
        else: #if the x coordinate is outside the range of the inner ellipse
            y = coeff * np.random.uniform(0, outerSemiMinor * np.sqrt(1 - (x*x)/(outerSemiMajor*outerSemiMajor)))
        dataEllipse[i - 1][0] = x
        dataEllipse[i - 1][1] = y

    plt.plot()
    plt.title("ratio = " + str(ratio))
    diagrams = ripser(dataEllipse)['dgms'] # Ripser plotting
    plot_diagrams(diagrams, plot_only=[1], xy_range=[0,2,0,2], show=False, lifetime=False)
    plt.savefig(str(m)) # when saving is finished, you can just create a new folder and put all the images in there, it should be in order so the gif making should be easy
    plt.clf()

    m += 1 # updates file name for the next image
    ratio += 0.1 # updating ratio for next iteration