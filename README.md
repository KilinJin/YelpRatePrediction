# YelpRatePrediction

How to use: <br>
## 1, clone this repo and put the dataset in it, the organization should look like below:
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
|   ├── generate.dataset.with.text.feature.ipynb
├── model
|   ├── ridge.regression.ipynb
|   ├── xgboost.ipynb
|   ├── lightgbm.ipynb
├── generate.text.features
|   ├──extract.restaurants.ipynb
|   ├──aggregate.restaurant.reviews.ipynb
|   ├──vectorize.reviews.ipynb
|   ├──topic_modeling.py
|   ├──process.topic.modeling.prob.ipynb
```

## 2, run the files in the following order:<br>
2.1: run `splitDataset.py`, this file split the whole review dataset into 3 parts <br>
You should get `data_modeling.json`,  `data_training.json` and `data_testing.json`<br>
2.2 run `extract.py`, this file encode each item in the business dataset into a simpler representation <br>
You should get `restaurants_encoded.json`<br>
2.3 run `user_model.py`, this file gets you the user model <br>
You should get `user_model.json` (note: if your computer does not have enough memory to run this, download the same file on the shared google folder and put it into the `code` foler)<br>
2.4  **NOTICE!!** use the file `data_to_vector.py` as follows:
2.4.1: run it directly, you should get `testing_X.json` and `testing_Y.json`<br>
2.4.2: modify the line 4,7,8 (no need to care about line 5), change the `testing` substring in them into `training`, then  you shuold get `training_X.json` and `training_Y.json`<br>.
the 4 result files are training and testing data encoded into vectors.<br>
2.4.3: run `generate.dataset.with.text.feature.ipynb` to get the feature table with text features, the rest are the same as you get from `data_to_vector.py`. For information about how to generate text features, see *2.6*.<br>
2.5 Fitting the model.<br>
2.5.1 run `linear_regression.py`, the final result should be printed.<br>
2.5.2 run `ridge.regression.ipynb` to fit a ridge regression model, in which we do feature selection using grid searching with Cross-Validation.<br>
2.5.3 run `xgboost.ipynb` to fit a xgboost model, in which we do parameter tuning with Cross-Validation.<br>
2.6 Generaet text features.<br>
2.6.1 run `extract.restaurants.ipynb` to extract all the restaurants from the business dataset, and run `aggregate.restaurant.reviews.ipynb` to aggregate reviews for every restaurant.<br>
2.6.2 run `vectorize.reviews.ipynb` to get the first text feature: text vector representations.<br>
2.6.3 run `topic_modeling.py` and `process.topic.modeling.prob.ipynb` to get the second text feature: probability distributions over topics for each restaurant. Note training a LDA model can take a long time.<br>
