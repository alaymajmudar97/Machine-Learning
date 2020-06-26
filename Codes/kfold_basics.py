# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:12:30 2020

@author: Admin
"""

from numpy import array
from sklearn.model_selection import KFold
data = [0.1,0.2,0.3,.4,.5,.6]


data = array(data)

kfold = KFold(3,True,1)

for train, test in kfold.split(data):
    print('train: %s, test: %s' % (data[train], data[test]))
