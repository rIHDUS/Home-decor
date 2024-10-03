#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-type: text/html\n")

form = cgi.FieldStorage()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor = mydb.cursor(dictionary=True)

score = 0

for key in form.keys():
    if key.startswith('q'):
        question_id = int(key[1:])  # extract the question ID from the radio button name
        selected_option = form.getvalue(key)  # get the selected option value

        # query the database to get the correct answer for the question
        qquery = "SELECT * FROM question WHERE id = %s"
        mycursor.execute(qquery, (question_id,))
        question_data = mycursor.fetchone()

        if selected_option == question_data['option1'] and question_data['coption'] == 'option1':
            score += 1
        elif selected_option == question_data['option2'] and question_data['coption'] == 'option2':
            score += 1
        elif selected_option == question_data['option3'] and question_data['coption'] == 'option3':
            score += 1
        elif selected_option == question_data['option4'] and question_data['coption'] == 'option4':
            score += 1

print(f"""
    <html>
    <head>
        <title>Audiology Test Result</title>
    </head>
    <body>
        <h1>Your score is: {score}</h1>
        <p>You answered {score} questions correctly.</p>
        <p><a href="consultation.py">Proceed to consultation</a></p>
    </body>
    </html>
""")