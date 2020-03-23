# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 20:48:43 2020

@author: Admin
"""

import sqlite3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import nltk
import string 
from sklearn.feature_extraction.text import CountVectorizer


def partition(x):
    if x <3:
        return 'negative'
    return 'positive'



con = sqlite3.connect("W:/DATA SCIENTIST/Machine-Learning/Codes/Datasets/amazon-fine-food-reviews/database.sqlite")


filtered_data = pd.read_sql_query(""" Select * From Reviews WHERE score!=3""",con)

actualScore = filtered_data['Score']
positveNegative = actualScore.map(partition)

filtered_data['Score'] = positveNegative

filtered_data.shape
filtered_data.head()


#Data cleaning
#We can see that in the data few data has same timestamp. On further analysis we see that products of 
#same company get common reviews. Thus we want to remove dupicate entries

sorted_data = filtered_data.sort_values('ProductId',axis=0,ascending =True)
final = sorted_data.drop_duplicates(subset={"UserId","ProfileName","Time","Text"},keep='first',inplace=False)
final.shape




#For two rows The helpfulness Numerator was greater than Helpfulness denominator which is  not correct.
# Thus those 2 rows need to be removed. 


final = final[final.HelpfulnessNumerator<=final.HelpfulnessDenominator]


#Bag of Words Representation 
count_vect = CountVectorizer()
final_counts = count_vect.fit_transform(final['Text'].values)
final_counts.get_shape()
