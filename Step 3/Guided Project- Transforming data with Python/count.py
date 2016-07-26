import read
import pandas as pd

df = read.load_data()
headline = df['headline'].dropna().str.lower()
print(pd.Series(' '.join(headline).split()).value_counts().head(100))