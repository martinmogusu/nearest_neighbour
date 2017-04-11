# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:00:35 2016

@author: Martin
"""
import numpy as np
import math
from operator import itemgetter
from collections import Counter

def get_distance(data1, data2):
    points = list(zip(data1, data2))
    points[0] = tuple([(p * 0.0001) for p in points[0]])
    sqr_differences = [pow(a - b, 2) for a, b in points]
    return math.sqrt(sum(sqr_differences))
    
def get_neighbours(training_set, test_instance, k):
    distances = [(training_instance, get_distance(test_instance[0], training_instance[0])) for training_instance in training_set]
    sorted_distances = sorted(distances, key=itemgetter(1))
    sorted_training_distances = [d[0] for d in sorted_distances]
    return sorted_training_distances[:k]
    
def get_majority_vote(neighbours):
    classifications = [neighbour[1] for neighbour in neighbours]
    count = Counter(classifications)
    return count.most_common()[0][0]

data = np.loadtxt("datingTestSet.txt")
formatted_data = [(d[:3], d[3]) for d in data]
train = formatted_data[:600]
test = formatted_data[600:]

expected_values = [t[1] for t in test]
found_values = [get_majority_vote(get_neighbours(train, instance, 10)) for instance in test]

value_stats = list(zip(expected_values, found_values))
expected_summary = dict(Counter(expected_values))
found_summary = dict(Counter(found_values))

#Test accuracy
print("%s\t%s\t%s" % ("No.", "Expected", "Found"))
for i in range(len(test)):
    value = value_stats[i]
    print("%s\t%s\t\t%s" % (i, value[0], value[1]), end="")
    if value[0] == value[1] :
        print()
    else:
        print("\tNot equal")
        
    
#Expected values
print("Expected values summary:\n", expected_summary)
print("Found values summary:\n", found_summary)


