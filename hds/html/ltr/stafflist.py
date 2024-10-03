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

query=f'''SELECT * FROM staff'''
#print(query)

mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)

tr_html=''
for x in myresult:
    tr_html+=f'''
        <tr>
            <td>
                <a href="staffedit.py?sid={x['sid']}"><button class="btn btn-success" style="background-color:#5DADE2;color:#FFF">EDIT</button></a> 
                <a href="staffdelete.py?sid={x['sid']}"><button class="btn btn-danger" style="background-color:#FF5733">DELETE</button></a>
            </td>
            <td>{x['sid']}</td>
            <td>{x['Firstname']}</td>
            <td>{x['Middlename']}</td>
            <td>{x['Lastname']}</td>
            <td>{x['Phone']}</td>
            <td>{x['Gender']}</td>
            <td>{x['Address']}</td>
            <td>{x['Maritalstatus']}</td>
            <td>{x['Bloodgroup']}</td>
            <td>{x['Dob']}</td>
            <td>{x['Adhar']}</td>
            <td>{x['Pan']}</td>
            <td>{x['Passport']}</td>
            <td>{x['Mobile']}</td>
            <td>{x['Email']}</td>
            <td>{x['Mobile2']}</td>
            <td>{x['Email2']}</td>
            <td>{x['Country']}</td>
            <td>{x['State']}</td>
            <td>{x['City']}</td>
            <td>{x['Pincode']}</td>
            <td>{x['Address2']}</td>
            <td>{x['Education']}</td>
            <td>{x['Specilisation']}</td>
            <td>{x['Institute']}</td>
            <td>{x['Percentage']}</td>
            <td>{x['Year']}</td>
            <td>{x['Bankname']}</td>
            <td>{x['Accountno']}</td>
            <td>{x['Accountholder']}</td>
            <td>{x['Accountype']}</td>
            <td>{x['Ifsccode']}</td>
            <td>{x['Bankbranch']}</td>
            <td>{x['Department']}</td>
            <td>{x['Jobtitle']}</td>
            <td>{x['Employmentstatus']}</td>
            <td>{x['Staffid']}</td>
            <td>{x['Experience']}</td>
            <td>{x['Joiningdate']}</td>
            <td>{x['Stime']}</td>
            <td>{x['Etime']}</td>
        </tr>
    '''

print(f'''
      <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <h3 class="page-title" style="text-align:center;">Staff List</h3>
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
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr style="background-color:#2ECC71;color:#FFF">
                                                <th>Action</th>
                                                <th scope="col">Sr. No.</th>
                                                <th scope="col">First Name</th>
                                                <th scope="col">Middle Name</th>
                                                <th scope="col">Last Name</th>
                                                <th scope="col">Phone No.</th>
                                                <th scope="col">Gender</th>
                                                <th scope="col">Address</th>
                                                <th scope="col">Maritalstatus</th>
                                                <th scope="col">Bloodgroup</th>
                                                <th scope="col">Dob</th>
                                                <th scope="col">Adhar</th>
                                                <th scope="col">Pan</th>
                                                <th scope="col">Passport</th>
                                                <th scope="col">Mobile </th>
                                                <th scope="col">Email</th>
                                                <th scope="col">Mobile2</th>
                                                <th scope="col">Email2</th>
                                                <th scope="col">Country</th>
                                                <th scope="col">State</th>
                                                <th scope="col">City</th>
                                                <th scope="col">Pincode</th>
                                                <th scope="col">Address2</th>
                                                <th scope="col">Education</th>
                                                <th scope="col">Specilisation</th>
                                                <th scope="col">Institute</th>
                                                <th scope="col">Percentage</th>
                                                <th scope="col">Year</th>
                                                <th scope="col">Bankname</th>
                                                <th scope="col">Accountno</th>
                                                <th scope="col">Accountholder</th>
                                                <th scope="col">Accountype</th>
                                                <th scope="col">Ifsccode</th>
                                                <th scope="col">Bankbranch</th>
                                                <th scope="col">Department</th>
                                                <th scope="col">Jobtitle</th>
                                                <th scope="col">Employmentstatus</th>
                                                <th scope="col">Staffid</th>
                                                <th scope="col">Experience</th>
                                                <th scope="col">Joiningdate</th>
                                                <th scope="col">Stime</th>
                                                <th scope="col">Etime</th>
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