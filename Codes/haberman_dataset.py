# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:36:34 2020

@author: Admin
"""

#Apply concepts of EDA on haberman cancer survival dataset. 
#https://www.kaggle.com/gilsousa/habermans-survival-data-set/data#
# The process which i am thinking of following is to understand higher level stats of the dataset 
# and gain some domain knowldge
# Keep my objective in my mind
#Perform univariate and multivariate analysis
# Explain the observations.

#Attribute Information:

#Age of patient at time of operation (numerical)
#Patient's year of operation (year - 1900, numerical)
#Number of positive axillary nodes detected (numerical)
#Survival status (class attribute) 1 = the patient survived 5 years or longer 2 = the patient died within 5 year



#import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 



haberman_data = pd.read_csv("W:/DATA SCIENTIST/Machine-Learning/Codes/Datasets/habermans-survival-data-set/haberman.csv")


# Few stats about the data
print(haberman_data.head(5))
print(haberman_data.shape)
print(haberman_data.columns)

print(haberman_data.describe())



#checking number of patients survival of more or less than 5 years.
haberman_data['Survival'].value_counts()

haberman_data.plot(kind = 'scatter',x = 'Age',y = 'no_auxilary_nodes')

nodes_not_zero = haberman_data[haberman_data['no_auxilary_nodes']!=0]

nodes_not_zero.plot(kind = 'scatter',x = 'Age',y = 'no_auxilary_nodes')


# plotting survival vs nodes
haberman_data.plot(kind = 'scatter',x = 'no_auxilary_nodes',y = 'Survival')


sns.set_style('whitegrid')
sns.FacetGrid( haberman_data, hue="Survival",size = 4 ).map(plt.scatter,"Age","no_auxilary_nodes").add_legend()
plt.show()



sns.set_style('whitegrid')
sns.FacetGrid( haberman_data, hue="Survival",size = 4 ).map(plt.scatter,"Age","Op_year").add_legend()
plt.show()



    