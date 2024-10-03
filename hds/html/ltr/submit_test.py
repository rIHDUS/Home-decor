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

# Get the user's answers from the form
answers = {}
for key in form.keys():
    if key.startswith("q"):
        answers[key] = form.getvalue(key)

# Get the correct answers from the database
query = "SELECT * FROM question"
mycursor.execute(query)
myresult = mycursor.fetchall()

# Calculate the score
score = 0
for x in myresult:
    if answers[f"q{x['id']}"] == x['coption']:
        score += 1

# Display the results
print(f"""
    <div class="page-wrapper">
        <div class="container-fluid">
            <div class="row">
                <div class="col-12">
                    <div class="card">
                        <div class="card-body">
                            <h4 class="card-title">Test Results</h4>
                            <p>You scored {score} out of {len(myresult)}.</p>
                            <table id="file_export" class="table table-striped table-bordered display">
                                <thead>
                                    <tr>
                                        <th>Question</th>
                                        <th>Your Answer</th>
                                        <th>Correct Answer</th>
                                    </tr>
                                </thead>
                                <tbody>
""")

for x in myresult:
    print(f"""
        <tr>
            <td>{x['question']}</td>
            <td>{answers[f"q{x['id']}"]}</td>
            
           
            <td>{x['coption']}</td>
        </tr>
    """)

print("""
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")