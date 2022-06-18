import pandas as pd
import names as nm

df=pd.DataFrame()
pid=pd.Series([])
fnme=pd.series([])
lnme=pd.series([])

rcdcnt=input('Enter number of records')

#For Mem PID

j=900000000000001
for i in range(int(rcdcnt)):
    j=j+1
    pid[i]=j
    fnme[i]=nm.get_first_name()
    lnme[i]=nm.get_last_name()

df.insert(0,"PID",pid,allow_duplicates=True)
df.insert(1,"First_name",fnme,allow_duplicates=True)
df.insert(1,"Last_name",lnme,allow_duplicates=True)
print(df.head())
