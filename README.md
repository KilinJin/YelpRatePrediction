# YelpRatePrediction

How to use: <br>
# 1, clone this repo and put the dataset in it, the organization should look like below:
```
YelpRatePrediction
├── yelp_academic_dataset_review.json
├── yelp_academic_dataset_business.json
├── yelp_academic_dataset_tip.json
├── yelp_academic_dataset_checkin.json
├── yelp_academic_dataset_user.json
├── code
|   ├── data_to_vector.py
|   ├── get_user_model.py
|   ├── extract.py
|   ├── linear_regression.py
|   ├── splitDataset.py
```

# 2, run the files in the following order:
2.1: run '''splitDataset.py''', this file split the whole review dataset into 3 parts <br>
You should get'''data_modeling.json''',  '''data_training.json''' and '''data_testing.json'''
2.2 run '''extract.py''', this file encode each item in the business dataset into a simpler representation <br>
You should get'''restaurants_encoded.json'''
2.3 run '''user_model.py''', this file gets you the user model <br>
You should get'''user_model.json''' (note: if your computer does not have enough memory to run this, download the same file on the shared google folder)
2.4 the file '''data_to_vector.py''' turns the '''data_training.json''' and '''data_testing.json''' you got from step 2.1 into vectors, seperately. This means that if you need to turn '''data_training.json''' to vectors stored in '''trainning_X.json''' and '''trainning_Y.json''', you need to modify line 4, 7, 8 <br>
You should get'''restaurants_encoded.json'''
2.2 run '''extract.py''', this file encode each item in the business dataset into a simpler representation <br>
You should get'''restaurants_encoded.json'''
