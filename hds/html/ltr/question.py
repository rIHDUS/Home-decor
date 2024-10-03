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
                <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b></b></h4><br>    
                <form class="m-t-5" action="questionbackend.py" method="POST" enctype="multipart/form-data">
                            <div class="card">
                         <div ="card-body">
                            <br><h4 class="card-subtitle" style="color:green; text-align:center; font-family:sans-serif;"><b>Patient Mcq Questions</b></h4><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-12">
                                        <label for="control-label">Question</label>
                                        <input class="form-control" name="question" id="question" type="text" placeholder="Enter question" required>
                                    </div>
                                    
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
					                    <label>Option 1</label><br>
					                    <input type="text" class="form-control" name="option1" id="option1" aria-describedby="emailHelp" placeholder="Enter option 1" required>
                                     </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Option 2 </label>
                                        <input type="text" class="form-control" name="option2" id="option2" placeholder="Enter option 2" required>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
                                        <label for="control-label">Option 3</label>
                                        <input type="text" class="form-control" name="option3" id="option3" placeholder="Enter Option 3" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label for="control-label">Option 4</label>
                                        <input type="text" class="form-control" name="option4" id="option4" placeholder="Enter Option 4" required>
                                    </div>
                                </div>
                            </div><br>
                            <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-6">
					                    <label>Correct option</label><br>
                                        <select class="form-control" name="coption" id="coption" aria-describedby="emailHelp">
                                            <option value="placeholder" selected>Select correct option</option>
                                            <option value="option 1">Option 1</option>
                                            <option value="option 2">Option 2</option>
                                            <option value="option 3">Option 3</option>
                                            <option value="option 4">Option 4</option>
                                        </select>                                     
                                    </div>
                                </div>
                            </div><br>
                        </div>
                    
                            <center><button type="submit" class="btn btn-success">Submit</button></center></div><br>
                </form><br>
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