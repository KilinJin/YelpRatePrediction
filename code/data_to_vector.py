import json

model_path = "user_model.json"
training_path = "data_testing.json"
testing_path = "data_testing.json"
restaurants_path = "restaurants_encoded.json"
training_X = "testing_X.json"
training_Y = "testing_Y.json"

training_list = list()
with open(training_path, 'r') as data:
    for full in data:
        training_list = json.loads(full)

user_model = dict()
with open(model_path, 'r') as data:
    for full in data:
        user_model = json.loads(full)

restaurants = dict()
with open(restaurants_path, 'r') as data:
    for full in data:
        restaurants = json.loads(full)

def match(uid, bid):
    u_info = user_model[uid]
    b_info = restaurants[bid]
    
    vec = list()
    features = u_info.keys()
    for feature in features:
        b_feature = b_info[feature]
        u_feature = u_info[feature]
        value = 0
        if type(b_feature) is int:
            for item in u_feature:
                diff = abs(item[0]-b_feature)
                if diff == 0:
                    diff = 0.5
                value = value + 1/diff * item[1]
        elif type(b_feature) is float:
            for item in u_feature:
                diff = abs(item[0]-b_feature)
                if diff == 0:
                    diff = 0.5
                value = value + 1/diff * item[1]
        else:
            for item in u_feature:
                diff = 0
                for i in range(len(b_feature)):
                    if (b_feature[i] != item[0][i]):
                        diff = diff + 1
                if diff == 0:
                    diff = 0.5
                value = value + 1/diff * item[1]
        
        length = len(u_feature)
        if (length == 0):
            length = 1
        value = value/length
        vec.append(value)
    

    return vec


X = list()
Y = list()
for item in training_list:
    if item[0] in user_model and item[1][0] in restaurants:
        x = match(item[0], item[1][0])
        X.append(x)
        Y.append(item[1][1])
print(len(X))
with open(training_X, 'w') as t:
    json.dump(X, t)
with open(training_Y, 'w') as t:
    json.dump(Y, t)
