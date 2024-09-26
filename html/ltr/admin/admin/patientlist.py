#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")
form = cgi.FieldStorage()

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)



# Get the current page number and search query from the form data


# SQL query for fetching patients with search functionality
query = "SELECT * FROM patient"

# Get total number of records
mycursor.execute(query)

myresult = mycursor.fetchall()

# Generate the table rows for the fetched records
tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>
                <a href="patient_edit.py ?pat_id={x['id']}"><button class="btn btn-success"><i class="fas fa-edit"></i></button></a>
                <a href="patient_delete.py ?pat_id={x['id']}"><button class="btn btn-danger"><i class="fas fa-trash"></i></button></a>
            </td>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['mothername']}</td>
            <td>{x['gender']}</td>
            <td>{x['dob']}</td>
            <td>{x['age']}</td>
            <td>{x['bld_grp']}</td>
            <td>{x['doct_refference']}</td>
            <td>{x['mobno']}</td>
            <td>{x['email']}</td>
            <td>{x['occuption']}</td>
            <td>{x['relation']}</td>
            <td>{x['password']}</td>
            <td>{x['country']}</td>
            <td>{x['state']}</td>
            <td>{x['city']}</td>
            <td>{x['area']}</td>
            <td>{x['bld_name']}</td>
            <td>{x['pincode']}</td>
        </tr>
    '''

# Pagination controls


# Search form and table display
print(f'''
<div class="page-wrapper">
<div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Admin's Panel</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb">
                                    <li class="breadcrumb-item"><a href="dashboard.py">Home</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Pateint List</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                    <div class="col-7 align-self-center">
                        
                    </div>
                </div>
            </div>
<div class="container-fluid">     
 <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h2 class="card-title">Patient's Data</h2>
                                
                                <div class="table-responsive">
                                    <table id="multi_control" class="table table-striped table-bordered display" style="width:100%">                                
                                <thead>
                                    <tr style="background-color:powderblue;"><br>
                                        <th>Action</th>
                                        <th scope="col">Sr.No.</th>
                                        <th scope="col">First Name</th>
                                        <th scope="col">Middle Name</th>
                                        <th scope="col">Last Name</th>
                                        <th scope="col">Mother Name</th>
                                        <th scope="col">Gender</th>
                                        <th scope="col">Date of Birth</th>
                                        <th scope="col">Age</th>                                                
                                        <th scope="col">Blood Group</th>
                                        <th scope="col">Dr.Refference</th>
                                        <th scope="col">Mob no.</th>
                                        <th scope="col">Email</th>
                                        <th scope="col">Occuption</th>
                                        <th scope="col">Parent Relation</th>
                                        <th scope="col">Password</th>                                                
                                        <th scope="col">Country</th>
                                        <th scope="col">State</th>
                                        <th scope="col">City</th>
                                        <th scope="col">Area</th>
                                        <th scope="col">Build. Name</th>
                                        <th scope="col">Pincode</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {tr_html}
                                </tbody>
                            </table>
                        </div>
                        <div style="text-align:center;">
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    </div>
    </div>
    
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
</div>
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
    <!--This page plugins -->
    <script src="../../assets/extra-libs/DataTables/datatables.min.js"></script>
    <!-- start - This is for export functionality only -->
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/dataTables.buttons.min.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.flash.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/pdfmake.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/vfs_fonts.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.html5.min.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.print.min.js"></script>
    <script src="../../dist/js/pages/datatable/datatable-advanced.init.js"></script>
</body>
</html> 
''')
