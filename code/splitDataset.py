import json

rpath = "../yelp_academic_dataset_review.json"
model_path = "data_modeling.json"
training_path = "data_training.json"
testing_path = "data_testing.json"
encoded_data = "restaurants_encoded.json"
restaurants = set()
with open(encoded_data, "r") as data:
    for r in data:
        temp = json.loads(r)
        rsTemp = temp.keys()
        restaurants = set(rsTemp)
print(restaurants)
#######################################################
#
#STEP 1: get user-restaurant dict
#
#######################################################
user_review = dict()
with open(rpath, "r") as rs:
    for r in rs:
        review = json.loads(r)
        if (review['business_id'] in restaurants):
            if review['user_id'] in user_review:
                pair = [review['business_id'], review['stars']]
                user_review[review['user_id']].append(pair)
            else: 
                temp = list()
                pair = [review['business_id'], review['stars']]
                temp.append(pair)
                user_review[review['user_id']] = temp

########################################################
#
#STEP 2: split dict into modeling, training and testing
#
########################################################
data_modeling = dict()
data_training = list()
data_testing  = list()
for user in user_review.keys():
    len_total = len(user_review[user])
    if len_total > 3:

        len_modeling = int(len_total/2)
        
        list_total = user_review[user]
        list_modeling = list_total[:len_modeling]
        
        data_modeling[user] = list_modeling
        for rstrt in list_total[len_modeling+1:len_total-1]:
            data_training.append([user, rstrt])
        data_testing.append([user, list_total[len_total-1]])

#########################################################
#
#STEP 3: save data for modeling, training and testing
#
#########################################################
print(len(data_modeling))
print(len(data_training))
print(len(data_testing))
with open(model_path, 'w') as m:
    json.dump(data_modeling, m)
with open(training_path, 'w') as t:
    json.dump(data_training, t)
with open(testing_path, 'w') as te:
    json.dump(data_testing, te)
