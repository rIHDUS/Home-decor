#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

Firstname=form.getvalue("firstname")
Middlename=form.getvalue("middlename")
Lastname=form.getvalue("lastname")
Mothername=form.getvalue("mothername")
Age=form.getvalue("age")
Dob=form.getvalue("dob")
Bloodgroup=form.getvalue("bloodgroup")
Doct_refference=form.getvalue("refference")
Gender=form.getvalue("gender")
Mobile=form.getvalue("mobno")
Email=form.getvalue("email")
Address=form.getvalue("addrs")
Altaddrs=form.getvalue("altaddrs")


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor(dictionary=True)

query=f"""INSERT INTO patient (firstname,middlename,lastname,mothername,age,dob,bloodgroup,doct_refference,gender,mobno,email,addrs,altaddrs) VALUES ('{Firstname}','{Middlename}','{Lastname}','{Mothername}','{Age}','{Dob}','{Bloodgroup}','{Doct_refference}','{Gender}','{Mobile}','{Email}','{Address}','{Altaddrs}')"""
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Patient Register Successfully !!!");
    location.href="dashboard.py";
</script>''')