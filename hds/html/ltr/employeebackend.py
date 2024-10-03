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
Mobile=form.getvalue("mobno")
Altmobno=form.getvalue("altmobno")
Bankname=form.getvalue("bnk_name")
Branch=form.getvalue("bnk_branch")
Accountno=form.getvalue("acc_no")
Ifscno=form.getvalue("ifsc_no")
Aadhar=form.getvalue("aadhar")
Email=form.getvalue("email")
Address=form.getvalue("addrs")
Altaddress=form.getvalue("altaddress")
Dob=form.getvalue("dob")
Education=form.getvalue("education")
Password=form.getvalue("password")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor()

query=f'''INSERT INTO employee (firstname,middlename,lastname,mobno,altmobno,bnk_name,bnk_branch,acc_no,ifsc_no,aadhar,email,addrs,altaddress,dob,education,password) VALUES ('{Firstname}','{Middlename}','{Lastname}','{Mobile}','{Altmobno}','{Bankname}','{Branch}','{Accountno}','{Ifscno}','{Aadhar}','{Email}','{Address}','{Altaddress}','{Dob}','{Education}','{Password}')'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Employee Register Successfully !!!");
    location.href="dashboard.py";
</script>''')