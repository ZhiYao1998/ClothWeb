# coding=UTF-8

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


user = sys.argv[1]
print("當前使用者：",user)

Type = sys.argv[2]
print("clothing type:",Type)

flag = int(sys.argv[3]) # 0 => cloth | 1 => pant
print("The flag is :",flag)

color = int(sys.argv[4])
print("The color is :",color)

shade = int(sys.argv[5])
print("The shade is :",shade)
#flag = int(flag)

#print("當前使用者：",user)
#print("clothing type:",Type)
    

mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password = "password",
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

#高季廷 0 ~ 83
#方志堯 84 ~ 210
#方韋傑 211 ~ 232
#張家瑋 233 ~ 331

Manipulated = M.iloc[:,1:-1]
#print(M)

ptr = names.index[-1]+1
names.loc[ptr] = user
color_of_cloth = M.iloc[:,[3,5]]
color_of_pant = M.iloc[:,[4,6]]
if(flag == 1):
    print("choose pant")
    color_of_pant.loc[ptr] = [color,shade]
else:
    print("choose cloth")
    color_of_cloth.loc[ptr] = [color,shade]

cosine_sim = 1-pairwise_distances(Manipulated, metric="cosine")

pd.DataFrame(cosine_sim)

total_similarities = dict()
for name in names:
    total_similarities[name] = 0

def findksimilarusers(user_id, ratings, metric = metric, k=k):
    similarities=[]
    indices=[]
    
    
    model_knn = NearestNeighbors(metric = metric, algorithm = 'auto') 
    model_knn.fit(ratings)
    
    distances, indices = model_knn.kneighbors(ratings.iloc[user_id, :].values.reshape(1, -1), n_neighbors = k+1)

    flattened_indices = indices.flatten()
    similarities = 1-distances.flatten() #only 1 D

    
    for i in range(0, len(flattened_indices)):
        
            if names[flattened_indices[i]] != names[user_id]:
                #print ('{0}: Combination {1} (from {2}), with similarity of {3}'.format(i, flattened_indices[i],names[flattened_indices[i]], similarities[i]) );
                total_similarities[names[flattened_indices[i]]] += similarities[i]
            else:
                #print("{0}: The combination is from {1}, same as the picked user, skip.".format(i,names[user_id]))
                total_similarities[names[flattened_indices[i]]] +=0

    return similarities,indices

def findksimilarcolor(user_id, ratings, flag, metric = metric, k=k):
    indices=[]    
    distances=[]
    index = []
    temp = []

    model_knn = NearestNeighbors(metric = metric, algorithm = 'auto') 
    model_knn.fit(ratings)
    
    distances, indices = model_knn.kneighbors(ratings.iloc[user_id, :].values.reshape(1, -1), n_neighbors = k+1)

    flattened_indices = indices.flatten()

    for i in range(0, len(flattened_indices)):
            if names[flattened_indices[i]] != names[user_id]:
                if(flag == 0):  # cloth
                    color = color_of_pant.iloc[flattened_indices[i]].values[0]
                    shade = color_of_pant.iloc[flattened_indices[i]].values[1]
                else:           # pant
                    color = color_of_cloth.iloc[flattened_indices[i]].values[0]
                    shade = color_of_cloth.iloc[flattened_indices[i]].values[1]
                #print ('{0}: | Id: {1} | name: {2} | color: {3} | shade: {4}'.format(i, flattened_indices[i],names[flattened_indices[i]] ,color,shade) )
                if([color,shade] not in temp):
                      temp.append([color,shade])
                      index.append(flattened_indices[i])
                      #print(temp)
            #else:
                #print("{0}: | Id: {1} | name: {2} ,skip.".format(i, flattened_indices[i],names[flattened_indices[i]] ) )

    return temp



picked_person = user

for index,name in enumerate(names):
    if (name == picked_person and index != ptr):
        similarities,indices = findksimilarusers(index,Manipulated, metric='cosine',k=5)
print(total_similarities)

max_value = max(total_similarities.values())  # maximum value
max_keys = {k for k, v in total_similarities.items() if v == max_value}
for p in max_keys:
    print("與 {0} 最相似的使用者(可能有多個)： {1}".format(picked_person,p))
    


picking_cloth = Type

if(flag == 0):
  duplicate = []
  for p in max_keys:
      for index,combination in M.iterrows():

          if combination['name'] == p and int(combination['cloth']) == int(picking_cloth):
              if(combination['pant'] not in duplicate):
                  duplicate.append(combination['pant'])
                  print("recommended pants:",combination['pant'])
  print('--------------------------------------------')
  result = findksimilarcolor(ptr,color_of_cloth,flag)
  for items in result:
      print("recommended color: ",items)
else:
  duplicate = []
  for p in max_keys:
    for index,combination in M.iterrows():
        
        if combination['name'] == p and int(combination['pant']) == int(picking_cloth):
            if(combination['cloth'] not in duplicate):
                  duplicate.append(combination['cloth'])
                  print("recommended clothes:",combination['cloth'])
  print('--------------------------------------------')
  result = findksimilarcolor(ptr,color_of_pant,flag)
  #print(result)
  for items in result:
      print("recommended color & shade: ",items)


"""for p in max_keys:
    for index,combination in M.iterrows():
        #print("indices:",index)
        #print(combination['name'], combination['cloth'], combination['pant'])
        if combination['name'] == p and combination['color'] == picking_cloth[1]:
            print("recommended color of pant:",combination['color2'])"""

""" similarities,indices = findksimilarusers(0,M, metric='cosine',k=5)
print(total_similarities) """

# The total number of data is 332, numbered 0 ~ 331 (user_id :)

# negative index means count from back. '-' means count from right to left, 
# and the number is the order, start from 0 but -0 may cause error.

print('\n')
