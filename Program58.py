# group by 
import pandas as pd
data= pd.read_excel("Company1.xlsx")
print(data)
gp=data.groupby("Department").agg({"EmploymentID":"count"})
print(gp)
gp1=data.groupby("country","gender").agg({"age":"mean"}) 
print(gp1)