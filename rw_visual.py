import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk

rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig,ax = plt.subplots()

# to color the points according to their numbers we will store them in a list
point_numbers = range(rw.num_points)

# we will assign the list to variable c and to remove the outline,
# we will pass none to edge colors so that ponts are cleare.
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
plt.show()



