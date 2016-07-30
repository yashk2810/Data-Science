import pandas as pd
import sqlite3
import math

conn = sqlite3.connect('factbook.db')
query = "select * from facts;"
df = pd.read_sql_query(query,conn)
df = df.dropna(axis=0)

def estimate(row):
    return row['population']*((math.e)**(row['population_growth']*35))
    
df['pop_estimate'] = df.apply(estimate, axis=1)
sorted_estimate = df.sort_values('pop_estimate', axis=0,ascending=False)
print(sorted_estimate['name'][:10])

