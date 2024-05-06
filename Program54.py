#exploring data in pandas
import pandas as pd 
data=pd.read_excel("ESd.xlsx")
print(data.head(10)) # read above 10 data
print(data.tail(10)) # read lower 10 data
