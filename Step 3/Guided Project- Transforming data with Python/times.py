import read
import pandas as pd
from datetime import *
from dateutil.parser import *

df = read.load_data()
l=[]
for i in df['submission_time'].values:
	l.append(parse(i).time().hour)

df['hours'] = pd.Series(l)
print(df['hours'].value_counts())


