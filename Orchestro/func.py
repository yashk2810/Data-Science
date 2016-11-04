import pandas as pd
import numpy as np
import math

df = pd.read_csv('Test2.csv')

df['WEEK_END_DATE'] = pd.to_datetime(df['WEEK_END_DATE'], format="%d-%m-%Y")
#print(df.dtypes)

df['Week'] = df['WEEK_END_DATE'].dt.week
df['Year'] = df['WEEK_END_DATE'].dt.year


def predict(ids):
	d_2013 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2013)]['POS_QTY']
	d_2014 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2014)]['POS_QTY']
	d_2015 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2015)]['POS_QTY']
	d_2016 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY']

	std_2013 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2013)]['POS_QTY'].std()
	std_2014 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2014)]['POS_QTY'].std()

	length_2015 = len(df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2015)]['POS_QTY'])
	std_2015 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2015)]['POS_QTY'].std()

	length_2016 = len(df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY'])
	if length_2016<=10:
		std_2016 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY'][:length_2016].std()
	else:
		std_2016 = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY'][:length_2016-9].std()

	d = {}
	d['2013'] = [std_2013, len(d_2013)]
	d['2014'] = [std_2014, len(d_2014)]
	d['2015'] = [std_2015, len(d_2015)]
	d['2016'] = [std_2016, len(d_2016)]

	count = 0
	avg_std = 0
	for key, value in d.items():
		if value[1]>1:
			avg_std+=value[0]
			count+=1
	avg_std/=count

	#print(std_2013, std_2014, std_2015, std_2016)

	if length_2015<9 or length_2016<9:
		if length_2015!=0 and length_2016!=0:
			minimum_length = min(length_2015, length_2016)
			actual = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY'][length_2016-minimum_length :length_2016]
			predicted = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2015)]['POS_QTY'][length_2015-minimum_length:length_2015] + avg_std
			predicted = np.floor(predicted)

			if sum(actual.values) == 0:
				mae = sum(predicted.values) * 100
			else:
				mae = (abs((sum(actual.values) - sum(predicted.values))) / sum(actual)) * 100
			return(predicted.values, actual.values, mae, ids, 228, sum(actual.values), sum(predicted.values))
		else:
			return ('NaN', 'NaN', 'No entries available', ids, 228, 'Nan', 'Nan')

	elif length_2015 > length_2016:
		actual = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY'][length_2016-9:length_2016]
		predicted = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2015)]['POS_QTY'][length_2016-9:length_2016] + avg_std
		predicted = np.floor(predicted)
		
		if sum(actual.values) == 0:
			mae = sum(predicted.values) * 100
		else:
			mae = (abs((sum(actual.values) - sum(predicted.values))) / sum(actual)) * 100

		return(predicted.values, actual.values, mae, ids, 228, sum(actual.values), sum(predicted.values))
	else:
		actual = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2016)]['POS_QTY'][length_2016-9:length_2016]
		predicted = df[(df['GNL_STR_NBR_ID']==ids) & (df['Year']==2015)]['POS_QTY'][length_2015-9:length_2015] + avg_std
		predicted = np.floor(predicted)
		
		if sum(actual.values) == 0:
			mae = sum(predicted.values) * 100
		else:
			mae = (abs((sum(actual.values) - sum(predicted.values))) / sum(actual)) * 100

		return(predicted.values, actual.values, mae, ids, 228, sum(actual.values), sum(predicted.values))

uniques = df['GNL_STR_NBR_ID'].unique()
error=[]
for i in uniques:
	pre, act, e, store_id, item_id, sum_actual, sum_predict = predict(i)
	error.append({'Predicted': pre, 'Actual': act, 'Error': e, 'Store_id': store_id, 'Item_id': item_id, 'Sum Actual': sum_actual, 'Sum Predicted': sum_predict})

submission = pd.DataFrame(error)
submission.to_csv("yash_katariya2.csv", index=False)



