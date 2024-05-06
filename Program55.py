#Handling duplicate values
import pandas as pd 
data = pd.read_csv("company1.csv")
print(data["employmentID"].duplicate().sum()) # check how many duplicates are there
print(data.drop_duplicates("employmentId")) # remove duplicates