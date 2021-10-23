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

mycursor.execute("SELECT * FROM cloth ORDER BY name ASC")

myresult = mycursor.fetchall()

df = pd.DataFrame (myresult, columns = ['name','cloth','color','shade','pant','color2','shade2'])
#print (df)

M = df
print(M)
#declaring k,metric as global which can be changed by the user later
global k,metric
k=4
metric='cosine'

M = M.iloc[:,1:]

cosine_sim = 1-pairwise_distances(M, metric="cosine")

pd.DataFrame(cosine_sim)

def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    model_knn = NearestNeighbors(metric = metric, algorithm = 'brute') 
    model_knn.fit(ratings)

    distances, indices = model_knn.kneighbors(ratings.iloc[user_id-1, :].values.reshape(1, -1), n_neighbors = k+1)
    similarities = 1-distances.flatten()
    print ('{0} most similar users for User {1}:\n'.format(k,user_id) )
    for i in range(0, len(indices.flatten())):
        if indices.flatten()[i]+1 == user_id:
            continue;

        else:
            print ('{0}: User {1}, with similarity of {2}'.format(i, indices.flatten()[i]+1, similarities.flatten()[i]) )
            
    return similarities,indices

similarities,indices = findksimilarusers(1,M, metric='cosine')