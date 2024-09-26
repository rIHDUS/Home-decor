#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

cgitb.enable()
print("Content-type: text/html\n")

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
middle_name = form.getvalue('middle_name')
last_name = form.getvalue('last_name')
mothername = form.getvalue('mother_name')
apt_date = form.getvalue('appointment_date')
apt_time = form.getvalue('appointment_time')
age = form.getvalue('age')
mobno = form.getvalue('phone')
email = form.getvalue('email')
score = form.getvalue('test_score')
message = form.getvalue('message')


# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor()

# Insert data into the database
query = f"""INSERT INTO appointment (first_name, middle_name, last_name, mothername, apt_date, apt_time, age, mobno, email,score, message) 
VALUES ('{first_name}', '{middle_name}', '{last_name}', '{mothername}', '{apt_date}', '{apt_time}', '{age}', '{mobno}','{email}', '{score}', '{message}')"""

mycursor.execute(query)
mydb.commit()

# Close the cursor and the connection
mycursor.close()
mydb.close()

# PDF generation function with improved styling

# PDF generation function with receipt-like layout
def generate_pdf(appointment_details, pdf_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    # Set up some basic settings
    c.setTitle("Appointment Receipt")
    
    # Title: Appointment Receipt
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2.0, height - inch, "Audiology Diagnostic Assessment Portal")
    
    # Draw a box for receipt number
    c.setLineWidth(1.5)
    c.rect(inch, height - (inch + 40), width - 2*inch, 30)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(inch + 10, height - inch - 30, "Receipt #: 00007")
    
    # Draw a line under the title
    c.setLineWidth(1)
    c.line(inch, height - (inch + 80), width - inch, height - (inch + 80))
    
    # Section 1: Patient Info
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, height - (inch + 100), "Patient Information")
    c.setLineWidth(0.5)
    c.line(inch, height - (inch + 115), width - inch, height - (inch + 115))
    
    c.setFont("Helvetica", 12)
    y_position = height - (inch + 140)
    c.drawString(inch, y_position, f"Name: {appointment_details['Name']}")
    
    c.drawString(inch, y_position - 20, f"Mother's Name: {appointment_details['Mother\'s Name']}")
    c.drawString(inch, y_position - 40, f"Age: {appointment_details['Age']}")
    c.drawString(inch, y_position - 60, f"Mobile Number:+ {appointment_details['Mobile Number']}")
    
    # Section 2: Appointment Info
    y_position -= 100
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, y_position, "Appointment Details")
    c.setLineWidth(0.5)
    c.line(inch, y_position - 15, width - inch, y_position - 15)
    
    c.setFont("Helvetica", 12)
    c.drawString(inch, y_position - 35, f"Appointment Date: {appointment_details['Appointment Date']}")
    c.drawString(inch, y_position - 55, f"Appointment Time: {appointment_details['Appointment Time']}")
    
    # Section 3: Other Info
    y_position -= 100
    c.setFont("Helvetica-Bold", 14)
    c.drawString(inch, y_position, "Additional Information")
    c.setLineWidth(0.5)
    c.line(inch, y_position - 15, width - inch, y_position - 15)
    
    c.setFont("Helvetica", 12)
    c.drawString(inch, y_position - 35, f"Score: {appointment_details['Score']}")
    c.drawString(inch, y_position - 55, f"Message: {appointment_details['Message']}")
    
    # Footer or closing message
    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width / 2.0, 50, "Thank for applying..!! Wait for the confirmation mail/messagae")
    
    # Save the PDF
    c.save()
# Prepare appointment details for PDF
appointment_details = {
    "Name": first_name+" "+middle_name+" "+last_name,
    "Mother's Name": mothername,
    "Appointment Date": apt_date,
    "Appointment Time": apt_time,
    "Age": age,
    "Mobile Number": mobno,
    "Score": score,
    "Message": message
}

# Adjust the path to a valid directory on your system
pdf_filename = f"C:/Users/HP/Desktop/appointment_{first_name}.pdf"
generate_pdf(appointment_details, pdf_filename)

# Display confirmation dialog
print(f'''
<script>
    var download = confirm("Application submitted successfully! Do you want to download a PDF of the appointment details?");
    if (download) {{
        window.location.href = "confirmation.py";  // Redirect to the PDF file
    }} else {{
        alert("Thank you! You can view your appointment details later.");
        window.location.href = "confirmation.py";  // Redirect to a confirmation page
    }}
</script>
''')
