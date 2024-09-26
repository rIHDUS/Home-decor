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

fname = form.getvalue('firstname')
mname = form.getvalue('middlename')
lname = form.getvalue('lastname')
mobno = form.getvalue('number')
email = form.getvalue('email')
experience = form.getvalue('experience')
degree = form.getvalue('degree')
otherdegree = form.getvalue('otherdegree')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE doctor SET firstname = '{fname}', middlename = '{mname}', lastname = '{lname}', number = '{mobno}', email = '{email}', experience = '{experience}', degree = '{degree}', otherdegree = '{otherdegree}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Doctor Record Updated Successfully !!!");
        location.href="doctorlist.py";
    </script>''')