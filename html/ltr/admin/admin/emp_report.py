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
    <title>Customer Report</title>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.3.2/css/buttons.dataTables.min.css">
</head>
<body>
    <h1>
        <h1>
            <hr>
            <center>Employee Report</center>
            <hr>
        </h1>
    </h1>
    <table id="example" class="display" style="width:100%">
        <thead>
            <tr>
                <th scope="col">Sr. No.</th>
                <th scope="col">First Name</th>
                <th scope="col">Middle Name</th>
                <th scope="col">Last Name</th>
                <th scope="col">Mobile No.</th>
                <th scope="col">Email</th>                                                
                <th scope="col">Aadhar No.</th>
                <th scope="col">Birth Date</th>
                <th scope="col">Education</th>
                <th scope="col">Gender</th>
                <th scope="col">Experience</th>
                <th scope="col">Joining Date</th>
                <th scope="col">Password</th>
                <th scope="col">Country</th>
                <th scope="col">State</th>
                <th scope="col">City</th>
                <th scope="col">Area</th>
                <th scope="col">Build. Name</th>
                <th scope="col">Pincode</th>
                <th scope="col">Bank Name</th>
                <th scope="col">Bank Branch</th>
                <th scope="col">Account No.</th>
                <th scope="col">IFSC Code</th>
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
query = f'''SELECT * FROM employee'''
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
            <td>{x['mobno']}</td>
            <td>{x['email']}</td>
            <td>{x['aadhar']}</td>
            <td>{x['dob']}</td>
            <td>{x['education']}</td>
            <td>{x['gender']}</td>
            <td>{x['work_exp']}</td>
            <td>{x['joindate']}</td>
            <td>{x['password']}</td>
            <td>{x['country']}</td>
            <td>{x['state']}</td>
            <td>{x['city']}</td>
            <td>{x['area']}</td>
            <td>{x['bld_name']}</td>
            <td>{x['pincode']}</td>
            <td>{x['bnk_name']}</td>
            <td>{x['bnk_branch']}</td>
            <td>{x['acc_no']}</td>
            <td>{x['ifsc_code']}</td>
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
