#!/usr/bin/env python
# coding: utf-8

# In[12]:


#imports
from numpy import mean
from numpy import std
from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from matplotlib import pyplot
import json
import math
import numpy as np


# In[8]:


trainX_path = "training_X.json"
trainY_path = "training_Y.json"
testX_path  = "testing_X.json"
testY_path  = "testing_Y.json"

trainX = list()
with open(trainX_path, 'r') as data:
    for full in data:
        trainX = json.loads(full)
trainY = list()
with open(trainY_path, 'r') as data:
    for full in data:
        trainY = json.loads(full)
testX = list()
with open(testX_path, 'r') as data:
    for full in data:
        testX = json.loads(full)
testY = list()
with open(testY_path, 'r') as data:
    for full in data:
        testY = json.loads(full)

trainX = np.array(trainX)
trainY = np.array(trainY)
testX = np.array(testX)
testY = np.array(testY)


# In[9]:


#evaluate model
# evaluate the model
model = GradientBoostingRegressor()
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
n_scores = cross_val_score(model, trainX, trainY, scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1, error_score='raise')
print('MAE: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))


# In[13]:


boost = model.fit(trainX,trainY)
print(boost.score(trainX,trainY))

test_result = boost.predict(testX)

mse = math.sqrt(np.average((testY-test_result)**2))
print(mse)

