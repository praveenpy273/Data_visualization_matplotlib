import matplotlib.pyplot as plt


x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
flg,ax = plt.subplots()
ax.scatter(x_values,y_values,s=10)
# ax.plot(input_values,squares,linewidth= 2)

#Set chart title and label axes.
ax.set_title('Square Numbers', fontsize = 14)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Value', fontsize = 14)

# Set size of tick_labels
ax.tick_params(axis = 'both', labelsize = 14)
ax.axis([0,1100, 0,1100000]) 
'''axis method is used to specify range of each axis, it takes 4 points, 
2 for x axis and 2 for y-axisx-axis: 0,1100, y-axis 0, 1100000'''
plt.show()