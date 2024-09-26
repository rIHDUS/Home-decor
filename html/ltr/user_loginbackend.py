#!C:\Python312\Python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
email = form.getvalue('user_name')
password = form.getvalue('user_psw')

# Check if the form fields are being captured correctly
#print(f"Email from form: {email}")
#print(f"Password from form: {password}")

# Database connection
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hds"
    )
    mycursor = mydb.cursor()

    # Trim leading/trailing spaces and use a parameterized query
    query = "SELECT * FROM user_register WHERE TRIM(email)=%s AND TRIM(password)=%s"
    mycursor.execute(query, (email, password))

    # Fetch one result
    myresult = mycursor.fetchall()

    # Print the executed query and the result
    #print(f"Query executed: {query}")
    #print(f"Email: {email}, Password: {password}")
    print(f"Result: {myresult}")

    # Check if a matching row was found
    if myresult:
        print(f'''
            <script>
            localStorage.clear();
            
            localStorage.setItem('User_Name','{myresult[0][1]}');
            localStorage.setItem('User_id','{myresult[0][0]}');
            alert("Logged in!");
            location.href="questions.py";
            </script>
            ''')
    else:
        print(f'''
            <script>
            alert("Wrong password or username");
            location.href="user_loginbackend.py";
            </script>
            ''')

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()
