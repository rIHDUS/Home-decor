#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
from hashlib import sha256

cgitb.enable()
print("Content-Type: text/html\n")

form = cgi.FieldStorage()
email = form.getvalue('email')
new_password = form.getvalue('new_password')
confirm_new_password = form.getvalue('confirm_new_password')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Update with your MySQL password
    database="hds"
)
mycursor = mydb.cursor()

if not email:
    print('''
          <script>alert("Enter your email..!!");
          </script>
          ''')
    mydb.close()
    exit()

# Check if email exists
query = "SELECT * FROM register WHERE email=%s"
mycursor.execute(query, (email,))
user = mycursor.fetchone()

if user:
    if new_password and confirm_new_password:
        if new_password == confirm_new_password:
            hashed_password = sha256(new_password.encode()).hexdigest()
            update_query = "UPDATE register SET password=%s WHERE email=%s"
            mycursor.execute(update_query, (hashed_password, email))
            mydb.commit()
            print("Password updated")
        else:
            print("New password and confirmation do not match.")
    else:
        print("Please fill in both password fields.")
else:
    print("Email not found")

# Close database connection
mycursor.close()
mydb.close()
