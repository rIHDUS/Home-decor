#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue('id')
#print(id)

firstname=form.getvalue("firstname")
middlename=form.getvalue("middlename")
lastname=form.getvalue("lastname")
mothername = form.getvalue("mothername")
age=int(form.getvalue("age"))
dob =form.getvalue("dob")
bloodgroup  =form.getvalue("bloodgroup")
doct_refference =form.getvalue("refference")
gender =form.getvalue("gender")
mobno=form.getvalue("mobno")
email = form.getvalue("email")
addrs = form.getvalue("addrs")
altaddress = form.getvalue("altaddrs")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE patient SET firstname = '{firstname}', middlename = '{middlename}', lastname = '{lastname}', mothername = '{mothername}', age = {age}, dob = '{dob}', bloodgroup = '{bloodgroup}', doct_refference = '{doct_refference}', gender = '{gender}', mobno='{mobno}', email = '{email}', addrs = '{addrs}', altaddrs = '{altaddress}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Patient Record Updated Successfully !!!");
        location.href="patientlist.py";
    </script>''')