# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 08:41:16 2020

@author: Admin
"""

#In this project, we will use regression to predict financial data for Enron employees and associates. 
#Once we know some financial data about an employee, like their salary, what would we predict for the size of their bonus?




#!/usr/bin/python

"""
    starter code for the regression mini-project
    
    loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project)

    draws a little scatterplot of the training/testing data

    you fill in the regression code where indicated

"""    


import sys
import pickle

enron_data = pickle.load(open("W:/DATA SCIENTIST/ud120-projects-master/final_project/final_project_dataset_modified.pkl", "rb"))


from feature_format import featureFormat, targetFeatureSplit

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
data = featureFormat( enron_data, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "b"
test_color = "r"



### regression goes here!
from sklearn.linear_model import LinearRegression
reg= LinearRegression().fit(feature_train,target_train)
print(reg.coef_)
print(reg.intercept_)
print(reg.score(feature_train,target_train))

print(reg.score(feature_test,target_test))





### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
