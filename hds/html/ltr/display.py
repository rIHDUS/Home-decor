#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)

def fetch_questions(age_group):
    mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor()

    mycursor.execute("SELECT id, question_text FROM questions WHERE age_group = %s", (age_group,))
    questions = mycursor.fetchall()

    mycursor.close()
    mydb.close()
    
    return questions

def fetch_options(question_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Use your MySQL password here
        database="hearing_test"
    )
    mycursor = mydb.cursor()

    cursor.execute("SELECT id, option_text FROM options WHERE question_id = %s", (question_id,))
    options = mycursor.fetchall()

    mycursor.close()
    db.close()
    
    return options

def main():
    form = cgi.FieldStorage()
    age_group = form.getvalue("age_group")

    questions = fetch_questions(age_group)

    print("Content-type: text/html\n")
    print("<html><body>")
    print("<h1>Hearing Test</h1>")
    print("<form action='/cgi-bin/submit_test.py' method='post'>")

    for question_id, question_text in questions:
        print(f"<div>")
        print(f"<p>{question_text}</p>")
        options = fetch_options(question_id)
        for option_id, option_text in options:
            print(f"<input type='radio' id='{question_id}_{option_id}' name='q{question_id}' value='{option_id}' required>")
            print(f"<label for='{question_id}_{option_id}'>{option_text}</label><br>")
        print(f"</div><br>")

    print("<input type='submit' value='Submit'>")
    print("</form>")
    print("</body></html>")

if __name__ == "__main__":
    main()
