import pandas as pd 
import numpy as np

titanic = pd.read_csv("train.csv")

titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1

titanic['Embarked'] = titanic['Embarked'].fillna('S')

titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

# Generating a familysize column
titanic["FamilySize"] = titanic["SibSp"] + titanic["Parch"]

# The .apply method generates a new series
titanic["NameLength"] = titanic["Name"].apply(lambda x: len(x))

import re

# A function to get the title from a name.
def get_title(name):
    # Use a regular expression to search for a title.  Titles always consist of capital and lowercase letters, and end with a period.
    title_search = re.search(' ([A-Za-z]+)\.', name)
    # If the title exists, extract and return it.
    if title_search:
        return title_search.group(1)
    return ""

# Get all the titles and print how often each one occurs.
titles = titanic["Name"].apply(get_title)

# Map each title to an integer.  Some titles are very rare, and are compressed into the same codes as other titles.
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2}
for k,v in title_mapping.items():
    titles[titles == k] = v

# Add in the title column.
titanic["Title"] = titles






titanic_test = pd.read_csv("test.csv")

titanic_test['Age'] = titanic_test['Age'].fillna(titanic['Age'].median())

titanic_test.loc[titanic_test['Sex'] == 'male', 'Sex'] = 0
titanic_test.loc[titanic_test['Sex'] == 'female', 'Sex'] = 1

titanic_test['Embarked'] = titanic_test['Embarked'].fillna('S')
titanic_test.loc[titanic_test['Embarked'] == 'S', 'Embarked'] = 0
titanic_test.loc[titanic_test['Embarked'] == 'C', 'Embarked'] = 1
titanic_test.loc[titanic_test['Embarked'] == 'Q', 'Embarked'] = 2

titanic_test['Fare'] = titanic_test['Fare'].fillna(titanic_test['Fare'].median())

titles_test = titanic_test["Name"].apply(get_title)
# We're adding the Dona title to the mapping, because it's in the test set, but not the training set
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8, "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2, "Dona": 10}
for k,v in title_mapping.items():
    titles_test[titles_test == k] = v
titanic_test["Title"] = titles_test







predictors = ["Pclass", "Sex", "Fare", "Title", "Age", "Parch", "SibSp", "Embarked"]


alg = RandomForestClassifier(random_state=1, n_estimators=250, min_samples_split=8, min_samples_leaf=4)

#alg.fit(titanic[predictors], titanic['Survived'])
#predictions = alg.predict(titanic_test[predictors])

kf = cross_validation.KFold(titanic.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, titanic[predictors], titanic['Survived'], cv=kf)
print(scores.mean())

# predictions = predictions.astype(int)
# submission = pd.DataFrame({'PassengerId':titanic_test['PassengerId'], 'Survived':predictions})
# submission.to_csv("kaggle.csv", index=False)

