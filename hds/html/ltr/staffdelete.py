#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import os
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
sid=form.getvalue('sid')
#print(sid)
mydb=mysql.connector.connect(host="localhost",
user="root",
password="",
database="hds")
mycursor=mydb.cursor()
query=f'''DELETE FROM staff WHERE sid={sid}'''
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" Record Deleted Successfully !");
    location.href="stafflist.py";
    </script>''')