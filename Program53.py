# creation of data frames
import pandas as pd 
data={"name":["Ankush","Krishn","Radha"],
      "Age":[24,56,76],
      "Salary":[300000,45000,34555]},
df=pd.DataFrame(data)
print(df)

# to open excel file
da=pd.read_excel("C:/Users/dwive/OneDrive/Desktop.xlsx")
print(da)

# to entr the csv file
p=pd.read_csv("C:/Users/dwive/OneDrive/Desktop/Oasis Infobyte Internship/Car_price_prediction.csv") # while coping a path always use back (/) slashes.
print(p)
