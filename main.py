import pandas as pd

df = pd.read_csv('AAPL.csv')
df1=df['Adj Close'].diff()
df["daily change"]=df1
totalsum=df['daily change'].sum()
df2 = {'Date':'total daily change combined','daily change':totalsum}
df = df.append(df2, ignore_index = True)
print("total sum is",totalsum)
df.to_csv("AAPL.csv")






