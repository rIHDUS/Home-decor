#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")
form=cgi.FieldStorage()
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hearing"
)
mycursor=mydb.cursor(dictionary=True)
query=f'''SELECT * FROM question'''
#print(query)
mycursor.execute(query)
result=mycursor.fetchall()
option = ''
for x in result:
        option += f'<option value="{x["id"]}">{x["age"]} {x["question"]}</option>\n'

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
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Client Form</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb">
                                    <li class="breadcrumb-item"><a href="#">Home</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Library</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                   <div class="col-7 align-self-center">
                        <div class="d-flex no-block justify-content-end align-items-center">
                            <!--<div class="m-r-10">
                                <div class="lastmonth"></div>
                            </div>-->
                           <div class="">
                       <!-- <a href="Doumentadd.py"> <button type="submit" class="btn btn-success"><i class="fa fa-save"
                             id="show_loader"></i>&nbsp;Add Document
                                </button></a>--></div>
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
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h6 class="card-subtitle">  </h6>
                                <form id="add_client" name="add_client" role="form" method="POST"
                      action="taskaddbackend.py">
                     <div class="x_content">

                        <div class="row">

                            <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Subject <span class="text-danger">*</span></label>
                                <input type="text" placeholder="" class="form-control" id="task_subject"
                                       name="task_subject">
                            </div>

                            <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Start Date <span class="text-danger">*</span></label>
                                <input type="date" placeholder="" class="form-control dateFrom" id="start_date"
                                       name="start_date">
                            </div>

                            <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Deadline<span class="text-danger">*</span></label>
                                <input type="date" placeholder="" class="form-control dateTo" id="end_date"
                                       name="end_date">
                            </div>
                        </div>

                       <div class="row">
                                    <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                        <label for="fullname">Select Status: <span class="text-danger">*</span></label>
                                        <select class="form-control" id="project_status_id" name="project_status_id">
                                            <option value="">Select status</option>
                                             <option value="not_started">Not_started</option>
                                     <option value="completed">Completed</option>
                                     <option value="in_progress">In Progress</option>
                                     <option value="deferred">Deferred</option>
                                         <option value="other">Other</option>
                                        </select>
                                    </div>
                                    <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Priority <span class="text-danger">*</span></label>
                                <select class="form-control" id="priority" name="priority">
                                    <option value="">Select priority</option>
                                    <option low="completed">Low</option>
                                     <option value="medium">Medium</option>
                                     <option value="high">High</option>
                                      <option value="urgent">Urgent</option>
                                </select>
                            </div>
                            
                       
                            <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Related To</label>
                                <select class="form-control selct2-width-100" id="related" name="related">
                                    <option value="">Noting Selected</option>
                                    <option value="case">Case</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>

                            <div class="col-md-4 col-sm-12 col-xs-12 form-group task_selection hide">
                                <label for="fullname">Case</label>
                                <select class="form-control selct2-width-100" id="related_id" name="related_id">
                                    <option value="">Select user</option>

                                </select>

                            </div>
                     

                                </div>

                            <div class="col-md-4 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Assign To<span class="text-danger">*</span></label>

                  <select  name="assigned_to" id="assigned_to" class="form-control form-group" required>
                            <option value="">Select Employee </option>"

                                    {option}
                                </select>

                            </div>
                        </div>


                        <div class="row">
                            <div class="col-md-12 col-sm-12 col-xs-12 form-group">
                                <label for="fullname">Description:</label>
                                <textarea class="form-control" id="task_description"
                                          name="task_description"></textarea>
                            </div>
                        </div>

                        <div class="form-group pull-right">
                            <div class="col-md-12 col-sm-6 col-xs-12">
                                <a class="btn btn-danger" href="{{ route('tasks.index') }}">Cancel</a>
                                <button type="submit" class="btn btn-success"><i class="fa fa-save"
                                                                                 id="show_loader"></i>&nbsp;Save
                                </button>
                            </div>
                        </div>

                    </div>
                  </form>

                                
                            </div>
                        </div>
                    </div>
                </div>
                <!-- row -->
                <!-- .row -->
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
           ''')