#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()

# HTML Header and CSS/JS includes
print("Content-type: text/html\n")
print('''<!DOCTYPE html>
<html>
<head>
    <title>Patient Appointment Records</title>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.3.2/css/buttons.dataTables.min.css">
</head>
<body>
    <h1>
        <h1>
            <hr>
            <center>Patient Appointment Records</center>
            <hr>
        </h1>
    </h1>
    <table id="example" class="display" style="width:100%">
        <thead>
            <tr style="background-color:powderblue;">
                <th scope="col">Sr. No.</th>
                <th scope="col">Patient Name</th>
                <th scope="col">Mother Name</th>
                <th scope="col">Appointment Date</th>
                <th scope="col">Appointment Time</th>
                <th scope="col">Age</th>
                <th scope="col">Mobile No.</th>
                <th scope="col">Message</th>
            </tr>
        </thead>
        <tbody>
''')

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

# Query to fetch customer data
mycursor = mydb.cursor(dictionary=True)
query=f'''SELECT * FROM appointment'''

mycursor.execute(query)
myresult = mycursor.fetchall()

# Generate table rows
tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>{x['id']}</td>
            <td>{x['pat_name']}</td>
            <td>{x['mothername']}</td>
            <td>{x['apt_date']}</td>
            <td>{x['apt_time']}</td>
            <td>{x['age']}</td>
            <td>{x['mobno']}</td>
            <td>{x['message']}</td>
        </tr>
    '''

# Print table rows and footer
print(f'''
        {tr_html}
        </tbody>
    </table>
    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/2.3.2/js/dataTables.buttons.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
    <script src="https://cdn.datatables.net/buttons/2.3.2/js/buttons.html5.min.js"></script>
    <script>
        $(document).ready(function() {{
            $('#example').DataTable({{
                dom: 'Bfrtip',
                buttons: [
                    'copyHtml5',
                    'excelHtml5',
                    'csvHtml5',
                    'pdfHtml5'
                ]
            }});
        }});
    </script>
</body>
</html>
''')
