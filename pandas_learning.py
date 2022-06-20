from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import numpy as np

tabA={'Pkey':[1,2,np.nan,1],
'Cval':['a','b','c','d']}
tabB={'Pkey':[1,2,3,np.nan],
'Cval':['a','b','c','e']}

tabA_df=pd.DataFrame(data=tabA)
tabB_df=pd.DataFrame(data=tabB)

# print(tabA_df.head())
# print(tabB_df.head())

tabJoin_df=tabA_df.merge(tabB_df,how='cross')

#print(tabJoin_df)

for col,row in tabA_df.items():
    print(row)
    print(col)
