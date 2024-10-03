#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
emp_id=form.getvalue('emp_id')


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor()

query=f'''DELETE FROM emloyee WHERE id={emp_id}'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Employee Record Delete Successfully !!!");
    location.href="employeelist.py";
</script>''')