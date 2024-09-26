#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

# Retrieve form data and check for None values
def get_value(field):
    return form.getvalue(field) if form.getvalue(field) else ''

pat_age = get_value('agegroup')
ques = get_value('question')
opt1 = get_value('opt1')
opt2 = get_value('opt2')
opt3 = get_value('opt3')
opt4 = get_value('opt4')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor()

query = """INSERT INTO question (pat_age, ques, opt1, opt2, opt3, opt4) VALUES (%s, %s, %s, %s, %s, %s)"""

values = (pat_age, ques, opt1, opt2, opt3, opt4)

mycursor.execute(query, values)
mydb.commit()

print('''
<script>
    alert("!!! New Question Add Successfully !!!");
    location.href="questionlist.py";
</script>
''')
