import matplotlib.pyplot as plt
import numpy as np
import random

xvals = []
yvals = []
freq = 20
count = 1
val = 1

while len(xvals) < freq:
    xvals.append(val)
    val+=1
while len(yvals) < freq:
    val = random.randint(10,20)
    yvals.append(val)
xvals.sort()
print(xvals)
print(yvals)

plt.ylim(0,90)
plt.xlim(xvals[0],xvals[len(xvals)-1])

while count < len(xvals):
    x = np.arange(xvals[count-1],xvals[count],.01)
    function = np.minimum(np.maximum((x - xvals[count-1])/(xvals[count]-xvals[count-1]),0),1)
    y = ((yvals[count] - yvals[count-1]) * function**2 * (3-(2*function))) + yvals[count-1]
    count+=1
    plt.plot(x, y, c='black')
plt.axis(False)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.show()
