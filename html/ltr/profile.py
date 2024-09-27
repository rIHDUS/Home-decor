#!C:\Python312\python.exe

import cgi
import cgitb
import mysql.connector

# Enable CGI traceback for debugging
cgitb.enable()

# CGI form
form = cgi.FieldStorage()
user_id = form.getvalue("user_id") 


print('''
      <script>
    // Retrieve the user ID from localStorage
    var userId = localStorage.getItem("User_id");  // Make sure User_ID is stored in localStorage

    if (userId === null || userId === "") {
        alert("Login first");
        window.location.href = "home.py";
    } else {
        // Redirect to profile.py with the user_id as a query parameter
        window.location.href = "profile.py ?user_id=" + encodeURIComponent(userId);
    }
       </script>

      ''')

 # Get user_id from the form

# Database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Add your MySQL root password if set
        database="hds"
    )
    cursor = conn.cursor()

    # Fetch user data based on user_id
    query = "SELECT name, email FROM user_register WHERE id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    if result:
        name, email = result
    else:
        name, email = ("N/A", "N/A")

except mysql.connector.Error as err:
    print("Content-type: text/html\n")
    print(f"<html><body><h2>Error: {str(err)}</h2></body></html>")
    exit()

finally:
    cursor.close()
    conn.close()

# Output the profile page as HTML
print("Content-type: text/html\n")
print(f"""
<html>
<head>
    <title>User Profile</title>
    <!--<link rel="stylesheet" href="path/to/your/css/styles.css">--> <!-- Add your styles -->
</head>
<body>
    <h1>Welcome, {name}</h1>
    <p><strong>Email:</strong> {email}</p>
</body>
</html>
""")
