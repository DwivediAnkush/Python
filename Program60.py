#pandas - pivoting and melting data frames
import pandas as pd
dict={"keys":["k1","k2","k1","k2"],"Names":["Jon","ben","Davis","petr"],
      "Houses":["red","blue","green","red"]}
df=pd.DataFrame(dict)
print(df)
print(df.pivot(index="keys",columns="Names",values=["houses"]))

#melting
print(pd.melt(df,id_vars=["Names"], value_vars=["houses"]))