import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

n = 1000 # sample size

ratio = 10 # set to 1 for circle
innerSemiMinor = 0.9
outerSemiMinor = 1.1

innerSemiMajor = innerSemiMinor * ratio
outerSemiMajor = outerSemiMinor * ratio


dataEllipse = np.random.random((n, 2)) # generates uninitialized points
xEllipse = np.random.random((n, 1)) # same as dataEllipse but in 1D arrays for matlab to plot
yEllipse = np.random.random((n, 1))

for i in range(1, n + 1): 
    x = np.random.uniform(-outerSemiMajor, outerSemiMajor) # places x coordinate randomly
    if np.random.randint(1, 3) == 1:# decides if the point goes above or below the x-axis
        coeff = 1
    else:
        coeff = -1
    # the following if-else statement places a random y coordinate and it makes sure it's in between the two ellipses
    if x <= innerSemiMajor and x >= -innerSemiMajor: # makes sure sqrt is positive
        y = coeff * np.random.uniform(innerSemiMinor * np.sqrt(1 - (x*x)/(innerSemiMajor*innerSemiMajor)), outerSemiMinor * np.sqrt(1 - (x*x)/(outerSemiMajor*outerSemiMajor)))
    else: #if the x coordinate is outside the range of the inner ellipse
        y = coeff * np.random.uniform(0, outerSemiMinor * np.sqrt(1 - (x*x)/(outerSemiMajor*outerSemiMajor)))
    dataEllipse[i - 1][0] = x
    dataEllipse[i - 1][1] = y
    xEllipse[i - 1] = x
    yEllipse[i - 1] = y

plt.plot(xEllipse, yEllipse, 'o') # MatLab plotting
ax = plt.gca()
ax.set_aspect('equal')
plt.show()


diagrams = ripser(dataEllipse)['dgms'] # Ripser plotting
plot_diagrams(diagrams, show=True, lifetime=False) # you can toggle lifetime
