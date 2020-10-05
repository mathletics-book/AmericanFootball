from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt
import numpy as np

locations = np.array([[89.13,31.65],
                        [86.32,26.70],
                        [90.03,28.61],
                        [87.83,31.59],
                        [88.77,28.45],
                        [87.52,27.26]])

# calculate the convex hull
ol_hull = ConvexHull(locations)

print("The area of the OL convex hull is: ", ol_hull.area)


# plot the data

plt.xlim((0,100))
plt.ylim((0,60))
plt.plot(locations[:,0],locations[:,1], 'o')

for simplex in hull.simplices:
        plt.plot(locations[simplex, 0], locations[simplex, 1], 'k-')

plt.plot(locations[hull.vertices,0], locations[hull.vertices,1], 'r--', lw=2)
plt.plot(locations[hull.vertices[0],0], locations[hull.vertices[0],1], 'ro')
plt.show()
