from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

b = np.array( [[0,0],[1,0],[1,1],[0,1]])


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.add_patch(Polygon(b[0:4,:], fill=False, closed=True))
plt.axis([-1, 2, -1, 2])
plt.show()
