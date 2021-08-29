import cx_Oracle
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m_box
import os

HEIGHT = 500
WIDTH = 600

def comboclick():
    global dbsave
    dbsave=mycombo.get()
    return dbsave

def radioclick():
    rad=r.get()
    return rad

def button_click_event():
    username=entry1.get()
    password=entry2.get()
    query=entry3.get()
    xpath=entry4.get()
    tnspath=entry5.get()
    dbsave=comboclick()
    rad=radioclick()
    wrd='PVS'
    dftmp=pd.DataFrame()
    df1=pd.DataFrame()

    LDAP={'ODS SYS':'iodssys','MDM SYS':'imdmsys','REG SYS OLD':'iregsys','REG SYS NEW':'ibregsys','ODS INT':'iodsint','MDM INT':'imdmint','REG INT OLD':'iregint','REG INT NEW':'ibregint',
          'ODS PVS':'lshpvs05-scan.sys.cigna.com:1521/iodspvs_etl.cigna.com','MDM PVS':'lshpvs05-scan.sys.cigna.com:1521/imdmpvs_ea.cigna.com','REG PVS OLD':'iregpvs','REG PVS NEW':'ibregpvs'}

    def DbConnect(databaseName):
        os.environ['TNS_ADMIN']=str(tnspath)
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

    if(xpath==""):
        m_box.showwarning("Path Error","Path can not be NULL")

    if(tnspath==""):
        m_box.showwarning("TNS ADMIN Path Error","Path can not be NULL")

    if (rad==1):
        path=xpath+"\ExcelExport.xlsx"
        #print(path)
        df1.to_excel(path,index=False)
    else:
        path=xpath+"\ExcelExport.xlsx"
        #print(path)
        df1.to_csv(path,index=False,sep=',')

top=tk.Tk()
top.title("DB Extractor")

canvas=tk.Canvas(top,height=HEIGHT,width=WIDTH)
canvas.pack()

#bg colour from the HTML color pallete
frame=tk.Frame(top, bg='#99ccff')
frame.place(relx=0.025,rely=0.025,relwidth=0.95,relheight=0.95)

label1=tk.Label(frame, text="User ID",bg='gray')
label1.place(relx=0.10,rely=0.1,relwidth=0.10,relheight=0.05)

entry1=tk.Entry(frame, bg='white')
entry1.place(relx=0.25,rely=0.1,relwidth=0.20,relheight=0.05)

label2=tk.Label(frame, text="Password",bg='gray')
label2.place(relx=0.10,rely=0.17,relwidth=0.10,relheight=0.05)

entry2=tk.Entry(frame, bg='white',show='*')
entry2.place(relx=0.25,rely=0.17,relwidth=0.20,relheight=0.05)

label3=tk.Label(frame, text="Enter your query without semicolon ';'",bg='gray')
label3.place(relx=0.10,rely=0.25,relwidth=0.70,relheight=0.05)

entry3=tk.Entry(frame, bg='white')
entry3.place(relx=0.10,rely=0.30,relwidth=0.70,relheight=0.25)

label4=tk.Label(frame, text="Path =",bg='gray')
label4.place(relx=0.10,rely=0.57,relwidth=0.10,relheight=0.05)

entry4=tk.Entry(frame, bg='white')
entry4.place(relx=0.20,rely=0.57,relwidth=0.60,relheight=0.05)

label5=tk.Label(frame, text="TNS Admin Path =",bg='gray',anchor='w')
label5.place(relx=0.10,rely=0.75,relwidth=0.20,relheight=0.05)

entry5=tk.Entry(frame, bg='white')
entry5.place(relx=0.32,rely=0.75,relwidth=0.48,relheight=0.05)

#combobox for the db

options=["ODS SYS","MDM SYS","REG SYS OLD","REG SYS NEW","ODS INT","MDM INT","REG INT OLD","REG INT NEW","ODS PVS","MDM PVS","REG PVS OLD","REG PVS NEW"]
clicked= StringVar()
clicked.set(options[0])

mycombo=ttk.Combobox(frame,value=options)
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>",comboclick)
mycombo.place(relx=0.10,rely=0.65,relwidth=0.20,relheight=0.05)

r=IntVar()
r.set("2")

rad1=tk.Radiobutton(frame,text ="EXCEL",variable = r, value = 1,command = lambda :radioclick())
rad1.place(relx=0.60,rely=0.1,relwidth=0.10,relheight=0.05)

rad2=tk.Radiobutton(frame,text ="CSV",variable = r, value = 2,command = lambda :radioclick())
rad2.place(relx=0.60,rely=0.17,relwidth=0.10,relheight=0.05)

button=tk.Button(top,text ="Go.!",bg='gray',fg='white',command = lambda :button_click_event())
button.place(relx=0.35,rely=0.8,relwidth=0.30,relheight=0.05)

top.mainloop()
