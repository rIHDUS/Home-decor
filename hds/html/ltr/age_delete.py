#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
aid=form.getvalue('aid')


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor=mydb.cursor()

query=f'''DELETE FROM add_age WHERE aid={aid}'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! age Record Delete Successfully !!!");
    location.href="agelist.py";
</script>''')