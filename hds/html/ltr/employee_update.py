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

mobno=form.getvalue("mobno")
altmobno =form.getvalue("altmobno")
bnk_name  =form.getvalue("bnk_name")
bnk_branch =form.getvalue("bnk_branch")
acc_no =form.getvalue("acc_no")
ifsc_no=form.getvalue("ifsc_no")
aadhar = form.getvalue("aadhar")
email = form.getvalue("email")
addrs = form.getvalue("addrs")
altaddress = form.getvalue("altaddress")
dob = form.getvalue("dob")
education = form.getvalue("education")
password = form.getvalue("password")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE employee SET firstname = '{firstname}', middlename = '{middlename}', lastname = '{lastname}', mobno = '{mobno}', altmobno = '{altmobno}', bnk_name = '{bnk_name}', bnk_branch = '{bnk_branch}', acc_no = '{acc_no}', ifsc_no = '{ifsc_no}', aadhar = '{aadhar}', email = '{email}', addrs = '{addrs}', altaddress = '{altaddress}', dob = '{dob}', education = '{education}', password = '{password}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Employee Record Updated Successfully !!!");
        location.href="employeelist.py";
    </script>''')