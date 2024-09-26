#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import header
cgitb.enable()

# Print the header and included CSS/JS
print(header.homehtml)
print("Content-type: text/html\n")
print('''<!DOCTYPE html>
<html>
<head>
    <title>Patient Appointment Records</title>
    
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Patient Appointment Records</h1>
        <div class="table-responsive">
            <table id="example" class="display table table-bordered" style="width:100%">
                <thead>
                    <tr style="background-color:powderblue;">
                        <th>Action</th>
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
query = "SELECT * FROM appointment"
mycursor.execute(query)
myresult = mycursor.fetchall()

# Generate table rows
tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>
                <a href="appointment_edit.py?pat_id={x['id']}"><button class="btn btn-success">EDIT</button></a>
                <a href="appointment_delete.py?pat_id={x['id']}"><button class="btn btn-danger">DELETE</button></a>
            </td>
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
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function() {{
            $('#example').DataTable();
        }});
    </script>
    <script src="../../assets/libs/jquery/dist/jquery.min.js"></script>
    <!-- Bootstrap tether Core JavaScript -->
    <script src="../../assets/libs/popper.js/dist/umd/popper.min.js"></script>
    <script src="../../assets/libs/bootstrap/dist/js/bootstrap.min.js"></script>
    <!-- apps -->
    <script src="../../dist/js/app.min.js"></script>
    <script src="../../dist/js/app.init.js"></script>
    <script src="../../dist/js/app-style-switcher.js"></script>
    <!-- slimscrollbar scrollbar JavaScript -->
    <script src="../../assets/libs/perfect-scrollbar/dist/perfect-scrollbar.jquery.min.js"></script>
    <script src="../../assets/extra-libs/sparkline/sparkline.js"></script>
    <!--Wave Effects -->
    <script src="../../dist/js/waves.js"></script>
    <!--Menu sidebar -->
    <script src="../../dist/js/sidebarmenu.js"></script>
    <!--Custom JavaScript -->
    <script src="../../dist/js/custom.min.js"></script>  
</body>
</html>
''')

