#column transformation
import pandas as o 
df=o.read_excel("ESD.xlsx")
print(df)
df.loc[(df["bonus %"]==0),"getsBonus"]="no bonus" # transform column bonus
df.loc[(df["bonus %"]>0," getsBonus")]= "bonus" # transform column bonus
print(df.head(10))