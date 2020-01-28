# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:07:56 2020

@author: Admin
"""


import sys
from time import time
sys.path.append("W:/DATA SCIENTIST/ud120-projects-master/tools")
from email_preprocess import preprocess

import numpy as np
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='linear')

clf.fit(features_train,labels_train)
print("fitted")

pred = clf.predict(features_test)

print(accuracy_score(pred,labels_test))


# Reducing the training data

features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

print(accuracy_score(pred,labels_test))

# Changing the kernel function to RBF
C = [10, 100,1000,10000]
    
clf = SVC(kernel='rbf')

clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

print(accuracy_score(pred,labels_test))




# Changing various values of parameter C

for x in C:
    clf = SVC(kernel='rbf',C = x)
    
    clf.fit(features_train,labels_train)
    pred = clf.predict(features_test)
    acc = accuracy_score(pred,labels_test)
    print(f"For value of C = {x}, accuracy is {acc}")
    
    
    
    
    
# Now after optimization of C value. Checking the accuracy on the whole dataset.
    
clf = SVC(kernel='rbf',C = 10000)

clf.fit(features_train,labels_train)
print("fitted")

pred = clf.predict(features_test)

print(accuracy_score(pred,labels_test))

# Calculating the total number of prediction for a specific user.
print(np.count_nonzero(pred==1))

