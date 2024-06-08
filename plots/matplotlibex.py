# Matplotlib
#Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK+.
#
#
# Some of the major Pros of Matplotlib are:

#     Generally easy to get started for simple plots
#     Support for custom labels and texts
#     Great control of every element in a figure
#     High-quality output in many formats
#     Very customizable in general

import matplotlib.pyplot as plt
import numpy as np

# simple example
x = np.arange(0,10)
y = np.arange(11,21)
# scatter plot
plt.scatter(x,y,c='b')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph in 2D')
plt.savefig('1.png')
plt.show()

y = x*x    # some change to y axis value
plt.plot(x,y,'r*',linestyle='dashed',linewidth=2,markersize=12)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('2D diagram')
plt.show()

## Creating subplots
plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')
plt.show()

x = np.arange(1,11)
y = 3 * x + 5
plt.plot(x,y)
plt.title('Demo Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()

# Compute x and y coordinate for points on a sine wave
x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.title('Sine wave')
plt.show()

# Subplot()
# sine and cosine curves
x = np.arange(0,5*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y_sin,'r--')
plt.title('Sine Wave')

plt.subplot(2,1,2)
plt.plot(x,y_cos,'g--')
plt.title('Cosine wave')

plt.show()

# Bar plot
x = [2,8,10]
y = [11,16,9]

x2 = [3,9,11]
y2 = [6,15,7]
plt.bar(x,y)
plt.bar(x2,y2,color='g')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X label')
plt.show()

# Histograms
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a)
plt.title('histogram')
plt.show()

# Box plot
data = [np.random.normal(0,std,100) for std in range(1,4)]
print(data)
plt.boxplot(data,vert=True,patch_artist=False)
plt.show()

# Pie Chart
# Data 
labels = 'Python','Java','C','C++'
sizes = [245,215,130,210]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode = (0.4,0,0,0)  # explode first slice

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=False)
plt.axis('equal')
plt.show()