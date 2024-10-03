#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")
form=cgi.FieldStorage()

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor(dictionary=True)

query=f'''SELECT * FROM employee'''
#print(query)

mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)

tr_html=''
for x in myresult:
    tr_html+=f'''
        <tr>
            <td>
                <a href="employee_edit.py?emp_id={x['id']}"><button class="btn btn-success">EDIT</button></a>
                <a href="employee_delete.py?emp_id={x['id']}"><button class="btn btn-danger">DELETE</button></a>
            </td>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['mobno']}</td>
            <td>{x['altmobno']}</td>
            <td>{x['bnk_name']}</td>
            <td>{x['bnk_branch']}</td>
            <td>{x['acc_no']}</td>
            <td>{x['ifsc_no']}</td>
            <td>{x['aadhar']}</td>
            <td>{x['email']}</td>
            <td>{x['addrs']}</td>
            <td>{x['altaddress']}</td>
            <td>{x['dob']}</td>
            <td>{x['education']}</td>
            <td>{x['password']}</td>
        </tr>
    '''

print(f'''
      <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <h3 class="page-title" style="text-align:center;">Employee List</h3>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Start Page Content -->
                <!-- ============================================================== -->
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body"><br>
                                <h4 class="card-title" style="text-align:center">Employee List</h4><br>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr style="background-color:powderblue;">
                                                <th>Action</th>
                                                <th scope="col">Sr. No.</th>
                                                <th scope="col">First Name</th>
                                                <th scope="col">Middle Name</th>
                                                <th scope="col">Last Name</th>
                                                <th scope="col">Mobile No.</th>
                                                <th scope="col">Alternate Mob.No.</th>
                                                <th scope="col">Bank Name</th>
                                                <th scope="col">Bank Branch</th>
                                                <th scope="col">Account No.</th>
                                                <th scope="col">IFSC No.</th>
                                                <th scope="col">Aadhar No.</th>
                                                <th scope="col">Email</th>
                                                <th scope="col">Address</th>
                                                <th scope="col">Alternate Address</th>
                                                <th scope="col">Birth Date</th>
                                                <th scope="col">Education</th>
                                                <th scope="col">Password</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {tr_html}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- footer -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- End footer -->
            <!-- ============================================================== -->
        </div>
        <!-- ============================================================== -->
        <!-- End Page wrapper  -->
        <!-- ============================================================== -->
    </div>
    <!-- ============================================================== -->
    <!-- End Wrapper -->
    <!-- ============================================================== -->
    <!-- ============================================================== -->
    <!-- customizer Panel -->
    <!-- ============================================================== -->
    <div class="chat-windows"></div>
    <!-- ============================================================== -->
    <!-- All Jquery -->
    <!-- ============================================================== -->
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
''')