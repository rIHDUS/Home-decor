#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

age=form.getvalue("age")
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

query=f"""INSERT INTO question (question,option1,option2,option3,option4,coption) VALUES ('{question}','{option1}','{option2}','{option3}','{option4}','{coption}')"""
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Question added Successfully !!!");
    location.href="questionlist1.py";
</script>''')