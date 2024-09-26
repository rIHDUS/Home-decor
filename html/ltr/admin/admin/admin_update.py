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

name = form.getvalue('name')
email = form.getvalue('email')
password = form.getvalue('password')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE register SET name = '{name}', email = '{email}', password = '{password}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Admin Record Updated Successfully !!!");
        location.href="adminlist.py";
    </script>''')