#!C:\Python312\python.exe
import header
print(header.homehtml)
print('''
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
            <h3 class="page-title" style="text-align:center;">Patient Form</h3>
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
                <!-- row -->
                <div class="card">
                <div class="card-body">
                <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b> Patient Information</b></h4><br>    
                <form class="m-t-30" action="patientbackend.py" method="POST" enctype="multipart/form-data">
                    <div class="col-md-12">
					    <div class="row">
                            <div class="col-md-4">
					            <label>First Name </label><br>
					            <input type="text" class="form-control" name="firstname" id="firstname" aria-describedby="emailHelp" placeholder="Enter Patient First Name" patteren="[A-Za-z]+" required>
                             </div>
                            <div class="col-md-4">
					            <label>Middle Name </label><br>
					            <input type="text" class="form-control" name="middlename" id="middlename" aria-describedby="emailHelp" placeholder="Enter Patient Middle Name" patteren="[A-Za-z]+" required>
                            </div>
                         
				             <div class="col-md-4">
					            <label>Last Name </label><br>
					            <input type="text" class="form-control" name="lastname" id="lastname" aria-describedby="emailHelp" placeholder="Enter Patient Last Name" patteren="[A-Za-z]+" required>
                            </div>
				        </div>   
				    </div><br>
                        <div class="col-md-12">
					        <div class="row">
                                <div class="col-md-6">
					            <label>Mother Name</label><br>
					            <input type="text" class="form-control" name="mothername" id="mothername" aria-describedby="emailHelp" placeholder="Enter Patient Mother Name" patteren="[0-9]" required>
                            </div>
                            <div class="col-md-6">
					            <label>Patient Age</label><br>
                                <input type="number" class="form-control" name="age" id="age" placeholder="Enter Age Between 0 To 6 Years" required>
                             </div>
                        </div><br>
                        <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Date of birth</label>
                                        <input type="date" class="form-control" name="dob" id="dob" placeholder="Select date of birth" required>
                                    </div>
                                    <div class="col-md-6">
					                    <label>Patient Blood Group</label><br>
                                        <select class="form-control" name="bloodgroup" id="bloodgroup" aria-describedby="emailHelp">
                                            <option value="placeholder" selected>Select Patient Blood Group</option>
                                            <option>A Positive</option>
                                            <option>A Negative</option>
                                            <option>A Unknown</option>
                                            <option>B Positive</option>
                                            <option>B Negative</option>
                                            <option>B Unknown</option>
                                            <option>AB Positive</option>
                                            <option>AB Negative</option>
                                            <option>AB Unknown</option>
                                            <option>O Positive</option>
                                            <option>O Negative</option>
                                            <option>O Unknown</option>
                                            <option>Unknown</option>
                                        </select>                                     
                                    </div>
                                </div>
                            </div><br>
                        </div>
                    </div>
                        <br>
                        <div class="card">
                         <div class="card-body">
                            <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b>Patient Other Information</b></h4><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Doctor Refference</label>
                                        <input class="form-control" name="refference" id="refference" type="text" placeholder="Enter Doctor Refference" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Gender</label><br>
                                        <select class="form-control" name="gender" id="gender" >
                                            <option value="">Please select one … </option>
                                            <option value="female">Female</option>
                                            <option value="male">Male</option>
                                        </select>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
					                    <label>Mobile No</label><br>
					                    <input type="text" class="form-control" name="mobno" id="mobno" aria-describedby="emailHelp" placeholder="Enter your mobile number" patteren="[0-9]" required>
                                     </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Email </label>
                                        <input type="email" class="form-control" name="email" id="email" placeholder="Enter email of patient" required>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Address</label>
                                        <input type="text" class="form-control" name="addrs" id="addrs" placeholder="Enter address of patient" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Alternative address</label>
                                        <input type="text" class="form-control" name="altaddrs" id="altaddrs" placeholder="Enter alternative address of patient" required>
                                    </div>
                                </div>
                            </div><br>
                            <center><button type="submit" class="btn btn-success">Submit</button></center>
                </form>
                </div>
            </div>
      </div>
      </div>

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
            <footer class="footer text-center">
       All Rights Reserved by Xtreme admin. Designed and Developed by <a href="https://wolfox.in">Wolfox</a>.
</footer>
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
    <script>
        function validatePasswords() {{
            var password = document.getElementById("password").value;
            var cpassword = document.getElementById("cpassword").value;
            if (password !== cpassword) {{
                alert("Passwords do not match.");
                return false;
            }}
            return true;
        }}
        $('[data-toggle="tooltip"]').tooltip();
        $(".preloader").fadeOut();
        
    </script>
</body>


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/form-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:49:09 GMT -->
</html>
''')