#make necesarry imports
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
import sklearn.metrics as metrics
from sklearn.neighbors import NearestNeighbors
from scipy.spatial.distance import correlation, cosine
import ipywidgets as widgets
#from IPython.display import display, clear_output
from sklearn.metrics import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import sys, os
from contextlib import contextmanager

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "",
    database = "clothweb"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM cloth2 ORDER BY ID ASC")

myresult = mycursor.fetchall()

M = pd.DataFrame (myresult,columns = ['name','cloth','pant','color','color2','shade','shade2','ID'])

#print(M)
#declaring k,metric as global which can be changed by the user later
global k,metric
k=4 # number of the most similar users
metric='cosine'

names = M.iloc[:,0]
#print(names)
#高季廷 0 ~ 83
#方志堯 84 ~ 210
#張家瑋 211 ~ 232
#方韋傑 233 ~ 331

M = M.iloc[:,1:-1]
#print(M)

cosine_sim = 1-pairwise_distances(M, metric="cosine")

pd.DataFrame(cosine_sim)

total_similarities = dict()
for name in names:
    total_similarities[name] = 0

def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[user_id, :].values.reshape(1, -1), n_neighbors = k+1)

    flattened_indices = indices.flatten()
    similarities = 1-distances.flatten() #only 1 D

    print ('{0} of the most similar users for User {1}, whose name is {2}:\n'.format(k,user_id,names[user_id]) )
    for i in range(0, len(flattened_indices)):
        # if flattened_indices[i] == user_id:
        #     print("{0}: iterates the user_id, skip.".format(i))
        #     continue;

        # else:
            if names[flattened_indices[i]] != names[user_id]:
                print ('{0}: User {1} ({2}), with similarity of {3}'.format(i, flattened_indices[i],names[flattened_indices[i]], similarities[i]) );
                total_similarities[names[flattened_indices[i]]] += similarities[i]
            else:
                print("{0}: The user is {1}, same as the picked user, skip.".format(i,names[user_id]))

    return similarities,indices



#similarities,indices = findksimilarusers(86,M, metric='cosine',k=5)
#print(total_similarities)
picked_person = "方韋傑"

for index,name in enumerate(names):
    if name == picked_person:
        similarities,indices = findksimilarusers(index,M, metric='cosine',k=5)
print(total_similarities)

""" similarities,indices = findksimilarusers(0,M, metric='cosine',k=5)
print(total_similarities) """

# The total number of data is 332, numbered 0 ~ 331 (user_id :)

# negative index means count from back. '-' means count from right to left, 
# and the number is the order, start from 0 but -0 may cause error.

print('\n')