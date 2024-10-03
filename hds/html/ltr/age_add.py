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
                <form class="m-t-30" action="questionbackend.py" method="POST" enctype="multipart/form-data">
                       
                        <div class="col-md-12">
					            <div class="row"> 
                                    <div class="col-md-12">
					                    <label>Patient Age Group</label><br>
                                        <select class="form-control" name="age" id="age" aria-describedby="emailHelp">
                                            <option value="placeholder" selected>Select Patient Age Group</option>
                                            <option>0-1 year</option>
                                            <option>1-2 year</option>
                                            <option>2-3 year</option>
                                            <option>3-4 year</option>
                                            <option>4-5 year</option>
                                            <option>5-6 year</option>
                                            <option>Add age year group</option>
                                        </select>                                     
                                    </div>
                                </div>
                            </div><br>
                        </div>
                    </div>
                        <br>
                        
                    
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