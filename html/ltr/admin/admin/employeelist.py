#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")

form = cgi.FieldStorage()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

query = """
SELECT * FROM employee
"""



mycursor.execute(query)
myresult = mycursor.fetchall()


tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>
                <a href="employee_edit.py ?emp_id={x['id']}"><button class="btn btn-success"><i class="fas fa-edit"></i></button></a>
                <a href="employee_delete.py ?emp_id={x['id']}"><button class="btn btn-danger"><i class="fas fa-trash"></i></button></a>
            </td>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['mobno']}</td>
            <td>{x['email']}</td>
            <td>{x['aadhar']}</td>
            <td>{x['dob']}</td>
            <td>{x['gender']}</td>
            <td>{x['institute_name']}</td>
            <td>{x['university']}</td>
            <td>{x['course']}</td>
            <td>{x['passing_year']}</td>
            <td>{x['percentage']}</td>
            <td>{x['designation']}</td>
            <td>{x['work_exp']}</td>
            <td>{x['joindate']}</td>
            <td>{x['country']}</td>
            <td>{x['state']}</td>
            <td>{x['city']}</td>
            <td>{x['area']}</td>
            <td>{x['bld_name']}</td>
            <td>{x['pincode']}</td>
            <td>{x['bnk_name']}</td>
            <td>{x['bnk_branch']}</td>
            <td>{x['acc_no']}</td>
           
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
                                    <li class="breadcrumb-item active" aria-current="page">Employee List</li>
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
                                <h2 class="card-title">Employee's Data</h2>    
                                <div class="table-responsive">
                                    <table id="multi_control" class="table table-striped table-bordered display" style="width:100%">                                 
                                <thead>
                                      <tr style="background-color:powderblue;">
                                           <th scope="col">Action</th>
                                           <th scope="col">Sr.No.</th>
                                           <th scope="col">First</th>
                                           <th scope="col">Middle</th>
                                           <th scope="col">Last</th>
                                           <th scope="col">Mobile No.</th>
                                           <th scope="col">Email</th>
                                           <th scope="col">Aadhar No.</th>
                                           <th scope="col">Birth Date</th>
                                           <th scope="col">Gender</th>                                         
                                           <th scope="col">Institute</th>                                        
                                           <th scope="col">University</th>
                                           <th scope="col">Course</th>
                                           <th scope="col">Passing Year</th>
                                           <th scope="col">Percentage</th>
                                           <th scope="col">Designation</th>
                                           <th scope="col">Experience</th>
                                           <th scope="col">Joining Date</th>
                                           <th scope="col">Country</th>
                                           <th scope="col">State</th>
                                           <th scope="col">City</th>
                                           <th scope="col">Area</th>
                                           <th scope="col">Building</th>
                                           <th scope="col">Pincode</th>
                                           <th scope="col">Bank</th>
                                           <th scope="col">Bank</th>                                    
                                           <th scope="col">Acc No.</th>
                                           
                                        </tr>
                                </thead>
                                <tbody>
                                    {tr_html}
                                </tbody>
                                <div style="text-align:center;">
                        </div>
                            </table>
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
