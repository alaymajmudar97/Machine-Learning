# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:41:27 2020

@author: Admin
"""

# This code implements Gaussian Naive Bayes formula. 
# First Few lines of code is the example from SKLearn documentation page.


import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2]) 
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-0.8,-1]]))
