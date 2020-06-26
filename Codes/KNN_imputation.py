# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:08:15 2020

@author: Admin
"""

# Using Simple KNN for imputation on Horse Colic Dataset

import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.pipeline import Pipeline
from matplotlib import pyplot

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/horse-colic.csv'
df = pd.read_csv(url, header=None, na_values='?')
    
df.head()

(df.isnull().sum())/df.shape[0]*100
df.isnull()
np.sum(df.isnull(),axis=1)/df.shape[0]*100
df[2]

df_values = df.values
X,y = df_values[:,:-1],df_values[:,-1]
print('Missing: %d' % sum(np.isnan(X).flatten()))

knn_impute= KNNImputer(n_neighbors = 5, weights = 'uniform', metric = 'nan_euclidean')

knn_impute.fit(X)    
strategies = [str(i) for i in [1,3,5,7,9,15,21,40]]
results = list()

X_transform = knn_impute.transform(X) 
print('Missing: %d' % sum(np.isnan(X_transform).flatten()))

model = RandomForestClassifier()

for s in strategies:
    pipeline = Pipeline(steps=[('i',KNNImputer(n_neighbors=int(s))),('m',model)])
    
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    
    scores = cross_val_score(pipeline, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    results.append(scores)
    
    
    print('Mean Accuracy: %.3f (%.3f)' % (np.mean(scores), np.std(scores)))
    
pyplot.boxplot(results, labels = strategies,showmeans= True)
pyplot.xticks(rotation=45)
pyplot.show()
pipeline = Pipeline(steps=[('i',KNNImputer(n_neighbors=42)),('m',model)])

pipeline.fit(X, y)
     # define new data
row = [2,1,530101,38.50,66,28,3,3,np.nan,2,5,4,4,np.nan,np.nan,np.nan,3,5,45.00,8.40,np.nan,np.nan,2,2,11300,00000,00000]
# make a prediction
yhat = pipeline.predict([row])
# summarize prediction
print('Predicted Class: %d' % yhat[0])
