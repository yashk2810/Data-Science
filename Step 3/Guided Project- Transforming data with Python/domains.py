import read

df = read.load_data()
print(df['url'].value_counts().head(100))