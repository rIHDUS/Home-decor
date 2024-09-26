#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import header
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")

form = cgi.FieldStorage()
emp_id = form.getvalue('emp_id')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

query = f"SELECT * FROM employee WHERE id = {emp_id}"
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
            <br><center><h2>Employee Form</h2></center><br>
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
                                <form action="employee_update.py" class="tab-wizard wizard-circle">
                                    <!-- Step 1 -->
                                    <h6>Basic Information</h6>
                                    <section>
                                        <div class="form-group"> 
                                            <label for="srno">Sr No.</label><br>
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
                                            <label for="mobileno">Mobile Number</label>
                                            <input type="tel" class="form-control" id="mobno" name="mobno" value="{myresult['mobno']}" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="altmobno">Alternate Mobile Number</label>
                                            <input type="tel" class="form-control" id="altmobno" name="altmobno" value="{myresult['alt_mobno']}" required>
                                        </div>
                                    </section>
                                    
                                    <!-- Step 2 -->
                                    <h6>Personal Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="email">Email</label>
                                            <input type="email" class="form-control" id="email" name="email" value="{myresult['email']}" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="aadhar">Aadhar Number</label>
                                            <input type="text" class="form-control" id="aadhar" name="aadhar" value="{myresult['aadhar']}" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="birthdate">Date of birth</label>
                                            <input type="date" class="form-control" id="dob" name="dob" value="{myresult['dob']}" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="pan">PAN Number</label>
                                            <input type="text" class="form-control" id="pan" name="pan" value="{myresult['pan_no']}" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="control-label">Gender</label><br>
                                            <input type="text" class="form-control" id="gender" value="{myresult['gender']}" name="gender" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="mar_status">Maritual Status</label>
                                            <input type="text" class="form-control" id="mar_status" value="{myresult['maritual_status']}" name="mar_status" required>
                                        </div>
                                    </section>
                                    
                                    <!-- Step 3 -->
                                    <h6> Education Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="institutename">Institute Name</label>
                                            <input type="text" class="form-control" id="institute_name" value="{myresult['institute_name']}" name="institute_name" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="institutecity">Institute City</label>
                                            <input type="text" class="form-control" id="institute_city" value="{myresult['institute_city']}" name="institute_city" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="university">University</label>
                                            <input type="text" class="form-control" id="university" value="{myresult['university']}" name="university" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="course">Course</label>
                                            <input type="text" class="form-control" id="course" value="{myresult['course']}" name="course" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="passingyear">Passing Year</label>
                                            <input type="text" class="form-control" id="passing_year" value="{myresult['passing_year']}" name="passing_year" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="percentage">Percentage</label>
                                            <input type="text" class="form-control" id="percentage" value="{myresult['percentage']}" name="percentage" required>
                                        </div>
                                    </section>
                                    
                                    <!-- Step 4 -->
                                    <h6> Employment Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="designation">Designation</label>
                                            <input type="text" class="form-control" id="designation" value="{myresult['designation']}" name="designation" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="experience">Work Experience</label>
                                            <input type="text" class="form-control" id="experience" value="{myresult['work_exp']}" name="experience" required>                   
                                        </div>
                                        <div class="form-group">
                                            <label for="joindate">Joining Date</label>
                                            <input type="date" class="form-control" id="join_date" value="{myresult['joindate']}" name="join_date" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="password">Password</label>
                                            <input type="text" class="form-control" id="password" value="{myresult['password']}" name="password" required>
                                        </div>
                                    </section>
                                
                                    <!-- Step 5 -->
                                    <h6>Address Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="country">Country</label>
                                            <input type="text" class="form-control" value="India" value="{myresult['country']}" id="country" name="country">
                                        </div>
                                        <div class="form-group">
                                            <label for="state">State</label>
                                            <input type="text" class="form-control" id="states" value="{myresult['state']}" name="states" required>                    
                                        </div>
                                        <div class="form-group">
                                            <label for="city">City</label>
                                            <input type="text" class="form-control" id="city" value="{myresult['city']}" name="city" required>
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
                                    
                                    <!-- Step 6 -->
                                    <h6> Banking Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="bankname">Bank Name</label>
                                            <input type="text" class="form-control" id="bnk_name" value="{myresult['bnk_name']}" name="bnk_name" required>
                                        </div>

                                        <div class="form-group">
                                            <label for="branch">Branch</label>
                                            <input type="text" class="form-control" id="branch" value="{myresult['bnk_branch']}" name="branch" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="acctype">Account Type</label>
                                            <input type="text" class="form-control" id="acc_type" value="{myresult['acc_type']}" name="acc_type" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="accno">Account Number</label>
                                            <input type="text" class="form-control" id="acc_no" value="{myresult['acc_no']}" name="acc_no" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="ifsccode">IFSC code</label>
                                            <input type="text" class="form-control" id="ifsc_code" value="{myresult['ifs_code']}" name="ifsc_code" required>
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
    <div class="chat-windows"></div>
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
    <script src="../../dist/js/custom.js"></script>
    <script src="../../assets/libs/jquery-steps/build/jquery.steps.min.js"></script>
    <script src="../../assets/libs/jquery-validation/dist/jquery.validate.min.js"></script>
  <script>
  $(".tab-wizard").steps({{
      headerTag: "h6",
      bodyTag: "section",
      transitionEffect: "fade",
      titleTemplate: '<span class="step">#index#</span> #title#',
      labels: {{
          finish: "Submit"
      }},
      onFinished: function(event, currentIndex) {{
          $("form").submit();
      }}
  }});
</script>
</body>
</html>
 ''')