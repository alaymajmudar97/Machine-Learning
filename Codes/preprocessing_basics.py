# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:59:10 2020

@author: Admin
"""

import numpy as np
from sklearn.preprocessing import OrdinalEncoder

data = np.asarray([['red'],['green'],['blue']])
data.shape
enc = OrdinalEncoder()
res = enc.fit_transform(data)
res
