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
2.5 run `linear_regression.py`, the final result should be printed. 
