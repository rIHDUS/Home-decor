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

# Get the form data
age_group_id = form.getvalue("age_group_id")
questions = form.getlist("question")

# Get the correct answers from the database
mycursor.execute("SELECT * FROM question WHERE age_group_id = %s", (age_group_id,))
correct_answers = mycursor.fetchall()

# Initialize the score
score = 0

# Loop through the questions and check the answers
for i, question in enumerate(questions):
    correct_answer = correct_answers[i]["correct_answer"]
    if question == correct_answer:
        score += 1

# Calculate the percentage
percentage = (score / len(questions)) * 100

# Print the result
print(f"""
    <html>
    <head>
        <title>Test Result</title>
    </head>
    <body>
        <h1>Test Result</h1>
        <p>Your score is {score} out of {len(questions)} ({percentage:.2f}%)</p>
    </body>
</html>
""")

# Insert the result into the database
mycursor.execute("INSERT INTO test_results (age_group_id, score, percentage) VALUES (%s, %s, %s)", (age_group_id, score, percentage))
mydb.commit()

mydb.close()