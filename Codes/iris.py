# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:44:52 2020

@author: Admin
"""

# plotting for exploratory data analysis
# understanding about the dataset. 

# Iris Dataset
# https://en.wikipedia.org/wiki/Iris_flower_data_set
# Simple dataset to learn basics
# Importance of Domain Knowledge
# Objective is to classify a new flower based on some features
# sepal and Petal are the features
# Why not color??
#EDA

#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 




#import the data
iris = pd.read_csv("W:/DATA SCIENTIST/Machine-Learning/Codes/Datasets/iris dataset/iris.csv")


#Some info about the dataset

print(iris.shape)

print(iris.columns)

print(iris.describe())


# How many datapoints for each species??
#Balanced vs unbalaced dataset
print(iris['species'].value_counts())



# 2d scatter plot  - But here we can see just the range of values and not species.
iris.plot(kind = 'scatter',x ='sepal_length', y ='sepal_width')


# 2d plot with color coding.

sns.set_style('whitegrid')
sns.FacetGrid( iris, hue="species",size = 4 ).map(plt.scatter,"sepal_length","sepal_width").add_legend()
plt.show()


#what are some observations?
# Using sepal_length and sepal_width we can differentiate 'SETOSA' from other species 


#Pair plot 
#Some disadvantages - Cannot be used when features are high 

plt.close()
sns.set_style("whitegrid")
sns.pairplot(iris, hue = 'species',size = 8)
plt.show()



#for plotting single varible we use histogram
#pdf = smoothed histogram (KDE)
sns.set_style("whitegrid"   )
sns.FacetGrid(iris,hue='species',size=8).map(sns.distplot,"petal_length").add_legend()



#univariate analysis - One variable analysis
# Need for Cumulative Distribution Function CDF
# We can visually see what percentage of versicolor flowers have a petal_length more than 1.6


iris_setosa = iris[iris['species']=='setosa']
counts, bin_edges  = np.histogram(iris_setosa['petal_length'],bins=10,density= True)

pdf = counts/sum(counts)
print(pdf)
print(bin_edges)


#compute CDF
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)



iris_versicolor = iris[iris['species']=='versicolor']
counts, bin_edges  = np.histogram(iris_versicolor['petal_length'],bins=10,density= True)

pdf = counts/sum(counts)
print(pdf)
print(bin_edges)


#compute CDF
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)



iris_virginica = iris[iris['species']=='virginica']
counts, bin_edges  = np.histogram(iris_virginica['petal_length'],bins=10,density= True)

pdf = counts/sum(counts)
print(pdf)
print(bin_edges)


#compute CDF
cdf = np.cumsum(pdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:],cdf)


plt.show()


sns.boxplot(x='species',y='petal_length', data = iris)
plt.show()


sns.violinplot(x='species',y='petal_length', data = iris,size=8)
plt.show()


# 2d density plot, contoursplot

sns.jointplot(x="petal_length",  y='petal_width', data=iris_setosa,kind ='kde')