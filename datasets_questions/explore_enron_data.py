#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Total number of data points available in the dataset is : ", len(enron_data)
print "Total number of features available in the dataset is : ", len(enron_data["SKILLING JEFFREY K"])


# Count the total number of POI
count = 0

for key in enron_data.keys():
   if enron_data[key]["poi"] == 1:
      count +=1

print "Total number of Person of interest available in the data is : ",count
