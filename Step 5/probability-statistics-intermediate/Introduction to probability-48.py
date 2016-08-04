## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = ''.join(flags.sort_values('bars', ascending=False).head(1)['name'].values)
print(most_bars_country)
highest_population_country = ''.join(flags.sort_values('population', ascending=False).head(1)['name'].values)
print(highest_population_country)


## 2. Calculating probability ##

total_countries = flags.shape[0]
count=0
for i in flags['orange']:
    if i == 1:
        count+=1
orange_probability = count / total_countries

stripe = len([i for i in flags['stripes'] if i>1])
stripe_probability = stripe/total_countries

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5

ten_heads = 1 / (2**10)
hundred_heads = 1 / (2**100)

## 4. Dependent probabilities ##

# Remember that whether a flag has red in it or not is in the `red` column.
total_countries = flags.shape[0]
countries_with_red_flag = flags[flags['red'] == 1].shape[0]
three_red = 1
for i in range(3):
    three_red*=((countries_with_red_flag-i) / (total_countries-i))
print(three_red)


## 5. Disjunctive probability ##

start = 1
end = 18000
count = 0
for i in range(start,end+1):
    if i%100 == 0:
        count+=1
hundred_prob = count/end

c = 0
for i in range(start,end+1):
    if i%70 == 0:
        c+=1
seventy_prob = c/end


## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None

total = flags.shape[0]
prob_red = flags[flags['red'] == 1].shape[0] / total
prob_orange = flags[flags['orange'] == 1].shape[0] / total
prob_both = flags[(flags['red'] == 1) & (flags['orange'] == 1)].shape[0] / total

red_or_orange = prob_red + prob_orange - prob_both

prob_stripes = flags[flags['stripes'] >= 1].shape[0] / total
prob_bars = flags[flags['bars'] >= 1].shape[0] / total
prob_b = flags[(flags['stripes'] >= 1) & (flags['bars'] >= 1)].shape[0] / total

stripes_or_bars = prob_stripes + prob_bars - prob_b

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
# '0.5*0.5*0.5' will represent all three tails
# Subtract it from '1' to get the final probability
heads_or = 1 - (0.5*0.5*0.5)