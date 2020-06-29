# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:59:10 2020

@author: Admin
"""

import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
abspath= os.path.abspath('W:/DATA SCIENTIST/Machine-Learning/Codes/Datasets/Chrosnic Kidney Disease') 
os.chdir(abspath)

df = pd.read_csv('./datasets_1111_2005_kidney_disease.csv')

df.head(10)

df
df.loc[1,'id']
df.groupby(by=df.dtypes.values).count()
# ratio of null values in each column
(np.sum(df.isnull())/df.shape[0])*100
df.dtypes
df.describe()


cp_df = df.copy()
impt = SimpleImputer()
cat_impt =SimpleImputer(missing_values = np.nan, strategy='most_frequent')
cp_df.to_numpy()
cp_array = cp_df.values





# Using most_freq as strategy. Applies on the whole dataset

X = cat_impt.fit_transform(cp_df.values)
cp_df
cp_df = cp_df.apply(lambda col:cat_impt.fit_transform(col))
cp_df[df.columns] = cp_df[df.columns].apply(lambda col:cat_impt.fit_transform(col)) 


categorical_columns= df.columns[df.dtypes==object].tolist()

num_df = df.select_dtypes(exclude=['object'])

df_categorical = df[categorical_columns]


#No of NAN values in numerical columns
(np.isnan(num_df.values.flatten())).sum()

array_after_impute_numerical = impt.fit_transform(num_df)

array_after_impute_numerical.shape


#imputing categorical variables
array_impt_cat = cat_impt.fit_transform(df_categorical.values)
np.isnan(array_impt_cat)


label_encoder = LabelEncoder()
a = pd.DataFrame(['hot','cold',np.nan])

label_encoder.fit_transform(a)
