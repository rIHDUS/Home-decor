#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import header
print(header.homehtml)
cgitb.enable()  # Enable debugging

print("Content-type: text/html\n")

print(f'''
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
            <h2 class="page-title" style="text-align:center;">Dashboard</h2>
            <!-- ============================================================== -->
            <!-- End Bread crumb and right sidebar toggle -->
            <!-- ============================================================== -->
            <!-- ============================================================== -->
            <!-- Container fluid  -->
            <!-- ============================================================== -->
            <div class="container-fluid">
                <!-- ============================================================== -->
                <!-- Sales chart -->
                <!-- ============================================================== -->
                
                <!-- ============================================================== -->
                <!-- Sales chart -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Email campaign chart -->
                <!-- ============================================================== -->
                <div class="row">
                    <div class="col-lg-8 col-xl-6">
                        <div class="card card-hover">
                            <div class="card-body">
                                <div class="d-md-flex align-items-center">
                                    <div>
                                        <h4 class="card-title">Email Campaigns</h4>
                                        <h5 class="card-subtitle">Overview of Email Campaigns</h5>
                                    </div>
                                    <div class="ml-auto align-items-center">
                                        <div class="dl">
                                            <select class="custom-select">
                                                <option value="0" selected>Monthly</option>
                                                <option value="1">Daily</option>
                                                <option value="2">Weekly</option>
                                                <option value="3">Yearly</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <!-- column -->
                                <div class="row m-t-40">
                                    <!-- column -->
                                    <div class="col-lg-6">
                                        <div id="visitor" style="height:290px; width:100%;" class="m-t-20"></div>
                                    </div>
                                    <!-- column -->
                                    <div class="col-lg-6">
                                        <h1 class="display-6 m-b-0 font-medium">45%</h1>
                                        <span>Open Ratio for Campaigns</span>
                                        <ul class="list-style-none">
                                            <li class="m-t-20"><i class="fas fa-circle m-r-5 text-cyan font-12"></i> 0-1 <span class="float-right">45%</span></li>
                                            <li class="m-t-20"><i class="fas fa-circle m-r-5 text-info font-12"></i> 1-2 <span class="float-right">14%</span></li>
                                            <li class="m-t-20"><i class="fas fa-circle m-r-5 text-orange font-12"></i> 2-3 <span class="float-right">5%</span></li>
                                            <li class="m-t-20"><i class="fas fa-circle m-r-5 text-primary font-12"></i> 3-4 <span class="float-right">17%</span></li>
                                            <li class="m-t-20"><i class="fas fa-circle m-r-5 text-danger font-12"></i>  4-5 <span class="float-right">20%</span></li>
                                            <li class="m-t-20"><i class="fas fa-circle m-r-5 text-secondary font-12"></i>  5-6 <span class="float-right">20%</span></li>
                                        </ul>
                                    </div>
                                </div>
                                <!-- column -->
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-xl-6">
                        <div class="card card-hover">
                            <div class="card-body" style="background:url(../../assets/images/background/active-bg.png) no-repeat top center;">
                                <div class="p-t-20 text-center">
                                    <i class="mdi mdi-file-chart display-4 text-orange d-block"></i>
                                    <span class="display-4 d-block font-medium">368</span>
                                    <span>Active Visitors on Site</span>
                                    <!-- Progress -->
                                    <div class="progress m-t-40" style="height:4px;">
                                        <div class="progress-bar bg-info" role="progressbar" style="width: 15%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
                                        <div class="progress-bar bg-orange" role="progressbar" style="width: 30%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
                                        <div class="progress-bar bg-warning" role="progressbar" style="width: 65%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
                                    </div>
                                    <!-- Progress -->
                                    <!-- row -->
                                    <div class="row m-t-30 m-b-20">
                                        <!-- column -->
                                        <div class="col-4 border-right text-left">
                                            <h3 class="m-b-0 font-medium">60%</h3>Desktop</div>
                                        <!-- column -->
                                        <div class="col-4 border-right">
                                            <h3 class="m-b-0 font-medium">28%</h3>Mobile</div>
                                        <!-- column -->
                                        <div class="col-4 text-right">
                                            <h3 class="m-b-0 font-medium">12%</h3>Tablet</div>
                                    </div>
                                    <a href="javascript:void(0)" class="waves-effect waves-light m-t-20 btn btn-lg btn-info accent-4 m-b-20">View More Details</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- ============================================================== -->
                <!-- Email campaign chart -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Ravenue - page-view-bounce rate -->
                <!-- ============================================================== -->
                <div class="row">
                    <div class="col-lg-4">
                        <a href="aadhar.py">
                            <div class="card bg-danger text-white card-hover">
                                <div class="card-body">
                                    <h3 class="card-title" style="text-align:center;">Aadhar Card</h3>
                                    <img style="width:100%;" src="https://digitalindia-gov.com/wp-content/uploads/2023/07/digitalindiaportals.in_-1024x1024.png">
                                </div>
                            </div>
                        </a>
                    </div>
                    <div class="col-lg-4">
                        <a href="pancard.py">
                            <div class="card bg-primary text-white card-hover">
                                <div class="card-body">
                                    <img style="width:100%;" src="https://5.imimg.com/data5/SELLER/Default/2024/3/403613469/ML/WV/UD/47205122/untitled.png">
                                </div>
                            </div>
                        </a>
                    </div>
                    <div class="col-lg-4">
                        <a href="vehicleregistration.py">
                            <div class="card bg-dark text-white card-hover">
                                <div class="card-body">
                                    <img style="width:100%;" src="https://formhouse.in/wp-content/uploads/2021/08/Custom-dimensions-400x400-px3.jpeg">
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="row">
                    <div class="col-lg-4">
                        <a href="passport.py">
                            <div class="card bg-info text-white card-hover">
                                <div class="card-body">
                                    <img style="width:100%;" src="https://pbs.twimg.com/media/E2A7Qv0UcAENXgr.jpg">
                                </div>
                            </div>
                        </a>
                    </div>
                    <div class="col-lg-4">
                        <a href="foodlicence.py">
                            <div class="card bg-success text-white card-hover">
                                <div class="card-body">
                                    <img style="width:100%;" src="https://5.imimg.com/data5/SELLER/Default/2022/4/OQ/HJ/SG/97945019/fssai-central-license-for-food-business-500x500.jpg">
                                </div>
                            </div>
                        </a>
                    </div>                    
                    
                    <div class="col-lg-4">
                        <a href="voterid.py">
                            <div class="card bg-orange text-white card-hover">
                                <div class="card-body">
                                    <img style="width:100%;" src="https://zaminwale.com/assets/images/7.12.png">
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
                <!-- ============================================================== -->
                <!-- Ravenue - page-view-bounce rate -->
                <!-- ============================================================== -->
                <!-- ============================================================== -->
                <!-- Table -->
                <!-- ============================================================== -->
                
                <!-- ============================================================== -->
                <!-- Table -->
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
    <!--This page JavaScript -->
    <!--chartis chart-->
    <script src="../../assets/libs/chartist/dist/chartist.min.js"></script>
    <script src="../../assets/libs/chartist-plugin-tooltips/dist/chartist-plugin-tooltip.min.js"></script>
    <!--c3 charts -->
    <script src="../../assets/extra-libs/c3/d3.min.js"></script>
    <script src="../../assets/extra-libs/c3/c3.min.js"></script>
    <!--chartjs -->
    <script src="../../assets/libs/chart.js/dist/Chart.min.js"></script>
    <script src="../../dist/js/pages/dashboards/dashboard1.js"></script>
</body>


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/index.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:46:30 GMT -->
</html>
''')
