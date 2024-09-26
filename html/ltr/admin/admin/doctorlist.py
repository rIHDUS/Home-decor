#!C:/Python312/python.exe
import cgi
import cgitb
import header
import mysql.connector
cgitb.enable()
print(header.homehtml)
print("Content-type: text/html\n")
form = cgi.FieldStorage()

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

query = "SELECT * FROM doctor"

mycursor.execute(query)


myresult = mycursor.fetchall()

tr_html = ''
for x in myresult:
    tr_html += f'''
        <tr>
            <td>
                <a href="doctor_edit.py?doct_id={x['id']}"><button class="btn btn-success"><i class="fas fa-edit"></i></button></a>
                <a href="doctor_delete.py?doct_id={x['id']}"><button class="btn btn-danger"><i class="fas fa-trash"></i></button></a>
            </td>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['number']}</td>
            <td>{x['email']}</td>
            <td>{x['experience']}</td>
            <td>{x['degree']}</td>
            <td>{x['otherdegree']}</td>
        </tr>
    '''

# Pagination controls


# Search form and table display
print(f'''
<div class="page-wrapper">
<div class="page-breadcrumb">
                <div class="row">
                    <div class="col-5 align-self-center">
                        <h4 class="page-title">Admin's Panel</h4>
                        <div class="d-flex align-items-center">
                            <nav aria-label="breadcrumb">
                                <ol class="breadcrumb">
                                    <li class="breadcrumb-item"><a href="dashboard.py">Home</a></li>
                                    <li class="breadcrumb-item active" aria-current="page">Doctor's List</li>
                                </ol>
                            </nav>
                        </div>
                    </div>
                    <div class="col-7 align-self-center">
                        
                    </div>
                </div>
            </div>
<div class="container-fluid">     
 <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body">
                                <h2 class="card-title">Doctor's Data</h2>
                                
                                <div class="table-responsive">
                                    <table id="multi_control" class="table table-striped table-bordered display" style="width:100%">                                
                                <thead>
                                   <tr style="background-color:powderblue;">
                                        <th>Action</th>
                                        <th>Sr.no.</th>
                                        <th scope="col">firstname</th>
                                        <th scope="col">middlename</th>
                                        <th scope="col">lastname</th>
                                        <th scope="col">number</th>
                                        <th scope="col">email</th>
                                        <th scope="col">experience</th>
                                        <th scope="col">degree</th>
                                        <th scope="col">otherdegree</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {tr_html}
                                </tbody>
                            </table>
                        </div>
                        <div style="text-align:center;">
                            
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    </div>
    </div>
    
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
</div>
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
    <!--This page plugins -->
    <script src="../../assets/extra-libs/DataTables/datatables.min.js"></script>
    <!-- start - This is for export functionality only -->
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/dataTables.buttons.min.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.flash.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/pdfmake.min.js"></script>
    <script src="../../../../../../../cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.32/vfs_fonts.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.html5.min.js"></script>
    <script src="../../../../../../../cdn.datatables.net/buttons/1.5.1/js/buttons.print.min.js"></script>
    <script src="../../dist/js/pages/datatable/datatable-advanced.init.js"></script>
</body>
</html> 
''')
