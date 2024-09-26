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

pat_age = form.getvalue('agegroup')
ques = form.getvalue('question')
opt1 = form.getvalue('opt1')
opt2 = form.getvalue('opt2')
opt3 = form.getvalue('opt3')
opt4 = form.getvalue('opt4')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE question SET pat_age = '{pat_age}', ques = '{ques}', opt1 = '{opt1}', opt2 = '{opt2}', opt3 = '{opt3}', opt4 = '{opt4}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Question Updated Successfully !!!");
        location.href="questionlist.py";
    </script>''')