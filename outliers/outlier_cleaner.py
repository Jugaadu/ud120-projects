#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    #print predictions

    #print "Printing ages ","\n", ages ," \n printing the other one ", net_worths
    
    predictions = [ x[0] for x in  predictions]
    ages = [x[0] for x in ages]
    net_worths = [x[0] for x in net_worths]

    import numpy as np
    
    
    rss = []
    
    for j in range(len(predictions)):
        rss.append(float(predictions[j] - net_worths[j]))

    
    test_tup = zip(ages,net_worths,rss)


    def getitem(item):
        return -item[2]

    cleaned_data = []
    
    ### your code goes here
    test_tup = sorted(test_tup,key = getitem)
    
    for i in range(9,len(test_tup)):
        cleaned_data.append(test_tup[i])
    
    return cleaned_data

