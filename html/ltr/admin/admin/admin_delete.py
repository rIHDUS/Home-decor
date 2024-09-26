#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")

# Get the employee ID from the form or query string
form = cgi.FieldStorage()
adm_id=form.getvalue('adm_id')
confirmed = form.getvalue('confirmed')

# If deletion is confirmed, perform the delete action
if confirmed == 'yes' and adm_id:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hds"
    )

    mycursor = mydb.cursor()

    # Execute the deletion
    query = f'''DELETE FROM register WHERE id={adm_id}'''
    mycursor.execute(query)
    mydb.commit()

    # Success message after deletion
    print(f'''
    <script>
        alert("Record Deleted!!!");
        location.href="adminlist.py";
    </script>
    ''')
else:
    # Show the confirmation box
    print(f'''
    <html>
    <head>
        <script>
            function confirmDelete() {{
                var result = confirm("Are you sure you want to delete this record?");
                if (result) {{
                    // If confirmed, reload the page with the confirmed parameter
                    window.location.href = "admin_delete.py?adm_id={adm_id}&confirmed=yes";
                }} else {{
                    // If canceled, redirect to the employee list page
                    window.location.href = "adminlist.py";
                }}
            }}
        </script>
    </head>
    <body onload="confirmDelete()">
    </body>
    </html>
    ''')
