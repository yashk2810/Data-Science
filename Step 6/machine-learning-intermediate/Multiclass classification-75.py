## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars['origin'].unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)
print(cars.head())

dummy_years = pd.get_dummies(cars['year'], prefix='year')
cars = pd.concat([cars, dummy_years], axis=1)
cars = cars.drop(['year', 'cylinders'], axis=1)
print(cars.head())

## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

train = shuffled_cars[:274]
test = shuffled_cars[274:]

## 4. Training a multiclass logistic regression model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

for i in unique_origins:
    lr = LogisticRegression()
    x = train[train.columns[6:]]
    y = train['origin'] == i
    lr.fit(x, y)
    
    models[i] = lr
    
    

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
for i in unique_origins:
    predictions = models[i].predict_proba(test[test.columns[6:]])[:,1]
    testing_probs[i] = predictions
    
print(testing_probs)


## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)