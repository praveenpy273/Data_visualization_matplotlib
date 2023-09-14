import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk

rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')

# figsize parameter takes tuple, which tells Matplotlib of the plotting window
# using figsize so that plot fills the screen
fig,ax = plt.subplots(figsize =(15,9))

# to color the points according to their numbers we will store them in a list


#for molecule path removed ax.scatter with ax.plot, also removed list to store points
ax.plot(rw.x_values, rw.y_values, linewidth=3)

# resizing first and last points.
ax.scatter(rw.x_values[0], rw.y_values[0], c ='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Removing the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()



