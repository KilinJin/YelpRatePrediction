import json

r_path = "restaurants_encoded.json"
modeling_path = "data_modeling.json"
training_path = "data_training.json"
testing_path  = "data_testing.json"
user_model_path = "user_model.json"

##############################################
#
#STEP 1: store restaurants as dict
#
##############################################
restaurants = dict()
with open(r_path, "r") as data:
    for full in data:
        restaurants = json.loads(full)

##############################################
#
#STEP2: create user model
#
#users = dict{key = user_id, value = 
#            dict{key = attributes(music, noise level, etc), value = 
#                dict{key = value of that attribute, value = rate}
#                }
#            }
#
##############################################
user_restaurant = dict()
user_model = dict()
with open(modeling_path, 'r') as data:
    for full in data:
        user_restaurant = json.loads(full)
        
        users = user_restaurant.keys()
        print(len(users))
        for user in users:
            info = dict()
            info['rCount'] = list()
            info['stars'] = list()
            info['alcohol'] = list()
            info['attire'] = list()
            info['wifi'] = list()
            info['noise'] = list()
            info['smoke'] = list()
            info['age'] = list()
            info['price'] = list()
            info['music'] = list()
            info['gfm'] = list()
            info['ab'] = list()
            info['park'] = list()
            info['best'] = list()
            info['diet'] = list()
            info['service'] = list()
            info['policy'] = list()
            info['style'] = list()

            for restaurant in user_restaurant[user]:
                res_id = restaurant[0]
                res_rate = restaurant[1]
                
                if res_id in restaurants:
                    info['rCount'].append([restaurants[res_id]['rCount'], res_rate])
                    info['stars'].append([restaurants[res_id]['stars'], res_rate])
                    info['alcohol'].append([restaurants[res_id]['attire'], res_rate])
                    info['wifi'].append([restaurants[res_id]['wifi'], res_rate])
                    info['noise'].append([restaurants[res_id]['noise'], res_rate])
                    info['smoke'].append([restaurants[res_id]['smoke'], res_rate])
                    info['age'].append([restaurants[res_id]['age'], res_rate])
                    info['price'].append([restaurants[res_id]['price'], res_rate])
                    info['music'].append([restaurants[res_id]['music'], res_rate])
                    info['gfm'].append([restaurants[res_id]['gfm'], res_rate])
                    info['ab'].append([restaurants[res_id]['ab'], res_rate])
                    info['park'].append([restaurants[res_id]['park'], res_rate])
                    info['best'].append([restaurants[res_id]['best'], res_rate])
                    info['diet'].append([restaurants[res_id]['diet'], res_rate])
                    info['service'].append([restaurants[res_id]['service'], res_rate])
                    info['policy'].append([restaurants[res_id]['policy'], res_rate])
                    info['style'].append([restaurants[res_id]['style'], res_rate])
            user_model[user] = info

print(len(user_model))
with open(user_model_path, 'w') as m:
    json.dump(user_model, m)
