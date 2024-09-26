#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

username=form.getvalue("username")
email=form.getvalue("email")
password=form.getvalue("password")
    
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor()

query=f'''INSERT INTO register (name,email,password) VALUES ('{username}','{email}','{password}')'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Register Successfully !!!");
    location.href="login.py";
</script>''')