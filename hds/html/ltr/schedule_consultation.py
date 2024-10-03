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

name = form.getvalue("name")
email = form.getvalue("email")
phone = form.getvalue("phone")
date = form.getvalue("date")
time = form.getvalue("time")

query = "INSERT INTO consultations (name, email, phone, date, time) VALUES (%s, %s, %s, %s, %s)"
mycursor.execute(query, (name, email, phone, date, time))
mydb.commit()

print(f"""
    <html>
    <head>
        <title>Consultation Scheduled</title>
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
                                <h4 class="card-title">Consultation Scheduled</h4>
                                <p>Thank you for scheduling a consultation with us!</p>
                                <p>We will contact you at {email} to confirm the details of your consultation.</p>
                                <p>Please note that this is an automated response and we will be in touch with you shortly.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
""")

# Send an email to the user to confirm the consultation
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'your-email@gmail.com'
msg['To'] = email
msg['Subject'] = 'Consultation Scheduled'

body = f"""
Dear {name},

Thank you for scheduling a consultation with us! We will contact you at {email} to confirm the details of your consultation.

Please note that this is an automated response and we will be in touch with you shortly.

Best regards,
Your Name
"""

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(msg['From'], 'your-password')
text = msg.as_string()
server.sendmail(msg['From'], msg['To'], text)
server.quit()