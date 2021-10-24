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

print(M)
#declaring k,metric as global which can be changed by the user later
global k,metric
k=4 # number of the most similar users
metric='cosine'

M = M.iloc[:,1:-2]
print(M)

cosine_sim = 1-pairwise_distances(M, metric="cosine")

pd.DataFrame(cosine_sim)

def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[user_id-1, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    print ('{0} of the most similar users for User {1}:\n'.format(k,user_id) )
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i]+1 == user_id:
            continue;

        else:
            print ('{0}: User {1}, with similarity of {2}'.format(i, indices.flatten()[i]+1, similarities.flatten()[i]) )
            
    return similarities,indices



similarities,indices = findksimilarusers(332,M, metric='cosine',k=5)
# The total number of data is 332

# In 四人搭配.csv the last data is numbered 333, the first dataq is numbered 2
# In here, the last data is numbered 332, the first data is numbered 1
# the number here + 1 = the number of corresponding row in 四人搭配.csv

# negative index means count from back. '-' means count from right to left, and the number is the order.

print('\n')