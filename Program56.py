# working with missing data in values
import pandas as pd 
data=pd.read_csv("compnay1.csv")
print(data)
print(data.isnull().sum()) # how many null/ missing values are there
print(data.dropna()) # delete all null values
data["salary"]= data["salary"].replace(pd.nan,3000) # replace the value
print(data) 