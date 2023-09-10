import matplotlib.pyplot as plt
fig,ax = plt.subplots()
plt.style.use('seaborn')
x_values = range(1,10)
y_values = [x**3 for x in x_values]
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,s= 100)
ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel('Values', fontsize = 10)
ax.set_ylabel('Cube Of Values', fontsize = 14)
ax.axis([0,10,0,1000])
plt.show()


