#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form = cgi.FieldStorage()
pat_id=form.getvalue('pat_id')
confirmed = form.getvalue('confirmed')

if confirmed == 'yes' and pat_id:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hds"
    )

    mycursor = mydb.cursor()

    # Execute the deletion
    query = f'''DELETE FROM patient WHERE id={pat_id}'''
    mycursor.execute(query)
    mydb.commit()

    # Success message after deletion
    print(f'''
    <script>
        alert("Record Deleted!!!");
        location.href="patientlist.py";
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
                    window.location.href = "patient_delete.py?pat_id={pat_id}&confirmed=yes";
                }} else {{
                    // If canceled, redirect to the patient list page
                    window.location.href = "patientlist.py";
                }}
            }}
        </script>
    </head>
    <body onload="confirmDelete()">
    </body>
    </html>
    ''')

