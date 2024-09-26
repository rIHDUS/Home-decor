#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form = cgi.FieldStorage()
apt_id=form.getvalue('app_id')
confirmed = form.getvalue('confirmed')

if confirmed == 'yes' and apt_id:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hds"
    )

    mycursor = mydb.cursor()

    # Execute the deletion
    query = f'''DELETE FROM appointment WHERE app_id={apt_id}'''
    mycursor.execute(query)
    mydb.commit()

    # Success message after deletion
    print(f'''
    <script>
        alert("Record Deleted!!!");
        location.href="appointmentlist.py";
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
                    window.location.href = "appointment_delete.py?app_id={apt_id}&confirmed=yes";
                }} else {{
                    // If canceled, redirect to the patient list page
                    window.location.href = "appointmentlist.py";
                }}
            }}
        </script>
    </head>
    <body onload="confirmDelete()">
    </body>
    </html>
    ''')


