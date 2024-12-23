import matplotlib.pyplot as plt

#Data for plotting
x = [1,2,3,4,5]
y = [1,4,9,16,25]

#Creating the plot
plt.plot(x,y)

#Adding title and labels
plt.title('Line Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#Display the plot
plt.show()

#Data for Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [3,7,2,5]
#Create a bar chart
plt.bar(categories, values)
#Adding titles and labels
plt.title('Bar Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
#Display
plt.show()

#Scatter Plot
x = [1,2,3,4,5]
y = [5,4,3,2,1]
#Create a scatter plot
#plt.scatter(x,y)
# Adding title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the plot
plt.show()

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [5, 4, 3, 2, 1]

#Create Subplots
fig, (ax1,ax2) = plt.subplots(1,2)
ax1.plot(x,y1)
ax1.set_title('Line Plot')

ax2.scatter(x, y2)
ax2.set_title('Scatter Plot')

plt.tight_layout()  # Adjusts the layout so plots don't overlap
plt.show()

plt.plot(x,y1, label='Square', color='blue', linestyle='--')
plt.plot(x,y2, label='Linear', color='red', linestyle= '-')
plt.legend()
plt.grid(True)
plt.title('Advanced Customization Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
plt.figure(figsize=(8,5),dpi=100)
plt.annotate('Highest Point', xy=(5,25), xytext=(3,20), arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.title('Annotation Example')

import numpy as np
data = np.random.randn(1000)
plt.hist(data,bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Data for pie chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [15, 30, 45, 10]
colors = ['red', 'yellow', 'pink', 'brown']
explode = (0, 0.1, 0, 0)  # Highlight the second slice

# Plot pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%')
plt.title('Pie Chart Example')
plt.show()

# Data
data = [7, 8, 5, 6, 9, 10, 7, 8, 9, 4, 10, 12]

# Plot box plot
plt.boxplot(data)

plt.title('Box Plot Example')
plt.ylabel('Values')
plt.show()

# Data for plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, ax = plt.subplots(2, 1, figsize=(8, 6))  # Two rows, one column

# Plot on each subplot
ax[0].plot(x, y1, color='blue')
ax[0].set_title('Sine Wave')

ax[1].plot(x, y2, color='orange')
ax[1].set_title('Cosine Wave')

plt.tight_layout()
plt.show()


#Exercise 
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)
plt.show()

