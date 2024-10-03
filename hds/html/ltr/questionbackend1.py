import cgi
import cgitb
import mysql.connector

cgitb.enable()

print("Content-type: text/html\r\n\r\n")

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

# Create a cursor object
mycursor = mydb.cursor(dictionary=True)

# Get form data
form = cgi.FieldStorage()

# Get the age group and question ID
age = form.getvalue('age')
question_id = form.getvalue('question_id')
answer = form.getvalue('answer')

# Fetch the correct answer from the database
mycursor.execute("SELECT * FROM question WHERE id = %s", (question_id,))
question = mycursor.fetchone()

# Check if the answer is correct
if answer == question['correct_answer']:
    print("<h1>Correct answer!</h1>")
else:
    print("<h1>Incorrect answer.</h1>")

# Update the score in the database
mycursor.execute("UPDATE patient SET score = score + 1 WHERE age_group = %s", (age,))
mydb.commit()

# Fetch the updated score from the database
mycursor.execute("SELECT score FROM patient WHERE age_group = %s", (age,))
patient = mycursor.fetchone()

# Print the updated score
print("<h1>Score: " + str(patient['score']) + "</h1>")

# Print a link to the next question
print("<a href='questionnaire.py'>Next question</a>")