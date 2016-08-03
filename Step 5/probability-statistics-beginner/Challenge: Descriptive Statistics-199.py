## 1. Introduction ##

import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)
ax4.set_xlim(0,5.0)

ax1.hist(movie_reviews['RT_user_norm'])

ax2.hist(movie_reviews['Metacritic_user_nom'])

ax3.hist(movie_reviews['Fandango_Ratingvalue'])

ax4.hist(movie_reviews['IMDB_norm'])
plt.show()

## 2. Mean ##

def mean(col):
    return col.mean()

user_reviews = movie_reviews[['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']]
means = user_reviews.apply(mean)
rt_mean = means['RT_user_norm']
mc_mean = means['Metacritic_user_nom']
fg_mean = means['Fandango_Ratingvalue']
id_mean = means['IMDB_norm']
print(rt_mean)
print(mc_mean)
print(fg_mean)
print(id_mean)


## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    v = series.values
    m = v.mean()
    var = [(i-m)**2 for i in v]
    variance = sum(var) / len(var)
    return variance

rt_var = calc_variance(movie_reviews['RT_user_norm'])
rt_stdev = rt_var**(1/2)

mc_var = calc_variance(movie_reviews['Metacritic_user_nom'])
mc_stdev = mc_var**(1/2)

fg_var = calc_variance(movie_reviews['Fandango_Ratingvalue'])
fg_stdev = fg_var**(1/2)

id_var = calc_variance(movie_reviews['IMDB_norm'])
id_stdev = id_var**(1/2)

print("Rotten Tomatoes (variance):", rt_var)
print("Metacritic (variance):", mc_var)
print("Fandango (variance):", fg_var)
print("IMDB (variance):", id_var)

print("Rotten Tomatoes (standard deviation):", rt_stdev)
print("Metacritic (standard deviation):", mc_stdev)
print("Fandango (standard deviation):", fg_stdev)
print("IMDB (standard deviation):", id_stdev)

## 4. Scatter plots ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)

ax1.scatter(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])
ax2.scatter(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])
ax3.scatter(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])
plt.show()

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean
    
def calc_covariance(col1, col2):
    x = col1.values
    y = col2.values
    x_mean = calc_mean(col1)
    y_mean = calc_mean(col2)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)
    
    mul = x * y
    cov = mul / len(mul)
    return cov

rt_fg_covar = calc_covariance(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])
mc_fg_covar = calc_covariance(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])
id_fg_covar = calc_covariance(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])

print(rt_fg_covar, mc_fg_covar, id_fg_covar)


## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

def calc_correlation(col1, col2):
    return calc_covariance(col1,col2) / ((calc_variance(col1) ** (1/2)) * (calc_variance(col2) ** (1/2)))

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print(rt_fg_corr, mc_fg_corr, id_fg_corr)