import pandas as pd
df=pd.read_csv("placement_readiness.csv")
#first 5 rows
print(df.head())
#shape
print(df.shape)
#no of rows and colunns
print(f"NO of rows are {df.shape[0]} and no of columns are {df.shape[1]}")
#columns
print(df.columns)
#describe
print(df["SQL_Score"].describe())
print(df[["SQL_Score","Python_Score"]].describe())
#Python score > 75
print(df[df["Python_Score"]>75])
#sort Aptitude highest->lowest
sorted_Aptitude_df=df.sort_values("Aptitude_Score",ascending=False)
print(sorted_Aptitude_df)
#Show the students with the top 10 Python scores.
sorted_py_df=df.sort_values("Python_Score",ascending=False)
print(sorted_py_df.head(10))
