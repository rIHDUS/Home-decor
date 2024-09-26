#!C:\Python312\Python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

form=cgi.FieldStorage()
# print(form)

email=form.getvalue('username')
# print(username)
password=form.getvalue('password')
# print(password)

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hds"
)
mycursor=mydb.cursor()

query=f"""SELECT * FROM register WHERE email='{email}' AND password='{password}'"""
# print(query)

mycursor.execute(query)

myresult=mycursor.fetchone()
# print(myresult)
mydb.commit()

if mycursor.rowcount==1:
  print(f'''
        <script>
        localStorage.setItem('email','{myresult[1]}');
        localStorage.setItem('id','{myresult[0]}');
        </script>
        ''')
  print(f'''
    <script>alert("Logged in as {myresult[1]}");
    location.href="dashboard.py";
    </script>''')
else:
  print(f'''
    <script>alert("Something went wrong.!!");
    location.href="login.py";
    </script>''')
