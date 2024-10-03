#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
import header
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")

form = cgi.FieldStorage()
sid = form.getvalue('sid')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

query = f"SELECT * FROM staff WHERE sid ={sid}"
mycursor.execute(query)
myresult = mycursor.fetchone()

#print(myresult)
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
            <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-12 align-self-center">
                        <center><h4 class="page-title">Staff Form</h4></center>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb">
                                    <li class="breadcrumb-item"><a href="#">Staff</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Add Staff</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                 
                </div>
            </div>
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
                <div class="page-breadcrumb">
                <div class="row">
                    <div class="col-12 align-self-center">
                        <center><h4 class="page-title">Staff Form</h4></center>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb">
                                    <li class="breadcrumb-item"><a href="#">Staff</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Add Staff</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                 
                </div>
            </div>
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
    <div class="col-12">     
        <div class="card"  style="padding-left:20px;padding-right:20px">
            <div class="card-body wizard-content">
                <form action="staffupdate.py" class="validation-wizard wizard-circle m-t-40" method="POST">
                <div class="col-md-12" style="margin-left: 12px;">
                         <div class="row"> 
                            <label>ID</label><br>
                            <input type="text" class="form-control" name="id" id="sid" value="{myresult['sid']}" readonly >
                        </div>   
                    </div><br>
                <center><h4 class="card-title">Personal Details</h4></center>
                <div class="row">
                    
                            <div class="col-md-4">
					            <label>First Name<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Firstname" id="Firstname" placeholder="Enter your First Name" patteren="[A-Za-z]+" value="{myresult['Firstname']}" required>
                            </div>
                            
                            
                            <div class="col-md-4">
					            <label>Middle Name<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Middlename" id="Middlename" placeholder="Enter your Middle Name" patteren="[A-Za-z]+" value="{myresult['Middlename']}" required>
                            </div>
                            
                         
				            <div class="col-md-4">
					            <label>Last Name<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Lastname" id="Lastname" placeholder="Enter your last Name" patteren="[A-Za-z]+" value="{myresult['Lastname']}" required>
                            </div>
                            <div class="col-md-4">
                                <label>Phone No<span class="text-danger">*</span> -</label>
                                <input type="tel" class="form-control" name="Phone" id="Phone" value="{myresult['Phone']}" placeholder="Enter Phone No"  required>
                            </div>
                    </div><br>
                    
                    <div class="row">
                        <div class="col-md-6">
					            <label>Address<span class="text-danger">*</span> -</label>
					            <textarea name="Address" id="Address" value="{myresult['Address']}" required rows="3" class="form-control"></textarea>
                        </div>
                       <div class="col-md-6">
                           <div class="form-group">
                                <label for="wintType1">Marital Status -</label>
                                <select class="custom-select form-control required" id="Maritalstatus" value="{myresult['Maritalstatus']}" data-placeholder="Type to select Maritalstatus" name="Maritalstatus">
                                    <option value="Maritalstatus">Select Marital Status</option>
                                    <option value="Married">Married</option>
                                    <option value="Unmarried">Unmarried</option>
                                </select>
                            </div>
                        </div>    
                    </div><br>
                    <div class="row">
                            <div class="col-md-4">
					            <label>Adhar No<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Adhar" id="Adhar" value="{myresult['Adhar']}" placeholder="Enter Adhar No" required="">
                            </div>
                            <div class="col-md-4">
					            <label>PAN No<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Pan" id="Pan" value="{myresult['Pan']}" placeholder="Enter PAN No" required>
                            </div>
                            <div class="col-md-4">
                           <div class="form-group">
                            <label for="wintType1">Passport Number -</label>
                            <input type="text" class="form-control" name="Passport" id="Passport" value="{myresult['Passport']}" placeholder="Enter Passport No">
                           </div>
                        </div>
                    </div><br>
                    <center><h4 class="card-title">Contact Details</h4></center>
                      <div class="row">
                            <div class="col-md-6">
					            <label>Mobile No<span class="text-danger">*</span> -</label>
					            <input type="tel" class="form-control" name="Mobile" id="Mobile" value="{myresult['Mobile']}" placeholder="Enter your Mobile" data-validation-required-message="This field is required" minlength="10" data-validation-containsnumber-message="No Characters Allowed, Only Numbers" data-validation-containsnumber-regex="(\d)+">
                            </div>
                            <div class="col-md-6">
					            <label>Email<span class="text-danger">*</span> -</label>
					            <input type="email" class="form-control" name="Email" id="Email" value="{myresult['Email']}" placeholder="Enter your Email" data-validation-regex-regex="([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})" data-validation-regex-message="Enter Valid Email" data-validation-required-message="This field is required">
                            </div>
                    </div><br>
                    <div class="row">
                            <div class="col-md-4">
					            <label>City<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="City" id="City" value="{myresult['City']}" placeholder="Enter City" required>
                            </div>
                            <div class="col-md-4">
					            <label>Pincode<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Pincode" id="Pincode" value="{myresult['Pincode']}" placeholder="Enter Pincode" required>
                            </div>
                            <div class="col-md-4">
					            <label>Address<span class="text-danger">*</span> -</label>
					            <textarea name="Address2" id="Address2" value="{myresult['Address2']}" required rows="3" class="form-control"></textarea>
                            </div>
                    </div><br>
                    <center><h4 class="card-title"> Educational Details</h4></center>
                        <div class="row">
                            <div class="col-md-4">
					            <label>Higher Educationa<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Education" id="Education" value="{myresult['Education']}" placeholder="Enter Education"  required="">
                            </div>
                            <div class="col-md-4">
					            <label>Specilisation<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Specilisation" id="Specilisation" value="{myresult['Specilisation']}" placeholder="Enter Specilisation Name"  required>
                            </div>
                            <div class="col-md-4">
					            <label>Year of Graduation<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Year" id="Year" value="{myresult['Year']}" placeholder="Enter Year" required>
                            </div>
                    </div><br>
                    <center><h4 class="card-title">Bank Details</h4></center>
                    <div class="row">
                        <div class="col-md-4">
					            <label>Bank Name<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Bankname" id="Bankname" value="{myresult['Bankname']}" placeholder="Enter Bankname Name" patteren="[A-Za-z]+" required="">
                            </div>
                            <div class="col-md-4">
					            <label>Account No<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Accountno" id="Accountno" value="{myresult['Accountno']}" placeholder="Enter Accountno No" patteren="[A-Za-z]+" required>
                            </div>
                            <div class="col-md-4">
					            <label>Account Holder<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Accountholder" id="Accountholder" value="{myresult['Accountholder']}" placeholder="Enter Account Holder Name" required>
                            </div>
                    </div><br>   
                    <div class="row">
                        <div class="col-md-4">
					            <label>Account Type<span class="text-danger">*</span> -</label>
					            <select class="custom-select form-control required" id="Accountype" name="Accountype" value="{myresult['Accountype']}">
                                    <option value="">Select Account Type</option>
                                    <option value="Checking">Checking</option>
                                    <option value="Saving">Saving</option>
                                </select>
                            </div>
                            <div class="col-md-4">
					            <label>IFSC Code<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Ifsccode" id="Ifsccode" value="{myresult['Ifsccode']}" placeholder="Enter IFSC Code" patteren="[A-Za-z]+" required>
                            </div>
                            <div class="col-md-4">
					            <label>Bank Branch<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Bankbranch" id="Bankbranch" value="{myresult['Bankbranch']}" placeholder="Enter Bank Branch" patteren="[A-Za-z]+" required>
                            </div>
                    </div><br>
                <center><h4 class="card-title"> Employment Details</h4></center>
                <div class="row">
                    <div class="col-md-4">
					            <label>Department<span class="text-danger">*</span> -</label>
					            <input type="text" class="form-control" name="Department" id="Department" value="{myresult['Department']}" placeholder="Enter Department"  required="">
                     </div>
                    <div class="col-md-4">
					    <label>Job Title<span class="text-danger">*</span> -</label>
					    <input type="text" class="form-control" name="Jobtitle" id="Jobtitle" value="{myresult['Jobtitle']}" placeholder="Enter Job Title"  required>
                    </div>
                    <div class="col-md-4">
                        <label>Employment Status -</label>
                        <select class="custom-select form-control required" name="Employmentstatus" id="Employmentstatus" value="{myresult['Employmentstatus']}" data-placeholder="Type to select Employment Status" >
                                    <option value="Employmentstatus">Select Employment Status</option>
                                    <option value="Full-Time">Full-Time</option>
                                    <option value="Part-Time">Part-Time</option>
                                    <option value="Contract">Contract</option>
                                </select>
                        </div><br>
                    <div class="row">
                        <div class="col-md-4">
					            <label>Work Experience<span class="text-danger">*</span> -</label>
					            <input type="number" class="form-control" name="Experience" id="Experience" value="{myresult['Experience']}" placeholder="Enter Experience" required>
                        </div>
                        <div class="col-md-4">
                            <label>Start Time</label>
                                <div class="col-sm-9">
                                    <input type="time" class="form-control" id="Stime" name="Stime" value="{myresult['Stime']}">
                                </div>
                        </div>
                        <div class="col-md-4">
                            <label>End Time</label>
                                <div class="col-sm-9">
                                    <input type="time" class="form-control" id="Etime" name="Etime" value="{myresult['Etime']}">
                                </div>
                        </div>
                    </div><br>
                    <center><button type="update" class="btn btn-success">Update</button></center>
                </form>
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
       All Rights Reserved by Xtreme admin. Designed and Developed by <a href="https://wrappixel.com/">WrapPixel</a>.
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
    <aside class="customizer">
        <a href="javascript:void(0)" class="service-panel-toggle"><i class="fa fa-spin fa-cog"></i></a>
        <div class="customizer-body">
            <ul class="nav customizer-tab" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" id="pills-home-tab" data-toggle="pill" href="#pills-home" role="tab" aria-controls="pills-home" aria-selected="true"><i class="mdi mdi-wrench font-20"></i></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" id="pills-profile-tab" data-toggle="pill" href="#chat" role="tab" aria-controls="chat" aria-selected="false"><i class="mdi mdi-message-reply font-20"></i></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" id="pills-contact-tab" data-toggle="pill" href="#pills-contact" role="tab" aria-controls="pills-contact" aria-selected="false"><i class="mdi mdi-star-circle font-20"></i></a>
                </li>
            </ul>
            <div class="tab-content" id="pills-tabContent">
                <!-- Tab 1 -->
                <div class="tab-pane fade show active" id="pills-home" role="tabpanel" aria-labelledby="pills-home-tab">
                    <div class="p-15 border-bottom">
                        <!-- Sidebar -->
                        <h5 class="font-medium m-b-10 m-t-10">Layout Settings</h5>
                        <div class="custom-control custom-checkbox m-t-10">
                            <input type="checkbox" class="custom-control-input" name="theme-view" id="theme-view">
                            <label class="custom-control-label" for="theme-view">Dark Theme</label>
                        </div>
                        <div class="custom-control custom-checkbox m-t-10">
                            <input type="checkbox" class="custom-control-input sidebartoggler" name="collapssidebar" id="collapssidebar">
                            <label class="custom-control-label" for="collapssidebar">Collapse Sidebar</label>
                        </div>
                        <div class="custom-control custom-checkbox m-t-10">
                            <input type="checkbox" class="custom-control-input" name="sidebar-position" id="sidebar-position">
                            <label class="custom-control-label" for="sidebar-position">Fixed Sidebar</label>
                        </div>
                        <div class="custom-control custom-checkbox m-t-10">
                            <input type="checkbox" class="custom-control-input" name="header-position" id="header-position">
                            <label class="custom-control-label" for="header-position">Fixed Header</label>
                        </div>
                        <div class="custom-control custom-checkbox m-t-10">
                            <input type="checkbox" class="custom-control-input" name="boxed-layout" id="boxed-layout">
                            <label class="custom-control-label" for="boxed-layout">Boxed Layout</label>
                        </div>
                    </div>
                    <div class="p-15 border-bottom">
                        <!-- Logo BG -->
                        <h5 class="font-medium m-b-10 m-t-10">Logo Backgrounds</h5>
                        <ul class="theme-color">
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-logobg="skin1"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-logobg="skin2"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-logobg="skin3"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-logobg="skin4"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-logobg="skin5"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-logobg="skin6"></a></li>
                        </ul>
                        <!-- Logo BG -->
                    </div>
                    <div class="p-15 border-bottom">
                        <!-- Navbar BG -->
                        <h5 class="font-medium m-b-10 m-t-10">Navbar Backgrounds</h5>
                        <ul class="theme-color">
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-navbarbg="skin1"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-navbarbg="skin2"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-navbarbg="skin3"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-navbarbg="skin4"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-navbarbg="skin5"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-navbarbg="skin6"></a></li>
                        </ul>
                        <!-- Navbar BG -->
                    </div>
                    <div class="p-15 border-bottom">
                        <!-- Logo BG -->
                        <h5 class="font-medium m-b-10 m-t-10">Sidebar Backgrounds</h5>
                        <ul class="theme-color">
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-sidebarbg="skin1"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-sidebarbg="skin2"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-sidebarbg="skin3"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-sidebarbg="skin4"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-sidebarbg="skin5"></a></li>
                            <li class="theme-item"><a href="javascript:void(0)" class="theme-link" data-sidebarbg="skin6"></a></li>
                        </ul>
                        <!-- Logo BG -->
                    </div>
               </div>
                <!-- End Tab 1 -->
                <!-- Tab 2 -->
                <div class="tab-pane fade" id="chat" role="tabpanel" aria-labelledby="pills-profile-tab">
                    <ul class="mailbox list-style-none m-t-20">
                        <li>
                            <div class="message-center chat-scroll">
                                <a href="javascript:void(0)" class="message-item" id='chat_user_1' data-user-id='1'>
                                    <span class="user-img"> <img src="../../assets/images/users/1.jpg" alt="user" class="rounded-circle"> <span class="profile-status online pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Pavan kumar</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:30 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_2' data-user-id='2'>
                                    <span class="user-img"> <img src="../../assets/images/users/2.jpg" alt="user" class="rounded-circle"> <span class="profile-status busy pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Sonu Nigam</h5> <span class="mail-desc">I've sung a song! See you at</span> <span class="time">9:10 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_3' data-user-id='3'>
                                    <span class="user-img"> <img src="../../assets/images/users/3.jpg" alt="user" class="rounded-circle"> <span class="profile-status away pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Arijit Sinh</h5> <span class="mail-desc">I am a singer!</span> <span class="time">9:08 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_4' data-user-id='4'>
                                    <span class="user-img"> <img src="../../assets/images/users/4.jpg" alt="user" class="rounded-circle"> <span class="profile-status offline pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Nirav Joshi</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_5' data-user-id='5'>
                                    <span class="user-img"> <img src="../../assets/images/users/5.jpg" alt="user" class="rounded-circle"> <span class="profile-status offline pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Sunil Joshi</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_6' data-user-id='6'>
                                    <span class="user-img"> <img src="../../assets/images/users/6.jpg" alt="user" class="rounded-circle"> <span class="profile-status offline pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Akshay Kumar</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_7' data-user-id='7'>
                                    <span class="user-img"> <img src="../../assets/images/users/7.jpg" alt="user" class="rounded-circle"> <span class="profile-status offline pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Pavan kumar</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                </a>
                                <!-- Message -->
                                <!-- Message -->
                                <a href="javascript:void(0)" class="message-item" id='chat_user_8' data-user-id='8'>
                                    <span class="user-img"> <img src="../../assets/images/users/8.jpg" alt="user" class="rounded-circle"> <span class="profile-status offline pull-right"></span> </span>
                                    <div class="mail-contnet">
                                        <h5 class="message-title">Varun Dhavan</h5> <span class="mail-desc">Just see the my admin!</span> <span class="time">9:02 AM</span> </div>
                                </a>
                                <!-- Message -->
                            </div>
                        </li>
                    </ul>
                </div>
                <!-- End Tab 2 -->
                <!-- Tab 3 -->
                <div class="tab-pane fade p-15" id="pills-contact" role="tabpanel" aria-labelledby="pills-contact-tab">
                    <h6 class="m-t-20 m-b-20">Activity Timeline</h6>
                    <div class="steamline">
                        <div class="sl-item">
                            <div class="sl-left bg-success"> <i class="ti-user"></i></div>
                            <div class="sl-right">
                                <div class="font-medium">Meeting today <span class="sl-date"> 5pm</span></div>
                                <div class="desc">you can write anything </div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left bg-info"><i class="fas fa-image"></i></div>
                            <div class="sl-right">
                                <div class="font-medium">Send documents to Clark</div>
                                <div class="desc">Lorem Ipsum is simply </div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left"> <img class="rounded-circle" alt="user" src="../../assets/images/users/2.jpg"> </div>
                            <div class="sl-right">
                                <div class="font-medium">Go to the Doctor <span class="sl-date">5 minutes ago</span></div>
                                <div class="desc">Contrary to popular belief</div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left"> <img class="rounded-circle" alt="user" src="../../assets/images/users/1.jpg"> </div>
                            <div class="sl-right">
                                <div><a href="javascript:void(0)">Stephen</a> <span class="sl-date">5 minutes ago</span></div>
                                <div class="desc">Approve meeting with tiger</div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left bg-primary"> <i class="ti-user"></i></div>
                            <div class="sl-right">
                                <div class="font-medium">Meeting today <span class="sl-date"> 5pm</span></div>
                                <div class="desc">you can write anything </div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left bg-info"><i class="fas fa-image"></i></div>
                            <div class="sl-right">
                                <div class="font-medium">Send documents to Clark</div>
                                <div class="desc">Lorem Ipsum is simply </div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left"> <img class="rounded-circle" alt="user" src="../../assets/images/users/4.jpg"> </div>
                            <div class="sl-right">
                                <div class="font-medium">Go to the Doctor <span class="sl-date">5 minutes ago</span></div>
                                <div class="desc">Contrary to popular belief</div>
                            </div>
                        </div>
                        <div class="sl-item">
                            <div class="sl-left"> <img class="rounded-circle" alt="user" src="../../assets/images/users/6.jpg"> </div>
                            <div class="sl-right">
                                <div><a href="javascript:void(0)">Stephen</a> <span class="sl-date">5 minutes ago</span></div>
                                <div class="desc">Approve meeting with tiger</div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- End Tab 3 -->
            </div>
        </div>
    </aside>
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


<!-- Mirrored from themedesigner.in/demo/wrappixel/admin-template/xtreme/html/ltr/form-basic.html by HTTrack Website Copier/3.x [XR&CO'2014], Wed, 06 Jun 2018 05:49:09 GMT -->
</html>
''')