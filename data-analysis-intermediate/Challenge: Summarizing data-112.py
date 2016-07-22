## 2. College majors and employment ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
all_ages.head(5)

## 3. Summarizing major categories ##

# All values for Major_category
all_ages_category = all_ages['Major_category'].value_counts().index
recent_grads_category = recent_grads['Major_category'].value_counts().index

all_ages_major_categories = dict()
recent_grads_major_categories = dict()

for i in all_ages_category:
    each_category = all_ages.loc[all_ages["Major_category"] == i]
    total_sum = sum(each_category["Total"])
    all_ages_major_categories[i] = total_sum
    
for i in recent_grads_category:
    each_category = recent_grads.loc[recent_grads["Major_category"] == i]
    total_sum = sum(each_category["Total"])
    recent_grads_major_categories[i] = total_sum

## 4. Low wage jobs rates ##

low_wage_percent = 0.0
low_wage_percent = sum(recent_grads["Low_wage_jobs"]) / sum(recent_grads["Total"])

## 5. Comparing datasets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].value_counts().index

recent_grads_lower_unemp_count = 0
all_ages_lower_unemp_count = 0

for major in majors:
    recent = recent_grads.loc[recent_grads['Major'] == major]
    a = all_ages.loc[all_ages['Major'] == major]
    
    if recent["Unemployment_rate"].values[0] < a['Unemployment_rate'].values[0]:
        recent_grads_lower_unemp_count+=1
    elif recent["Unemployment_rate"].values[0] > a['Unemployment_rate'].values[0]:
        all_ages_lower_unemp_count+=1