import pandas as pd


airfile = './air_data.csv'

df = pd.read_csv(airfile)
df = df.dropna()
index1 = df["SUM_YR_1"] != 0
index2 = df["SUM_YR_2"] != 0
index3 = (df["SEG_KM_SUM"] == 0) & (df["avg_discount"] == 0)
df = df[index1 | index2| index3]
print(index3)
print(df.shape)
print(df.info())
df.to_csv('./data_cleaned.csv')

