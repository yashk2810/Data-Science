## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
prob_over_5000 = bikes[bikes['cnt'] > 5000].shape[0] / bikes.shape[0]
print(prob_over_5000)

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def calc(n,k,p,q):
    num = math.factorial(n)
    den = math.factorial(n-k) * math.factorial(k)
    
    return ((p**k) * (q**(n-k))) * (num / den)
    
outcome_probs = []
p = 0.39
q = 0.61

for k in outcome_counts:
    outcome_probs.append(calc(30,k,p,q))
print(outcome_probs)

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

d = binom.pmf(outcome_counts, 30, 0.39)

plt.bar(outcome_counts, d)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None
dist_mean = 30 * 0.39
print(dist_mean)

## 9. Computing the standard deviation ##

dist_stdev = None
dist_stdev = (30 * 0.39 * 0.61) ** (1/2)
print(dist_stdev)

## 10. A different plot ##

# Enter your answer here.
import scipy
from scipy import linspace
from scipy.stats import binom

outcomes = linspace(0,10,11)
d = binom.pmf(outcomes,10, 0.39)
plt.bar(outcomes,d)
plt.show()

outcomes = linspace(0,100,101)
d = binom.pmf(outcomes,100, 0.39)
plt.bar(outcomes,d)
plt.show()


## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
dist = binom.cdf(outcome_counts, 30, 0.39)
plt.plot(outcome_counts, dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

left_16 = binom.cdf(16,30,0.39)
right_16 = 1 - left_16