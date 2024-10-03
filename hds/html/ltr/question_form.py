#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-type: text/html\n")

try:
    form = cgi.FieldStorage()
    print("Form data received successfully")
except Exception as e:
    print("Error receiving form data: ", e)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hearing"
    )
    print("Database connection established successfully")
except mysql.connector.Error as err:
    print("Error connecting to database: ", err)

try:
    mycursor = mydb.cursor(dictionary=True)
    print("Database cursor created successfully")
except Exception as e:
    print("Error creating database cursor: ", e)

try:
    qquery = "SELECT * FROM question"
    mycursor.execute(qquery)
    myresult = mycursor.fetchall()
    print("Query executed successfully")
except Exception as e:
    print("Error executing query: ", e)

tr_html = ""
for x in myresult:
    tr_html += f"""
        <tr>
            <td>{x['question']}</td>
            
            <td>
                <input type="radio" name="q{x['id']}" value="{x['option1']}"> {x['option1']}<br>
                <input type="radio" name="q{x['id']}" value="{x['option2']}"> {x['option2']}<br>
                <input type="radio" name="q{x['id']}" value="{x['option3']}"> {x['option3']}<br>
                <input type="radio" name="q{x['id']}" value="{x['option4']}"> {x['option4']}
            </td>
        </tr>
    """

print(f"""
    <html>
    <head>
        <title>Audiology Test</title>
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
                display : block;
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
                                <h4 class="card-title">Audiology Test</h4>
                                <form action="submit_test.py" method="post">
                                    <table id="file_export" class="table table-striped table-bordered display">
                                        <thead>
                                            <tr>
                                               
                                                <th>Question</th>
                                                <th>Options</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {tr_html}
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
        <script>
            const form = document.querySelector('form');
            form.addEventListener('submit', (e) => {{
                e.preventDefault();
                const formData = new FormData(form);
                const radios = formData.getAll('radio');
                const score = 0;
                radios.forEach((radio) => {{
                    if (radio.checked) {{
                        score++;
                    }}
                }});
                if (score > 5) {{
                    window.location.href = 'consultation.py';
                }}
            }});
        </script>
    </body>
    </html>
""")