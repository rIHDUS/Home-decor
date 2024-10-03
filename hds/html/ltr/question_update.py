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


question=form.getvalue("question")
option1=form.getvalue("option1")
option2=form.getvalue("option2")
option3=form.getvalue("option3")
option4=form.getvalue("option4")
coption=form.getvalue("coption")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE question SET  question = '{question}', option1 = '{option1}', option2 = '{option2}', option3 = '{option3}', option4 = '{option4}', coption = '{coption}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Question Record Updated Successfully !!!");
        location.href="questionlist1.py";
    </script>''')