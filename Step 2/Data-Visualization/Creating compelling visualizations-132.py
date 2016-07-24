## 1. Seaborn ##

import pandas as pd
births = pd.read_csv('births.csv')
print(births.head(10))
print(births.shape)

## 3. Seaborn styling ##

import seaborn as sns
plt.hist(births['agepreg'])
plt.show()

## 5. Customizing histogram: distplot() ##

sns.distplot(births['prglngth'], kde=False)
sns.axlabel('Pregnancy Length, weeks', 'Frequency')
sns.plt.show()

## 6. Practice: customizing distplot() ##

import seaborn as sns

sns.set_style('dark')
sns.distplot(births['birthord'], kde=False)
sns.axlabel('Birth Number','Frequency')
sns.plt.show()

## 7. Boxplots: boxplot() ##

births = pd.read_csv('births.csv')
sns.boxplot(x=births['birthord'], y=births['agepreg'])
sns.plt.show()

## 8. Pair plot: pairplot() ##

sns.pairplot(births[['agepreg', 'prglngth', 'birthord']])
sns.plt.show()