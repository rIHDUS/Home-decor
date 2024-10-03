#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor=mydb.cursor(dictionary=True)

# Get the question data from the database
query = "SELECT * FROM question"
mycursor.execute(query)
question = mycursor.fetchall()

# Print the HTML header
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>MCQ Questions</title>")
print("</head>")
print("<body>")

# Display the MCQ questions
print("<h1>MCQ Questions</h1>")
print("<form action='mcq.cgi' method='post'>")
for question in question:
    print("<p>{}<br>".format(question[1]))
    print("<input type='radio' name='q{}' value='A'> {}".format(question[0], question[2]))
    print("<input type='radio' name='q{}' value='B'> {}".format(question[0], question[3]))
    print("<input type='radio' name='q{}' value='C'> {}".format(question[0], question[4]))
    print("<input type='radio' name='q{}' value='D'> {}".format(question[0], question[5]))
    print("</p>")
print("<input type='submit' value='Submit Answers'>")
print("</form>")

# Check if the form has been submitted
if 'q1' in cgi.FieldStorage():
    # Get the submitted answers
    answers = cgi.FieldStorage()
    score = 0
    for id, answer in answers.items():
        query = "SELECT coption FROM question WHERE id = %s"
        cursor.execute(query, (id[1:],))
        coption = cursor.fetchone()[0]
        if answer.value == coption:
            score += 1
    print("<p>Your score is: {}</p>".format(score))

print("</body>")
print("</html>")

# Close the database connection
cursor.close()
cnx.close()