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
# import types

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print len(enron_data)

# print type(enron_data)

countPoi = 0
countSalary = 0

# for k in enron_data['SKILLING JEFFREY K']:

# print len(enron_data['SKILLING JEFFREY K'])

# print enron_data['SKILLING JEFFREY K']

# for k in enron_data:
#     # print k
#     if enron_data[k]['poi'] == 1:
#         countPoi += 1
#         # print k
#         print enron_data[k]

# print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# for k in enron_data:
#     if enron_data[k]['total_payments'] == 'NaN':
#         countSalary += 1

# # print ( countSalary / len(enron_data) ) 
# # print len(enron_data)

# print countSalary


# for k in enron_data:
#     # print k
#     if enron_data[k]['poi'] == 1:
#         countPoi += 1
# print countPoi

# for k in enron_data:
#     print k

# print enron_data['PRENTICE JAMES']


print enron_data['COLWELL WESLEY']
