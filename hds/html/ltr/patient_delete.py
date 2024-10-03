#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
pat_id=form.getvalue('pat_id')


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor()

query=f'''DELETE FROM patient WHERE id={pat_id}'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Patient Record Delete Successfully !!!");
    location.href="patientlist.py";
</script>''')