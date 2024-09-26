#!C:/Python312/python.exe
import header
print (header.homehtml)
print('''
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
                                <form action="patientbackend.py" class="tab-wizard wizard-circle">
                                    <!-- Step 1 -->
                                    <h6>Basic Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="firstName">First Name</label>
                                            <input type="text" class="form-control" id="fname" name="fname" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="middleName">Middle Name</label>
                                            <input type="text" class="form-control" id="mname" name="mname" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="lastName">Last Name</label>
                                            <input type="text" class="form-control" id="lname" name="lname" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="motherName">Mother Name</label>
                                            <input type="text" class="form-control" id="momname" name="momnaame" required>
                                        </div>
                                    </section>
                                    <!-- Step 2 -->
                                    <h6>Other Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="control-label">Gender</label><br>
                                            <select class="form-control" name="gender" id="gender" aria-describedby="emailHelp" required>
                                                <option value="">Please select one … </option>
                                                <option value="female">Female</option>
                                                <option value="male">Male</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="birthdate">Date of birth</label>
                                            <input type="date" class="form-control" id="dob" name="dob" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="age">Age</label>
                                            <input type="number" class="form-control" id="age" name="age" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="bloodgroup">Blood Group</label>
                                            <select class="form-control" name="bloodgroup" id="bloodgroup" aria-describedby="emailHelp">
                                                <option value="placeholder" selected>Select Patient Blood Group</option>
                                                <option>A Positive</option>
                                                <option>A Negative</option>
                                                <option>B Positive</option>
                                                <option>B Negative</option>
                                                <option>AB Positive</option>
                                                <option>AB Negative</option>
                                                <option>O Positive</option>
                                                <option>O Negative</option>
                                                <option>Unknown</option>
                                            </select>                    
                                        </div>
                                        <div class="form-group">
                                            <label for="refference">Doctor Refference</label>
                                            <input type="text" class="form-control" id="refference" name="refference" required>
                                        </div>
                                    </section>
                                    <!-- Step 3 -->
                                    <h6>Parent Information</h6>
                                    <section>
                                        <div class="form-group">
                                            <label for="mob">Mobile No.</label>
                                            <input type="tel" class="form-control" id="mobno" name="mobno" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="email">Email</label>
                                            <input type="email" class="form-control" id="email" name="email" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="occuption">Occuption</label>
                                            <input type="text" class="form-control" id="occuption" name="occuption" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="relation">Parent Relation</label>
                                            <input type="text" class="form-control" id="relation" name="relation" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="password">Password</label>
                                            <input type="password" class="form-control" id="password" name="password" required>                    
                                        </div>
                                    </section>
                                    <!-- Step 4 -->
                                    <h6>Address Information</h6>
                                     <section>
                                        <div class="form-group">
                                            <label for="country">Country</label>
                                            <input type="text" class="form-control" value="India" id="country" name="country" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="state">State</label>
                                            <select id="states" name="states" class="form-control" required>
                                                <option value="Andhra Pradesh">Andhra Pradesh</option>
                                                <option value="Arunachal Pradesh">Arunachal Pradesh</option>
                                                <option value="Assam">Assam</option>
                                                <option value="Bihar">Bihar</option>
                                                <option value="Chhattisgarh">Chhattisgarh</option>
                                                <option value="Goa">Goa</option>
                                                <option value="Gujarat">Gujarat</option>
                                                <option value="Haryana">Haryana</option>
                                                <option value="Himachal Pradesh">Himachal Pradesh</option>
                                                <option value="Jharkhand">Jharkhand</option>
                                                <option value="Karnataka">Karnataka</option>
                                                <option value="Kerala">Kerala</option>
                                                <option value="Madhya Pradesh">Madhya Pradesh</option>
                                                <option value="Maharashtra" selected>Maharashtra</option>
                                                <option value="Manipur">Manipur</option>
                                                <option value="Meghalaya">Meghalaya</option>
                                                <option value="Mizoram">Mizoram</option>
                                                <option value="Nagaland">Nagaland</option>
                                                <option value="Odisha">Odisha</option>
                                                <option value="Punjab">Punjab</option>
                                                <option value="Rajasthan">Rajasthan</option>
                                                <option value="Sikkim">Sikkim</option>
                                                <option value="Tamil Nadu">Tamil Nadu</option>
                                                <option value="Telangana">Telangana</option>
                                        </div>
                                                <option value="Tripura">Tripura</option>
                                                <option value="Uttar Pradesh">Uttar Pradesh</option>
                                                <option value="Uttarakhand">Uttarakhand</option>
                                                <option value="West Bengal">West Bengal</option>
                                                <option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
                                                <option value="Chandigarh">Chandigarh</option>
                                                <option value="Dadra and Nagar Haveli and Daman and Diu">Dadra and Nagar Haveli and Daman and Diu</option>
                                                <option value="Lakshadweep">Lakshadweep</option>
                                                <option value="Delhi">Delhi</option>
                                                <option value="Puducherry">Puducherry</option>
                                                <option value="Ladakh">Ladakh</option>
                                                <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                                            </select>                    
                                        </div>
                                        <div class="form-group">
                                            <label for="city">City</label>
                                            <input type="text" class="form-control" id="city" name="city" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="area">Area / Street</label>
                                            <input type="text" class="form-control" id="area" name="area" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="build_name">Building / House Name</label>
                                            <input type="text" class="form-control" id="bld_name" name="bld_name" required>
                                        </div>
                                        <div class="form-group">
                                            <label for="build_name">Pincode</label>
                                            <input type="text" class="form-control" id="pincode" name="pincode" required>
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
  $(".tab-wizard").steps({
      headerTag: "h6",
      bodyTag: "section",
      transitionEffect: "fade",
      titleTemplate: '<span class="step">#index#</span> #title#',
      labels: {
          finish: "Submit"
      },
      onFinished: function(event, currentIndex) {
          $("form").submit();
      }
  });
</script>

</body>
</html>
      ''')