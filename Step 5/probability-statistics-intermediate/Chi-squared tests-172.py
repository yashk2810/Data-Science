## 2. Calculating differences ##

female_diff = (10771 - 16280.5) / 16280.5

male_diff = (21790 - 16280.5) / 16280.5

## 3. Updating the formula ##

female_diff = ((10771 - 16280.5) ** 2) / 16280.5
male_diff = ((21790 - 16280.5) ** 2) / 16280.5

gender_chisq = female_diff + male_diff
print(gender_chisq)

## 4. Generating a distribution ##

from numpy.random import random
import matplotlib.pyplot as plt
chi_squared_values = []

def count(no, x):
    c = 0
    for i in no:
        if i==x:
            c+=1
    return c

for i in range(1000):
    no = random((32561,))
    for n in range(len(no)):
        if no[n]<0.5:
            no[n]=0
        else:
            no[n]=1
    male_diff = ((count(no, 0) - 16280.5) ** 2) / 16280.5
    female_diff = ((count(no, 1) - 16280.5) ** 2) / 16280.5
    
    chisq = male_diff + female_diff
    chi_squared_values.append(chisq)

plt.hist(chi_squared_values)


## 6. Smaller samples ##

female_diff = (107.71 - 162.805) ** 2 / 162.805
male_diff = (217.90 - 162.805) ** 2 / 162.805

gender_chisq = male_diff + female_diff


## 7. Sampling distribution equality ##

from numpy.random import random
import matplotlib.pyplot as plt
chi_squared_values = []

def count(no, x):
    c = 0
    for i in no:
        if i==x:
            c+=1
    return c

for i in range(1000):
    no = random((300,))
    for n in range(len(no)):
        if no[n]<0.5:
            no[n]=0
        else:
            no[n]=1
    male_diff = ((count(no, 0) - 150) ** 2) / 150
    female_diff = ((count(no, 1) - 150) ** 2) / 150
    
    chisq = male_diff + female_diff
    chi_squared_values.append(chisq)

plt.hist(chi_squared_values)

## 9. Increasing degrees of freedom ##

diffs = []
observed = [27816, 3124, 1039, 311, 271]
expected = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

for i, obs in enumerate(observed):
    exp = expected[i]
    diff = (obs - exp) ** 2 / exp
    diffs.append(diff)
    
race_chisq = sum(diffs)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

obs = [27816, 3124, 1039, 311, 271]
exp = [26146.5, 3939.9, 944.3, 260.5, 1269.8]

chisq, race_pvalue = chisquare(obs, exp)
print(chisq, race_pvalue)