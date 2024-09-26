#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import header
print(header.homehtml)
cgitb.enable()  # Enable debugging

print("Content-Type: text/html\n")

# Retrieve data from the form
form = cgi.FieldStorage()

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Add your password here
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

# SQL queries to fetch counts
queries = {
    "total_patients": "SELECT COUNT(*) as total_patients FROM patient",
    "total_employees": "SELECT COUNT(*) as total_employees FROM employee",
    "total_appointments": "SELECT COUNT(*) as total_appointments FROM appointment",
    "total_admins": "SELECT COUNT(*) as total_admins FROM register",
    "total_users": "SELECT COUNT(*) as total_users FROM user_register",
    "total_doctors": "SELECT COUNT(*) as total_doctors FROM doctor",
    "total_questions": "SELECT COUNT(*) as total_questions FROM question"
}

results = {}
for key, query in queries.items():
    mycursor.execute(query)
    result = mycursor.fetchone()
    results[key] = result[key] if result else 0

# Closing the cursor and the connection
mycursor.close()
mydb.close()

# Define URLs for images
image_urls = {
    
    "admin": "https://via.placeholder.com/400x200?text=Admins",
    "users": "https://via.placeholder.com/400x200?text=Users",
    "patient": "https://via.placeholder.com/400x200?text=Patients",
    "employee": "https://via.placeholder.com/400x200?text=Employees",
    "appointment": "https://via.placeholder.com/400x200?text=Appointments",
    "doctor": "https://via.placeholder.com/400x200?text=Doctors",
    "Questions": "https://via.placeholder.com/400x200?text=Questions"
}

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
    <h2 class="page-title" style="text-align:center;">Admin's Panel</h2>
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
                                <div id="visitor" style="height:290px; width:125%;" class="m-t-20"></div>
                            </div>
                            <!-- column -->
                            <div class="col-lg-6">
                                <h1 class="display-6 m-b-0 font-medium">45%</h1>
                                <span>Age Groups</span>
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
                    <div class="card-body">
                        <div class="p-t-20 text-center">
                            <i class="mdi mdi-file-chart display-4 text-orange d-block"></i>
                            <span class="display-4 d-block font-medium">{results['total_patients']}</span>
                            <span>Registered Patients</span>
                            <!-- Progress -->
                            <div class="progress m-t-40" style="height:4px;">
                                <div class="progress-bar bg-info" role="progressbar" style="width: 60%" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100"></div>
                                <div class="progress-bar bg-orange" role="progressbar" style="width: 28%" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100"></div>
                                <div class="progress-bar bg-warning" role="progressbar" style="width: 12%" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <!-- Progress -->
                            <!-- row -->
                            <div class="row m-t-30 m-b-20">
                                <!-- column -->
                                <div class="col-4 border-right text-left">
                                    <h3 class="m-b-0 font-medium">60%</h3>Male</div>
                                <!-- column -->
                                <div class="col-4 border-right">
                                    <h3 class="m-b-0 font-medium">28%</h3>Female</div>
                                <!-- column -->
                                <div class="col-4 text-right">
                                    <h3 class="m-b-0 font-medium">12%</h3>Others</div>
                            </div>
                            <a href="patientlist1.py" class="waves-effect waves-light m-t-20 btn btn-lg btn-info accent-4 m-b-20">View More Details</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- ============================================================== -->
        <!-- Email campaign chart -->
        <!-- ============================================================== -->
        <!-- ============================================================== -->
        <!-- Revenue - page-view-bounce rate -->
        <!-- ============================================================== -->
        <div class="row">
    <div class="col-lg-4">
        <a href="appointmentlist1.py">
            <div class="card bg-cyan text-white card-hover">
                <div class="card-body">
                    <h3 class="card-title">Total Appointments</h3>
                    <h3 class="white-text m-b-0"><i class="ti-arrow-up"></i> {results['total_appointments']}</h3>
                    <img style="width:100%; height:auto; aspect-ratio: 2 / 1;" src="{image_urls['appointment']}" alt="Appointments">
                </div>
            </div>
        </a>
    </div>
    <div class="col-lg-4">
        <a href="userlist.py">
            <div class="card bg-danger text-white card-hover">
                <div class="card-body">
                    <h3 class="card-title">Total Users</h3>
                    <h3 class="white-text m-b-0"><i class="ti-arrow-up"></i> {results['total_users']}</h3>
                    <img style="width:100%; height:auto; aspect-ratio: 2 / 1;" src="{image_urls['users']}" alt="Users">
                </div>
            </div>
        </a>
    </div>
    <div class="col-lg-4">
        <a href="patientlist1.py">
            <div class="card bg-success text-white card-hover">
                <div class="card-body">
                    <h3 class="card-title">Total Patients</h3>
                    <h3 class="white-text m-b-0"><i class="ti-arrow-up"></i> {results['total_patients']}</h3>
                    <img style="width:100%; height:auto; aspect-ratio: 2 / 1;" src="{image_urls['patient']}" alt="Patients">
                </div>
            </div>
        </a>
    </div>
</div>

<div class="row">
    <div class="col-lg-4">
        <a href="doctorlist.py">
            <div class="card bg-secondary text-white card-hover">
                <div class="card-body">
                    <h3 class="card-title">Total Doctors</h3>
                    <h3 class="white-text m-b-0"><i class="ti-arrow-up"></i> {results['total_doctors']}</h3>
                    <img style="width:100%; height:auto; aspect-ratio: 2 / 1;" src="{image_urls['doctor']}" alt="Doctors">
                </div>
            </div>
        </a>
    </div>
    <div class="col-lg-4">
        <a href="questionlist.py">
            <div class="card bg-primary text-white card-hover">
                <div class="card-body">
                    <h3 class="card-title">Total Questions</h3>
                    <h3 class="white-text m-b-0"><i class="ti-arrow-up"></i> {results['total_questions']}</h3>
                    <img style="width:100%; height:auto; aspect-ratio: 2 / 1;" src="{image_urls['Questions']}" alt="Questions">
                </div>
            </div>
        </a>
    </div>
    <div class="col-lg-4">
        <a href="employeelist.py">
            <div class="card bg-warning text-white card-hover">
                <div class="card-body">
                    <h3 class="card-title">Total Employees</h3>
                    <h3 class="white-text m-b-0"><i class="ti-arrow-up"></i> {results['total_employees']}</h3>
                    <img style="width:100%; height:auto; aspect-ratio: 2 / 1;" src="{image_urls['employee']}" alt="Employees">
                </div>
            </div>
        </a>
    </div>
</div>

<!-- ============================================================== -->
        <!-- Revenue - page-view-bounce rate -->
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

</html>
''')
