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
            <h3 class="page-title" style="text-align:center;">Employee Form</h3>
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
                <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b>Employee Personal Information</b></h4><br>    
                <form class="m-t-30" action="employeebackend.py" method="POST" enctype="multipart/form-data" onsubmit="return validatePasswords()">
                    <div class="col-md-12">
					    <div class="row">
                            <div class="col-md-4">
					            <label>First Name </label><br>
					            <input type="text" class="form-control" name="firstname" id="firstname" aria-describedby="emailHelp" placeholder="Enter your First Name" pattern="[A-Za-z]+" required>
                             </div>
                            <div class="col-md-4">
					            <label>Middle Name </label><br>
					            <input type="text" class="form-control" name="middlename" id="middlename" aria-describedby="emailHelp" placeholder="Enter your Middle Name" pattern="[A-Za-z]+" required>
                            </div>
				             <div class="col-md-4">
					            <label>Last Name </label><br>
					            <input type="text" class="form-control" name="lastname" id="lastname" aria-describedby="emailHelp" placeholder="Enter your last Name" pattern="[A-Za-z]+" required>
                            </div>
				        </div>   
				    </div><br>
                    <div class="col-md-12">
					        <div class="row">
                                <div class="col-md-6">
					            <label>Mobile No</label><br>
					            <input type="text" class="form-control" name="mobno" id="mobno" aria-describedby="emailHelp" placeholder="Enter your mobile number" pattern="[0-9]+" required>
                            </div>
                            <div class="col-md-6">
					            <label>Alternative Mobile No</label><br>
					            <input type="text" class="form-control" name="altmobno" id="altmobno" aria-describedby="emailHelp" placeholder="Enter your alternative mobile" pattern="[0-9]+" required>
                             </div>
                            </div>
                    </div>
                    </div><br> 
                    <div class="card">
                         <div class="card-body">
                            <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b>Employee Banking Information</b></h4><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Bank Name</label>
                                        <input type="text" class="form-control" name="bnk_name" id="bnk_name" placeholder="Enter bank name" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Branch </label>
                                        <input type="text" class="form-control" name="bnk_branch" id="bnk_branch" placeholder="Enter bank branch name" required>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Account Number</label>
                                        <input type="text" class="form-control" name="acc_no" id="acc_no" placeholder="Enter account number" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">IFSC Number</label>
                                        <input type="text" class="form-control" name="ifsc_no" id="ifsc_no" style="text-transform: uppercase" placeholder="Enter ifsc number" required>
                                    </div>
                                </div>
                            </div><br>
                        </div>
                    </div><br>
                    <div class="card">
                         <div class="card-body">
                            <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b>Employee Other Information</b></h4><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Aadhar Number</label>
                                        <input type="text" class="form-control" name="aadhar" id="aadhar" placeholder="Enter aadhar number of employee" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Email </label>
                                        <input type="email" class="form-control" name="email" id="email" placeholder="Enter email of employee" required>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Address</label>
                                        <input type="text" class="form-control" name="addrs" id="addrs" placeholder="Enter address of employee" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Alternative address</label>
                                        <input type="text" class="form-control" name="altaddress" id="altaddress" placeholder="Enter alternative address of employee" required>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Password</label>
                                        <input class="form-control" name="password" id="password" type="password" placeholder="Create a password" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Confirm Password</label>
                                        <input class="form-control" name="cpassword" id="cpassword" type="password" placeholder="Re-enter Password" required>
                                    </div>
                                </div>
                            </div><br> 
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Date of birth</label>
                                        <input type="date" class="form-control" name="dob" id="dob" placeholder="Select date of birth" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Education</label>
                                        <input type="text" class="form-control" name="education" id="education" placeholder="Enter education of employee" required>
                                    </div>
                                </div>
                            </div><br>
                            <br>    
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
        function validatePasswords() {
            var password = document.getElementById("password").value;
            var cpassword = document.getElementById("cpassword").value;
            if (password !== cpassword) {
                alert("Passwords do not match.");
                return false;
            }
            return true;
        }
    </script>
</body>
<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/form-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:49:09 GMT -->
</html>
''')
