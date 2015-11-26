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
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Total number of data points available in the dataset is : ", len(enron_data)
print "Total number of features available in the dataset is : ", len(enron_data["SKILLING JEFFREY K"])

print " The list of variables ", enron_data["SKILLING JEFFREY K"].keys()
# Count the total number of POI
count = 0

for key in enron_data.keys():
   if enron_data[key]["poi"] == 1:
      count +=1

print "Total number of Person of interest available in the data is : ",count

stock = 0
for key in enron_data.keys():
   #print key
   if key == "JAMES PRENTICE" or key == "PRENTICE JAMES":
      stock += enron_data[key]["total_stock_value"]
   if key == "COLWELL WESLEY" or key == "WESLEY COLWELL":
      print " Total email from ", key," to persons of interest is ; ",enron_data[key]["from_this_person_to_poi"]
   if key == "JEFFREY SKILLING K" or key == "SKILLING JEFFREY K":
      print enron_data[key]["exercised_stock_options"]


#print "Total value of stock James Prentice have : ", stock

#Calculate how many folks have quantified salary
salaried_person = 0
email_persons = 0

for key in enron_data.keys():
   if float(enron_data[key]['salary']) >0:
      salaried_person += 1
   if len(enron_data[key]['email_address'])>3 :
      email_persons += 1
#   else:
#     print enron_data[key]['email_address']

print "Salaried persons : ",salaried_person
print "Email persons : ", email_persons


#count the total number of people have NaN for their total payments

count_tp = 0
total_row = 0
for key in enron_data.keys():
   total_row += 1
   if (enron_data[key]["total_payments"]=='NaN') & (enron_data[key]['poi'] == 1):
      count_tp += 1

print "People with NaN as their total_payments : ", count_tp, " total rows = ", total_row
