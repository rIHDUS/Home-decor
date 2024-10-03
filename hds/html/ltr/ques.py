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

# Fetch age groups from backend file
add_age_query = "SELECT * FROM add_age"
mycursor.execute(add_age_query)
add_age = mycursor.fetchall()

# Fetch questions for each age group
questions_query = "SELECT * FROM question"
mycursor.execute(questions_query)
question = mycursor.fetchall()

# Create a dictionary to store questions for each age group
add_age_questions = {}
for add_age in add_age:
   add_age_questions[add_age['aid']] = []

for question in question:
    if question['id'] in add_age_questions:
        add_age_questions[question['id']].append(question)
print(f"""
    <html>
    <head>
        <title>MCQ Test</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f0f0;
            }}
            .page-wrapper {{
                display: flex;
                flex-direction: column;
                align-items: center;
                height: 100vh;
                padding: 20px;
                box-sizing: border-box;
            }}
            .container-fluid {{
                width: 100%;
                max-width: 800px;
                padding: 20px;
                box-sizing: border-box;
                background-color: #fff;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 4px;
            }}
            .card {{
                margin-bottom: 20px;
            }}
            .card-body {{
                padding: 20px;
                box-sizing: border-box;
            }}
            .card-title {{
                font-size: 24px;
                margin-bottom: 20px;
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th, td {{
                text-align: left;
                padding: 10px;
                border: 1px solid #ddd;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: normal;
                font-size: 14px;
                color: #333;
            }}
            td {{
                font-size: 14px;
                color: #666;
            }}
            input[type="radio"] {{
                margin-right: 10px;
            }}
            input[type="submit"] {{
                display: block;
                width: 100%;
                padding: 10px;
                background-color: #4CAF50;
                color: #fff;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }}
            input[type="submit"]:hover {{
                background-color: #3e8e41;
            }}
        </style>
    </head>
    <body>
        <div class="page-wrapper">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">MCQ Test</h4>
                                <form action="submit_test1.py" method="post">
                                    <table id="file_export" class="table table-striped table-bordered display">
                                        <thead>
                                            <tr>
                                                <th>Age Group</th>
                                                <th>Question</th>
                                                <th>Options</th>
                                            </tr>
                                        </thead>
                                        <tbody>
""")

for add_age in add_age:
    print(f"""
                                            <tr>
                                                <td colspan="3">{add_age['name']}</td>
                                            </tr>
    """)
    for question in add_age_question[add_age['id']]:
        print(f"""
                                            <tr>
                                                <td></td>
                                                <td>{question['question']}</td>
                                                <td>
                                                    <input type="radio" name="q{question['id']}" value="{question['option1']}"> {question['option1']} <br>
                                                    <input type="radio" name="q{question['id']}" value="{question['option2']}"> {question['option2']}<br>
                                                    <input type="radio" name="q{question['id']}" value="{question['option3']}"> {question[' option3']}<br>
                                                    <input type="radio" name="q{question['id']}" value="{question['option4']}"> {question['option4']}
                                                </td>
                                            </tr>
    """)

print(f"""
                                        </tbody>
                                    </table>
                                    <input type="submit" value="Submit Test">
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
""")