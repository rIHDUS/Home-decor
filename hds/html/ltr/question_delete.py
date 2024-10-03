#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue('id')


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor=mydb.cursor()

query=f'''DELETE FROM question WHERE id={id}'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Question Record Delete Successfully !!!");
    location.href="questionlist1.py";
</script>''')