## 2. Partititioning the data ##

import pandas as pd

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
admissions = shuffled_admissions.reset_index()
print(admissions)

admissions.ix[0:128, "fold"] = 1
admissions.ix[129:257, "fold"] = 2
admissions.ix[258:386, "fold"] = 3
admissions.ix[386:514, "fold"] = 4
admissions.ix[514:644, "fold"] = 5

print(admissions.head())
print(admissions.tail())

## 3. First iteration ##

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
train = admissions[admissions['fold']!=1]
test = admissions[admissions['fold']==1]

model.fit(train[['gpa']], train['actual_label'])
test['labels'] = model.predict(test[['gpa']])
matches = test['labels'] == test['actual_label']
iteration_one_accuracy = len(test[matches]) / len(test)
print(iteration_one_accuracy)

## 4. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
from sklearn.linear_model import LogisticRegression

fold_ids = [1,2,3,4,5]

def train_and_test(df, ids):
    model = LogisticRegression()
    accuracy_list = []
    for i in ids:
        train = df[df['fold']!=i]
        test = df[df['fold']==i]
        
        model.fit(train[['gpa']], train['actual_label'])
        test['labels'] = model.predict(test[['gpa']])
        matches = test['labels'] == test['actual_label']
        iteration_accuracy = len(test[matches]) / len(test)
        accuracy_list.append(iteration_accuracy)
    
    return accuracy_list

accuracies = train_and_test(admissions, fold_ids)
print(accuracies)
average_accuracy = np.mean(accuracies)
print(average_accuracy)


## 5. Sklearn ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

lr = LogisticRegression()

# kf = KFold(n, n_folds, shuffle=False, random_state=None)
#n is the number of observations in the dataset,
#n_folds is the number of folds you want to use,
#shuffle is used to toggle shuffling of the ordering of the observations in the dataset,
#random_state is used to specify a seed value if shuffle is set to True.
kf = KFold(len(admissions), 5, shuffle=True, random_state=8)

#cross_val_score(estimator, X, Y, scoring=None, cv=None)
#estimator is a sklearn model that implements the fit method (e.g. instance of LinearRegression or LogisticRegression),
#X is the list or 2D array containing the features you want to train on,
#Y is a list containing the values you want to predict (target column),
#scoring is a string describing the scoring criteria (list of accepted values here).
#cv describes the number of folds. Here are some examples of accepted values:
    #an instance of the KFold class,
    #an integer representing the number of folds.
accuracies = cross_val_score(lr, admissions[['gpa']], admissions['actual_label'], scoring='accuracy', cv=kf)
print(accuracies)

average_accuracy = np.mean(accuracies)
print(average_accuracy)
