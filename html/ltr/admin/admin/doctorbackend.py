#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

firstname = form.getvalue("firstname")
middlename = form.getvalue("middlename")
lastname = form.getvalue("lastname")
number = form.getvalue("number")
email = form.getvalue("email")
experience = form.getvalue("experience")
degree = form.getvalue("degree")
otherdegree = form.getvalue("otherdegree")

    
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor()

query = f'''INSERT INTO doctor (firstname, middlename, lastname, number, email, experience, degree, otherdegree) 
VALUES ('{firstname}', '{middlename}', '{lastname}', '{number}', '{email}', '{experience}', '{degree}', '{otherdegree}')'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("Doctor registered.!!!");
    location.href="doctorlist.py";
</script>''')