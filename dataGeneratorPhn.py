import cx_Oracle
import os
import re
from pathlib import Path
import pandas as pd
import random as rd
import datetime as dt

wrd='PVS'

dftmp=pd.DataFrame()
df1=pd.DataFrame()
phn=pd.series()
cons=pd.series()
xpath=r'C:\Users\Arun\Desktop'

username=str(input('Enter Username \n'))
password=str(input('Enter Password \n'))
dbsave=str(input('Enter DB service name \n'))
query=str(input('Enter query \n'))

LDAP={'ODS SYS':'iodssys','MDM SYS':'imdmsys','REG SYS OLD':'iregsys','REG SYS NEW':'ibregsys','ODS INT':'iodsint','MDM INT':'imdmint','REG INT OLD':'iregint','REG INT NEW':'ibregint',
      'ODS PVS':'lshpvs05-scan.sys.cigna.com:1521/iodspvs_etl.cigna.com','MDM PVS':'lshpvs05-scan.sys.cigna.com:1521/imdmpvs_ea.cigna.com','REG PVS OLD':'iregpvs','REG PVS NEW':'ibregpvs'}


def DbConnect(databaseName):
    os.environ['TNS_ADMIN']=r'C:\Users\Arun\Desktop'
    try:
        connection=cx_Oracle.connect(username,password,databaseName)
        cursor=connection.cursor()
        dftmp=pd.read_sql_query(query,connection)
    except:
        if(cx_Oracle.DatabaseError):
            m_box.showwarning("Error occurred in Oracle","Please check UserName or Password or Query")
        finally:
            cursor.close()
            connection.close()
        return dftmp

def DbConnection(databaseName):
    os.environ['TNS_ADMIN']=''
    try:
        connection=cx_Oracle.connect(username,password,databaseName)
        cursor=connection.cursor()
        dftmp=pd.read_sql_query(query,connection)
    except:
        if(cx_Oracle.DatabaseError):
            m_box.showwarning("Error occurred in Oracle","Please check UserName or Password or Query")
        finally:
            cursor.close()
            connection.close()
        return dftmp

for k,v in LDAP.items():
    if(dbsave == k):
        if wrd in k:
            dbname=v
            df1=DbConnection(dbname)
        else:
            dbname=v
            df1=DbConnect(dbname)

print('outside :',dbsave,dbname)
print('After query :',dt.datetime.now())

for i in range(len(df1)):
    phn[i]=rd.randint(1000000000,9999999999)
    if df1["INDIV_ENTERPRISE_ID"][i]%10==1:
        cons[i]='IAD,12,indiv-tos-phn'
    elif df1["INDIV_ENTERPRISE_ID"][i]%10==2:
        cons[i]='HEV,5,hev-self-phn'
    elif df1["INDIV_ENTERPRISE_ID"][i]%10==3:
        cons[i]='CCV,5,ccv-self-phn'
    elif df1["INDIV_ENTERPRISE_ID"][i]%10==4:
        cons[i]='IAD,12,indiv-hra-phn'
    elif df1["INDIV_ENTERPRISE_ID"][i]%10==5:
        cons[i]='IAD,12,indiv-autodialer-phn'
    else:
        cons[i]='IAD,12,indiv-pref-phn'

print('After phone list:',dt.datetime.now())

df1.insert(1,"consumer,version,pref-phn",cons,allow_duplicates=True)
df1.insert(2,"PH_NUM",cons,allow_duplicates=False)

print('After phone list in dataframe:'dt.datetime.now())

print(len(df1))
print(df1.head())
print(df1.tail())

path=xpath+"\CSVExport.xlsx"
df1.to_csv(path,index=False,sep=',')
      

