#!C:/Python312/python.exe

import cgi
import cgitb
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

cgitb.enable()

form = cgi.FieldStorage()
recipient = form.getvalue("email")
subject = "Appointment Confirmation"
message_body = form.getvalue("amess")

# Email credentials
sender_email = "sudhirsarpata@gmail.com"
sender_password = "caqkhimjlxosvdnt"

# SMTP server details (example: Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

def send_email(recipient, subject, message_body):
    try:
        # Create message container
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject

        # Attach message body
        msg.attach(MIMEText(message_body, "plain"))

        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()

        # Trigger a success alert and redirect
        print("<script>alert('Email sent successfully!'); window.location.href = 'appointmentlist.py';</script>")
    except Exception as e:
        # Trigger an error alert and prevent redirection
        print(f"<script>alert('Failed to send email. Error: {str(e)}');</script>")

# CGI response header
print("Content-type: text/html\n")

# Send email and display result
send_email(recipient, subject, message_body)
