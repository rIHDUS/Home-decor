#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

age_group=form.getvalue("age_group")



mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor=mydb.cursor(dictionary=True)

query=f"""INSERT INTO add_age (age_group) VALUES ('{age_group}')"""
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Age added Successfully !!!");
    location.href="agelist.py";
</script>''')