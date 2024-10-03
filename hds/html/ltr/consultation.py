#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)

mycursor = mydb.cursor(dictionary=True)

print(f"""
    <html>
    <head>
        <title>Consultation</title>
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
        </style>
    </head>
    <body>
        <div class="page-wrapper">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h4 class="card-title">Consultation</h4>
                                <p>Congratulations! You have scored more than 7 points in our hearing test.</p>
                                <p>We recommend that you consult with a hearing specialist to discuss your results and determine the best course of action.</p>
                                <p>Please fill out the form below to schedule a consultation:</p>
                                <form action="schedule_consultation.py" method="post">
                                    <label for="name">Name:</label>
                                    <input type="text" id="name" name="name"><br><br>
                                    <label for="email">Email:</label>
                                    <input type="email" id="email" name="email"><br><br>
                                    <label for="phone">Phone:</label>
                                    <input type="text" id="phone" name="phone"><br><br>
                                    <label for="date">Date:</label>
                                    <input type="date" id="date" name="date"><br><br>
                                    <label for="time">Time:</label>
                                    <input type="time" id="time" name="time"><br><br>
                                    <input type="submit" value="Schedule Consultation">
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