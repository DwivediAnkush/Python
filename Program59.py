#merge,concatenate and join 
import pandas as pd
data1= {"emp ID":["E01","E02","E03","E04","E05"],"names":["Ram","shyaam","krishn","radha","ankush"]}
data2= {"emp ID":["E01","E02","E03","E04","E05"],"salary":[45000,50000,45000,43444,54333]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print()
print(df2)

#merge
print(pd.merge(df1,df2,on="emp ID"))
print(pd.merge(left=df1, right=df2, on= "Emp Id", how="left"))

#concatenate
print(pd.concat([df1,df2]))
