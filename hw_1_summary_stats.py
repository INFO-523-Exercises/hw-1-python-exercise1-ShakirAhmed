# -*- coding: utf-8 -*-
"""Hw-1-Summary stats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OFIWgrYUtaANLBNRkeX-e39vkzPfJ06l

-------------------
####Title: Exercise 1: INFO 523- Data Mining- Summary stats
####Author: Shakir Ahmed
####Date: 2023-09-13 (YYYY_MM_DD)
-------------------

##Downloading and initializing data

###3.1 Summary Statitics

####1. Importing IRIS dataset
"""

import pandas as pd
#read.csv used to read the Iris dataset
data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',header=None)
data.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

data.head()

"""####2. Calculating average, std deviation"""

from pandas.api.types import is_numeric_dtype
#Displaying the mean, std deviation, max and min for each parameter
for col in data.columns:
    if is_numeric_dtype(data[col]):
        print('%s:' % (col))
        print('\t Mean = %.2f' % data[col].mean())
        print('\t Standard deviation = %.2f' % data[col].std())
        print('\t Minimum = %.2f' % data[col].min())
        print('\t Maximum = %.2f' % data[col].max())

"""####3. Counting the frequency for each distinct value"""

#Counting the number of distinct values
data['class'].value_counts()

"""####4. Summarizing all the attributes"""

data.describe(include='all')

"""####5. Computing covariance and correlation"""

print('Covariance:')
data.cov()

print('Correlation:')
data.corr()

"""###3.2 Data Visualization

1. Histogram:
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

data['sepal length'].hist(bins=8)

"""####2. Boxplot"""

data.boxplot()

"""3. Scatter plot:"""

#Importing libs necessary for scatter plot
import matplotlib.pyplot as plt

#Code to plot the scatter plot
fig, axes = plt.subplots(3, 2, figsize=(12,12)) #Dividing plot area into 3x2 areas
index = 0
for i in range(3):              #Nested for loop for the plot
    for j in range(i+1,4):
        ax1 = int(index/2)
        ax2 = index % 2
        axes[ax1][ax2].scatter(data[data.columns[i]], data[data.columns[j]], color='orange')
        axes[ax1][ax2].set_xlabel(data.columns[i])
        axes[ax1][ax2].set_ylabel(data.columns[j])
        index = index + 1

"""####4. Parallel Coordinates:"""

# Commented out IPython magic to ensure Python compatibility.
from pandas.plotting import parallel_coordinates
# %matplotlib inline

parallel_coordinates(data, 'class')

"""##3.3 Summary:

1. Documentation on Pandas. https://pandas.pydata.org/
2. Documentation on matplotlib. https://matplotlib.org/
3. Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
"""