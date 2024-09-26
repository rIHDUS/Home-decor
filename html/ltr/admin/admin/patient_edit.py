#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import header
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")

form = cgi.FieldStorage()
pat_id = form.getvalue('pat_id')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

query = f"SELECT * FROM patient WHERE id = {pat_id}"
mycursor.execute(query)
myresult = mycursor.fetchone()

print(f'''

        <!-- ============================================================== -->
        <!-- End Topbar header -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- End Left Sidebar - style you can find in sidebar.scss  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Page wrapper  -->
        <!-- ============================================================== -->
        <div class="page-wrapper">
            <!-- ============================================================== -->
            <!-- Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <br><center><h2>Patient Form</h2></center><br>
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
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body wizard-content">
                                <form action="patient_update.py" class="tab-wizard wizard-circle">
                                    <!-- Step 1 -->
                                    <h6>Basic Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label>Sr No.</label><br>
                                            <input type="text" class="form-control" name="id" id="id" value="{myresult['id']}" readonly >
                                        </div>
                                        <div class="form-group">
                                            <label for="firstName">First Name</label>
                                            <input type="text" class="form-control" id="fname" value="{myresult['firstname']}" name="fname" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="middleName">Middle Name</label>
                                            <input type="text" class="form-control" id="mname" value="{myresult['middlename']}" name="mname" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="lastName">Last Name</label>
                                            <input type="text" class="form-control" id="lname" value="{myresult['lastname']}" name="lname" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="motherName">Mother Name</label>
                                            <input type="text" class="form-control" id="momname" value="{myresult['mothername']}" name="momnaame" required>
                                        </div>
                                    </section>
                                    <!-- Step 2 -->
                                    <h6>Other Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="control-label">Gender</label><br>
                                            <input type="text" class="form-control" id="gender" value="{myresult['gender']}" name="gender" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="birthdate">Date of birth</label>
                                            <input type="date" class="form-control" id="dob" value="{myresult['dob']}" name="dob" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="age">Age</label>
                                            <input type="number" class="form-control" id="age" value="{myresult['age']}" name="age" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="bloodgroup">Blood Group</label>
                                            <input type="text" class="form-control" id="bloodgroup" value="{myresult['bld_grp']}" name="bloodgroup" required>                   
                                        </div>
                                        <div class="form-group">
                                            <label for="refference">Doctor Refference</label>
                                            <input type="text" class="form-control" id="refference" value="{myresult['doct_refference']}" name="refference" required>
                                        </div>
                                    </section>
                                    <!-- Step 3 -->
                                    <h6>Parent Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="mob">Mobile No.</label>
                                            <input type="tel" class="form-control" id="mobno" value="{myresult['mobno']}" name="mobno" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="email">Email</label>
                                            <input type="email" class="form-control" id="email" value="{myresult['email']}" name="email" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="occuption">Occuption</label>
                                            <input type="text" class="form-control" id="occuption" value="{myresult['occuption']}" name="occuption" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="relation">Parent Relation</label>
                                            <input type="text" class="form-control" id="relation" value="{myresult['relation']}" name="relation" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="password">Password</label>
                                            <input type="text" class="form-control" id="password" value="{myresult['password']}" name="password" required>                    
                                        </div>
                                    </section>
                                    <!-- Step 4 -->
                                    <h6>Address Information</h6>
                                     <section>
                                        <div class="form-group">
                                            <label for="country">Country</label>
                                            <input type="text" class="form-control" value="India" value="{myresult['country']}" id="country" name="country" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="state">State</label>
                                            <input type="text" class="form-control" id="state" value="{myresult['state']}" name="state" required>                        
                                        </div>
                                        <div class="form-group">
                                            <label for="city">City</label>
                                            <input type="text" class="form-control" id="city" value="{myresult['city']}"  name="city" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="area">Area / Street</label>
                                            <input type="text" class="form-control" id="area" value="{myresult['area']}" name="area" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="build_name">Building / House Name</label>
                                            <input type="text" class="form-control" id="bld_name" value="{myresult['bld_name']}" name="bld_name" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="build_name">Pincode</label>
                                            <input type="text" class="form-control" id="pincode" value="{myresult['pincode']}" name="pincode" required>
                                        </div>
                                    </section>
                                </form>
                            </div>
                        </div>
                    </div>
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                    <!-- ============================================================== -->
                    <!-- Example -->
                    <!-- ============================================================== -->
                </div>
                <!-- ============================================================== -->
                <!-- End PAge Content -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Right sidebar -->
                <!-- ============================================================== -->
                <!-- .right-sidebar -->
                <!-- ============================================================== -->
                <!-- End Right sidebar -->
                <!-- ============================================================== -->
            </div>
            <!-- ============================================================== -->
            <!-- End Container fluid  -->
            <!-- ============================================================== -->
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
 
            <!-- row -->
            <!-- .row -->
            <!-- /.row -->
            <!-- Row -->
            <!-- .row -->
            <!-- /.row -->
            <!-- .row -->
            <!-- /.row -->
            <!-- .row -->
            <!-- .row -->
            <!-- /.row -->
            <!-- row -->
            <!-- Row -->
            <!-- Row -->
            <!-- ============================================================== -->
            <!-- End PAge Content -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Right sidebar -->
            <!-- ============================================================== -->
            <!-- .right-sidebar -->
            <!-- ============================================================== -->
            <!-- End Right sidebar -->
            <!-- ============================================================== -->
        </div>
        <!-- ============================================================== -->
        <!-- End Container fluid  -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- footer -->
        <!-- ============================================================== -->
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
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

</body>
</html>
      ''')