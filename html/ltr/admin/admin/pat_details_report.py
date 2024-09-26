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
    <title>Patient Details Report</title>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.3.2/css/buttons.dataTables.min.css">
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
</head>
<body>
    <h1>
        <center>Patient Details Report</center>
        <hr>
    </h1>

    <table id="example" class="display" style="width:100%">
        <thead>
            <tr>
                <th scope="col">Sr. No.</th>
                <th scope="col">First Name</th>
                <th scope="col">Middle Name</th>
                <th scope="col">Last Name</th>
                <th scope="col">Birth Date</th>
                <th scope="col">Age</th>
                <th scope="col">Blood Group</th>
                <th scope="col">Gender</th>
                <th scope="col">Dr. Refference</th>                
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

# Handle form data
form = cgi.FieldStorage()

# Query to fetch employee data with date filter
query = "SELECT * FROM patient"

mycursor = mydb.cursor(dictionary=True)
mycursor.execute(query)
myresult = mycursor.fetchall()

# Generate table rows
tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['dob']}</td>
            <td>{x['age']}</td>
            <td>{x['bld_grp']}</td>
            <td>{x['gender']}</td>
            <td>{x['doct_refference']}</td>
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
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
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
