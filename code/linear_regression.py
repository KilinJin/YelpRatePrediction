import numpy as np
from sklearn.linear_model import LinearRegression
import json
import math

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

reg = LinearRegression().fit(trainX, trainY)
print(reg.score(trainX,trainY))
test_result = reg.predict(testX)

print(math.sqrt(np.average((testY-test_result)**2)))
