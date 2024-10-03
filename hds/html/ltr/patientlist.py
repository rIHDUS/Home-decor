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

query=f'''SELECT * FROM patient'''
#print(query)

mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)

tr_html=''
for x in myresult:
    tr_html+=f'''
        <tr>
            <td>
                <a href="patient_edit.py?pat_id={x['id']}"><button class="btn btn-success">EDIT</button></a>
                <a href="patient_delete.py?pat_id={x['id']}"><button class="btn btn-danger">DELETE</button></a>
            </td>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['mothername']}</td>
            <td>{x['age']}</td>
            <td>{x['dob']}</td>
            <td>{x['bloodgroup']}</td>
            <td>{x['doct_refference']}</td>
            <td>{x['gender']}</td>
            <td>{x['mobno']}</td>
            <td>{x['email']}</td>
            <td>{x['addrs']}</td>
            <td>{x['altaddrs']}</td>
        </tr>
    '''

print(f'''
      <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <h3 class="page-title" style="text-align:center;">Patient List</h3>
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
                                <h4 class="card-title" style="text-align:center">Patient List</h4><br>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr style="background-color:powderblue;">
                                                <th>Action</th>
                                                <th scope="col">Sr. No.</th>
                                                <th scope="col">First Name</th>
                                                <th scope="col">Middle Name</th>
                                                <th scope="col">Last Name</th>
                                                <th scope="col">Mother Name</th>
                                                <th scope="col">Age</th>
                                                <th scope="col">Birth Date</th>
                                                <th scope="col">Blood Group</th>
                                                <th scope="col">Doct. Refference</th>
                                                <th scope="col">Gender</th>
                                                <th scope="col">Mobile No.</th>
                                                <th scope="col">Email</th>
                                                <th scope="col">Address</th>
                                                <th scope="col">Alternate Address</th>
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