## 1. Introduction to the Data ##

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")

model = LogisticRegression()
model.fit(admissions[["gpa"]], admissions["admit"])
labels = model.predict(admissions[['gpa']])
admissions['predicted_label'] = labels
print(admissions['predicted_label'].value_counts())
print(admissions.head(10))
print(admissions.shape)

## 2. Accuracy ##

labels = model.predict(admissions[["gpa"]])
admissions["predicted_label"] = labels
# one more way to rename a column is to
# assign the old column to a new column and drop the old column
admissions.columns = ['actual_label', 'gpa', 'gre', 'predicted_label']

matches = admissions['actual_label'] == admissions['predicted_label']
correct_predictions = admissions[matches == True]
print(correct_predictions)
accuracy = correct_predictions.shape[0] / admissions.shape[0]
print(accuracy)

## 3. Binary classification outcomes ##

tp = admissions[(admissions['predicted_label'] == 1) & (admissions['actual_label'] == 1)]
true_positives = len(tp)

tn = admissions[(admissions['predicted_label'] == 0) & (admissions['actual_label'] == 0)]
true_negatives = len(tn)

print(true_positives)
print(true_negatives)

## 4. Sensitivity ##

# From the previous screen
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])

fn = admissions[(admissions['predicted_label'] == 0) & (admissions['actual_label'] == 1)]
false_negatives = len(fn)

# sensitivity = The fraction of students that were correctly admitted
# In this case only 12.7% of students were correctly admitted
sensitivity = true_positives / (true_positives + false_negatives)
print(sensitivity)

## 5. Specificity ##

# From previous screens
true_positive_filter = (admissions["predicted_label"] == 1) & (admissions["actual_label"] == 1)
true_positives = len(admissions[true_positive_filter])
false_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 1)
false_negatives = len(admissions[false_negative_filter])
true_negative_filter = (admissions["predicted_label"] == 0) & (admissions["actual_label"] == 0)
true_negatives = len(admissions[true_negative_filter])

fp = admissions[(admissions['predicted_label'] == 1) & (admissions['actual_label'] == 0)]
false_positives = len(fp)

# Specificity = the fraction of students that were correctly rejected
# In this case 96.25% were correctly rejected
specificity = true_negatives / (true_negatives + false_positives)
print(specificity)
