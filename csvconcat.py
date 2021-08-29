import pandas as pd

df1=pd.DataFrame()
df2=pd.DataFrame()

df1=pd.read_excel(r'C:\Users\Arun\Desktop\concat\file1.xlsx',header=0)
df2=pd.read_excel(r'C:\Users\Arun\Desktop\concat\file2.xlsx',header=0)
df3=pd.read_excel(r'C:\Users\Arun\Desktop\concat\file3.xlsx',header=0)
#df3=pd.concat([df1,df2])
df4=pd.merge(df1,df2,on='MemID',how='left')
df5=df1.compare(df3,keep_shape=True)


#df3.to_excel(r'C:\Users\Arun\Desktop\concat\file4.xlsx',index=False)
print(df5)
