#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
aid=form.getvalue('aid')
#print(id)

age_group=form.getvalue("age_group")


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE add_age SET age_group = '{age_group}' WHERE aid = {aid}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Patient Record Updated Successfully !!!");
        location.href="agelist.py";
    </script>''')