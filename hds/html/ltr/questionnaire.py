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

# Get the age group
age = form.getvalue('age')

# Fetch the questions from the database
mycursor.execute("SELECT * FROM question WHERE age_group = age)
questions = mycursor.fetchall()

# Print the questionnaire
print("<h1>Questionnaire</h1>")
for i, question in enumerate(questions):
    print("<h2>Question " + str(i+1) + ": " + question['question'] + "</h2>")
    print("<form action='questionbackend.py' method='POST'>")
    print("<input type='hidden' name='age' value='" + age + "'>")
    print("<input type='hidden' name='question_id' value='" + str(question['id']) + "'>")
    print("<label>Option 1:</label><br>")
    print("<input type='radio' name='answer' value='" + question['option1'] + "'> " + question['option1'] + "<br>")
    print("<label>Option 2:</label><br>")
    print("<input type='radio' name='answer' value='" + question['option2'] + "'> " + question['option2'] + "<br>")
    print("<label>Option 3:</label><br>")
    print("<input type='radio' name='answer' value='" + question['option3'] + "'> " + question['option3'] + "<br>")
    print("<label>Option 4:</label><br>")
    print("<input type='radio' name='answer' value='" + question['option4'] + "'> " + question['option4'] + "<br>")
    print("<br><br>")
    print("<input type='submit' value='Submit'>")
    print("</form>")

# Print a link to the results page
print("<a href='results.py'>View Results</a>")