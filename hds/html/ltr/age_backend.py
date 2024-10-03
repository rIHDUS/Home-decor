#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

age=form.getvalue("age")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor=mydb.cursor(dictionary=True)
if(age==a)

query=f"""SELECT * from question"""
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Patient Register Successfully !!!");
    location.href="dashboard.py";
</script>''')