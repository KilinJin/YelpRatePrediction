import json
import ast

##################################
#
#    file paths
#
##################################
bpath = "../yelp_academic_dataset_business.json"
upath = "../yelp_academic_dataset_user.json"
rpath = "../yelp_academic_dataset_review.json"
newfile = "restaurants_encoded.json"
#text = "restaurant.txt"

#ff = open(text, 'r')
#prev = ff.readlines()
#ff.close()
#print(prev)
#count = 0
#get all restrauts
restaurants = dict()
with open(bpath, "r") as bs:
    for b in bs:
        item = json.loads(b)
        if item['categories'] != None and "Restaurants" in item['categories']:
 #           if (item['business_id']+'\n') not in prev:
 #               count = count + 1
#                print(len(prev))
 #               print(item)
            temp = dict()
            temp['name'] = item['name']
            temp['rCount'] = item['review_count']
            temp['stars'] = item['stars']
            temp['categories'] = str(item['categories']).split(', ')
            temp['alcohol'] = 0
            temp['attire'] = 0
            temp['wifi'] = 0
            temp['noise'] = 1
            temp['smoke'] = 0
            temp['age'] = 0
            temp['price'] = 1
            temp['music'] = "0000000"
            temp['gfm'] = "000000"   # good for meal
            temp['ab'] = "000000000" # ambience
            temp['park'] = "00000"   # business parking
            temp['best'] = "0000000" # best nights
            temp['diet'] = "0000000"
            '''
            other attributes are organized as follows:

            **Service
            HappyHour
            BikeParking
            WheelchairAccessible 
            Open24Hours
            RestaurantsCounterService
            HasTV
            Caters
            OutdoorSeating
            RestaurantsTableService

            **policy
            BusinessAcceptsBitcoin
            BYOB
            RestaurantsTakeOut
            BesinessAcceptsCreditCards
            RestaurantsReservations
            RestaurantsDelivery
            ByAppointmentOnly
            Corkage
            CoatCheck
            DogsAllowed

            **Style
            GoodForKids
            RestaurantsGoodForGroups
            GoodForDancing
            '''
            temp['service'] = "000000000"
            temp['policy'] = "0000000000"
            temp['style'] = "000"

            if (item['attributes'] != None):
                atrb = item['attributes']
                attrTemp = atrb.keys()

                #service
                if ("HappyHour" in attrTemp and atrb['HappyHour'] != None):
                    temp['service'] = "1" + temp['service'][1:]
                if ("BikeParking" in attrTemp and atrb['BikeParking'] != None):
                    temp['service'] = temp['service'][:1] + "1" + temp['service'][2:]
                if ("WheelchairAccessible" in attrTemp and atrb['WheelchairAccessible'] != None):
                    temp['service'] = temp['service'][:2] + "1" + temp['service'][3:]
                if ("Open24Hours" in attrTemp and atrb['Open24Hours'] != None):
                    temp['service'] = temp['service'][:3] + "1" + temp['service'][4:]
                if ("RestaurantsCounterService" in attrTemp and atrb['RestaurantsCounterService'] != None):
                    temp['service'] = temp['service'][:4] + "1" + temp['service'][5:]
                if ("HasTV" in attrTemp and atrb['HasTV'] != None):
                    temp['service'] = temp['service'][:5] + "1" + temp['service'][6:]
                if ("Caters" in attrTemp and atrb['Caters'] != None):
                    temp['service'] = temp['service'][:6] + "1" + temp['service'][7:]
                if ("OutdoorSeating" in attrTemp and atrb['OutdoorSeating'] != None):
                    temp['service'] = temp['service'][:7] + "1" + temp['service'][8:]
                if ("RestaurantsTableService" in attrTemp and atrb['RestaurantsTableService'] != None):
                    temp['service'] = temp['service'][:8] + "1"
               
                #policy
                if ("BusinessAcceptsBitcoin" in attrTemp and atrb['BusinessAcceptsBitcoin'] != None):
                    temp['policy'] = "1" + temp['policy'][1:]
                if ("BYOB" in attrTemp and atrb['BYOB'] != None):
                    temp['policy'] = temp['policy'][:1] + "1" + temp['policy'][2:]
                if ("RestaurantsTakeOut" in attrTemp and atrb['RestaurantsTakeOut'] != None):
                    temp['policy'] = temp['policy'][:2] + "1" + temp['policy'][3:]
                if ("BusinessAcceptsCreditCards" in attrTemp and atrb['BusinessAcceptsCreditCards'] != None):
                    temp['policy'] = temp['policy'][:3] + "1" + temp['policy'][4:]
                if ("RestaurantsReservations" in attrTemp and atrb['RestaurantsReservations'] != None):
                    temp['policy'] = temp['policy'][:4] + "1" + temp['policy'][5:]
                if ("RestaurantsDelivery" in attrTemp and atrb['RestaurantsDelivery'] != None):
                    temp['policy'] = temp['policy'][:5] + "1" + temp['policy'][6:]
                if ("ByAppointmentOnly" in attrTemp and atrb['ByAppointmentOnly'] != None):
                    temp['policy'] = temp['policy'][:6] + "1" + temp['policy'][7:]
                if ("Corkage" in attrTemp and atrb['Corkage'] != None):
                    temp['policy'] = temp['policy'][:7] + "1" + temp['policy'][8:]
                if ("CoatCheck" in attrTemp and atrb['CoatCheck'] != None):
                    temp['policy'] = temp['policy'][:8] + "1" + temp['policy'][9:]
                if ("DogsAllowed" in attrTemp and atrb['DogsAllowed'] != None):
                    temp['policy'] = temp['policy'][:9] + "1"
                
                #style
                if ("GoodForKids" in attrTemp and atrb['GoodForKids'] != None):
                    temp['style'] = "1" + temp['style'][1:]
                if ("RestaurantsGoodForGroups" in attrTemp and atrb['RestaurantsGoodForGroups'] != None):
                    temp['style'] = temp['style'][:1] + "1" + temp['style'][2:]
                if ("GoodForDancing" in attrTemp and atrb['GoodForDancing'] != None):
                    temp['style'] = temp['style'][:2] + "1"
                
                #price
                if ("RestaurantsPriceRange" in attrTemp and atrb['RestaurantsPriceRange'] != None):
                    temp['price'] = atrb['RestaurantsPriceRange']
                
                #age
                if ("AgesAllowed" in attrTemp and atrb['AgesAllowed'] != None):
                    if "19" in str(item['attributes']['AgesAllowed']):
                        temp['age'] = 19
                    if "21" in str(item['attributes']['AgesAllowed']):
                        temp['age'] = 21
                    if "18" in str(item['attributes']['AgesAllowed']):
                        temp['age'] = 18
                
                #smoking
                if ("Smoking" in attrTemp):
                    if "out" in str(item['attributes']['Smoking']):
                        temp['smoke'] = 1
                    elif "yes" in str(item['attributes']['Smoking']):
                        temp['smoke'] = 2

                #alcohol
                if ("Alcohol" in attrTemp):
                    if "full" in str(item['attributes']['Alcohol']):
                        temp['alcohol'] = 2
                    elif "wine" in str(item['attributes']['Alcohol']):
                        temp['alcohol'] = 1

               #attire
                if ("RestaurantsAttire" in attrTemp):
                    if "casual" in str(item['attributes']['RestaurantsAttire']):
                        temp['attire'] = 1
                    elif "no" in str(item['attributes']['RestaurantsAttire']):
                        temp['attire'] = 0
                    else:
                        temp['attire'] = 2
                
                #wifi
                if ("WiFi" in attrTemp):
                    if "free" in str(item['attributes']['WiFi']):
                        temp['wifi'] = 2
                    elif "paid" in str(item['attributes']['WiFi']):
                        temp['wifi'] = 1
                
                #noise
                if ("NoiseLevel" in attrTemp):
                    if "very" in str(item['attributes']['NoiseLevel']):
                        temp['NoiseLevel'] = 3
                    elif "loud" in str(item['attributes']['NoiseLevel']):
                        temp['NoiseLevel'] = 2
                    elif "quiet" in str(item['attributes']['NoiseLevel']):
                        temp['NoiseLevel'] = 0
                
                #music
                if ("Music" in attrTemp and item["attributes"]['Music'] != "None"):
                    musicTemp = ast.literal_eval(item['attributes']['Music'])
                    keys = musicTemp.keys()
                    if "dj" in keys and musicTemp["dj"] is True:
                        temp['music'] = "1" + temp['music'][1:]
                    if "background_music" in keys and musicTemp["background_music"] is True:
                        temp['music'] =temp['music'][:1] + "1" + temp['music'][2:]
                    if "no_music" in keys and musicTemp["no_music"] is True:
                        temp['music'] =temp['music'][:2] + "1" + temp['music'][3:]
                    if "jukebox" in keys and musicTemp["jukebox"] is True:
                        temp['music'] =temp['music'][:3] + "1" + temp['music'][4:]
                    if "live" in keys and musicTemp["live"] is True:
                        temp['music'] =temp['music'][:4] + "1" + temp['music'][5:]
                    if "video" in keys and musicTemp["video"] is True:
                        temp['music'] =temp['music'][:5] + "1" + temp['music'][6:]
                    if "karaoke" in keys and musicTemp["karaoke"] is True:
                        temp['music'] =temp['music'][:6] + "1"

                #good for meal
                if ("GoodForMeal" in attrTemp and item["attributes"]['GoodForMeal'] != "None"):
                    gfmTemp = ast.literal_eval(item['attributes']['GoodForMeal'])
                    keys = gfmTemp.keys()
                    if "dessert" in keys and gfmTemp["dessert"] is True:
                        temp['gfm'] = "1" + temp['gfm'][1:]
                    if "latenight" in keys and gfmTemp["latenight"] is True:
                        temp['gfm'] =temp['gfm'][:1] + "1" + temp['gfm'][2:]
                    if "lunch" in keys and gfmTemp["lunch"] is True:
                        temp['gfm'] =temp['gfm'][:2] + "1" + temp['gfm'][3:]
                    if "dinner" in keys and gfmTemp["dinner"] is True:
                        temp['gfm'] =temp['gfm'][:3] + "1" + temp['gfm'][4:]
                    if "brunch" in keys and gfmTemp["brunch"] is True:
                        temp['gfm'] =temp['gfm'][:4] + "1" + temp['gfm'][5:]
                    if "breakfast" in keys and gfmTemp["breakfast"] is True:
                        temp['gfm'] =temp['gfm'][:5] + "1"
                
                #ambience
                if ("Ambience" in attrTemp and item["attributes"]['Ambience'] != "None"):
                    abTemp = ast.literal_eval(item['attributes']['Ambience'])
                    keys = abTemp.keys()
                    if "touristy" in keys and abTemp["touristy"] is True:
                        temp['ab'] = "1" + temp['ab'][1:]
                    if "hipster" in keys and abTemp["hipster"] is True:
                        temp['ab'] =temp['ab'][:1] + "1" + temp['ab'][2:]
                    if "romantic" in keys and abTemp["romantic"] is True:
                        temp['ab'] =temp['ab'][:2] + "1" + temp['ab'][3:]
                    if "divey" in keys and abTemp["divey"] is True:
                        temp['ab'] =temp['ab'][:3] + "1" + temp['ab'][4:]
                    if "intimate" in keys and abTemp["intimate"] is True:
                        temp['ab'] =temp['ab'][:4] + "1" + temp['ab'][5:]
                    if "trendy" in keys and abTemp["trendy"] is True:
                        temp['ab'] =temp['ab'][:5] + "1" + temp['ab'][6:]
                    if "upscale" in keys and abTemp["upscale"] is True:
                        temp['ab'] =temp['ab'][:6] + "1" + temp['ab'][7:]
                    if "classy" in keys and abTemp["classy"] is True:
                        temp['ab'] =temp['ab'][:7] + "1" + temp['ab'][8:]
                    if "casual" in keys and abTemp["casual"] is True:
                        temp['ab'] =temp['ab'][:8] + "1"

                #business parking
                if ("BusinessParking" in attrTemp and item["attributes"]['BusinessParking'] != "None"):
                    parkTemp = ast.literal_eval(item['attributes']['BusinessParking'])
                    keys = parkTemp.keys()
                    if "garage" in keys and parkTemp["garage"] is True:
                        temp['park'] = "1" + temp['park'][1:]
                    if "street" in keys and parkTemp["street"] is True:
                        temp['park'] =temp['park'][:1] + "1" + temp['park'][2:]
                    if "validated" in keys and parkTemp["validated"] is True:
                        temp['park'] =temp['park'][:2] + "1" + temp['park'][3:]
                    if "lot" in keys and parkTemp["lot"] is True:
                        temp['park'] =temp['park'][:3] + "1" + temp['park'][4:]
                    if "valet" in keys and parkTemp["valet"] is True:
                        temp['park'] =temp['park'][:4] + "1"

                #dietary restriction
                if ("DietaryRestrictions" in attrTemp and item["attributes"]['DietaryRestrictions'] != "None"):
                    dietTemp = ast.literal_eval(item['attributes']['DietaryRestrictions'])
                    keys = dietTemp.keys()
                    if "dairy-free" in keys and dietTemp["dairy-free"] is True:
                        temp['diet'] = "1" + temp['diet'][1:]
                    if "gluten-free" in keys and dietTemp["gluten-free"] is True:
                        temp['diet'] = temp['diet'][:1] + "1" + temp['diet'][2:]
                    if "vegan" in keys and dietTemp["vegan"] is True:
                        temp['diet'] = temp['diet'][:2] + "1" + temp['diet'][3:]
                    if "kosher" in keys and dietTemp["kosher"] is True:
                        temp['diet'] = temp['diet'][:3] + "1" + temp['diet'][4:]
                    if "halal" in keys and dietTemp["halal"] is True:
                        temp['diet'] = temp['diet'][:4] + "1" + temp['diet'][5:]
                    if "soy-free" in keys and dietTemp["soy-free"] is True:
                        temp['diet'] = temp['diet'][:5] + "1" + temp['diet'][6:]
                    if "vegetarian" in keys and dietTemp["vegetarian"] is True:
                        temp['diet'] = temp['diet'][:6] + "1"
            restaurants[item['business_id']] = temp
            print(temp)
#print(count)
with open(newfile, 'w') as fp:
    json.dump(restaurants, fp)
