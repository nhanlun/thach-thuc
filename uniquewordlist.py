import pandas as pd 

df = pd.read_csv("word list.csv", dtype=str, encoding='latin-1')
keywords = df['Keyword'].dropna().values.tolist()

keywords = list(set(keywords))

df = pd.DataFrame({'Keyword': keywords})
df.to_csv("word list.csv", index=False)