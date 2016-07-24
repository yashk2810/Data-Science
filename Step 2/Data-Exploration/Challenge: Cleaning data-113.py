## 4. Filter out the bad years ##

import matplotlib.pyplot as plt
%matplotlib inline
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] >= 1960]
true_avengers['Year'].hist()

## 5. Consolidating deaths ##

def number_of_deaths(row):
    count = 0
    if row['Death1'] == 'YES':
        count+=1
    if row['Death2'] == 'YES':
        count+=1
    if row['Death3'] == 'YES':
        count+=1
    if row['Death4'] == 'YES':
        count+=1
    if row['Death5'] == 'YES':
        count+=1
    return count

true_avengers['Deaths'] = true_avengers.apply(number_of_deaths, axis=1)
print(true_avengers['Deaths'])

## 6. Years since joining ##

joined_accuracy_count  = int()

correct = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]

joined_accuracy_count = len(correct)
print(joined_accuracy_count)