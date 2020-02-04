# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:40:23 2020

@author: Admin
"""

#!/usr/bin/python3

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
enron_data = pickle.load(open("W:/DATA SCIENTIST/ud120-projects-master/final_project/final_project_dataset.pkl", "rb"))

# Find number of person in the dataset
print(len(enron_data.keys()))

#find number of features each key has
print(len(enron_data['METTS MARK']))


# Find total number of perosn of interest.
count=0
for k,v in enron_data.items():
    if v['poi']==1:
        count+=1
print(count)



#quantified salary
count=0
for k,v in enron_data.items():
    if not(math.isnan(int(v['salary']))):
        count+=1
print(count)