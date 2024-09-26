#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")

form = cgi.FieldStorage()
usr_id = form.getvalue('usr_id')

print(f'''
<html>
<head>
    <script>
        function confirmDelete() {{
            var result = confirm("Are you sure you want to delete this user?");
            if (result) {{
                // If confirmed, reload the page with the confirmed parameter
                window.location.href = "delete_user.py?usr_id={usr_id}&confirmed=yes";
            }} else {{
                // If canceled, redirect to the user list page
                window.location.href = "userlist.py";
            }}
        }}
    </script>
</head>
<body onload="confirmDelete()">
</body>
</html>
''')

# Check if the deletion is confirmed
confirmed = form.getvalue('confirmed')

if confirmed == 'yes' and usr_id:
    # Connect to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hds"
    )

    mycursor = mydb.cursor()

    # Delete query
    query = f'''DELETE FROM user_register WHERE id={usr_id}'''

    # Execute the query
    mycursor.execute(query)
    mydb.commit()

    # Success message
    print(f'''
    <script>alert("!!! User Deleted Successfully !!!");
        location.href="userlist.py";
    </script>
    ''')
