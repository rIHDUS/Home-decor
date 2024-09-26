#!C:/Python312/python.exe
import header
print(header.homehtml)
print('''
        <div class="page-wrapper">
            <br><center><h2>Doctor Form</h2></center><br>
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <div class="card">
                            <div class="card-body wizard-content">
<form action="doctorbackend.py" class="tab-wizard wizard-circle">
    <div class="form-group">
        <label for="firstname">First Name</label>
        <input id="firstname" type="text" class="form-control" name="firstname" placeholder="Enter first name" required />
    </div>
    <div class="form-group">
        <label for="middlename">Middle Name</label>
        <input id="middlename" type="text" class="form-control" name="middlename" placeholder="Enter middle name" />
    </div>
    <div class="form-group">
        <label for="lastname">Last Name</label>
        <input id="lastname" type="text" class="form-control" name="lastname" placeholder="Enter last name" required />
    </div>
    
    <!-- Contact Details Section with Number and Email in the Same Line -->
    <div class="form-row">
        <div class="form-group col-md-6">
            <label for="number">Contact Number</label>
            <input id="number" type="text" class="form-control" name="number" placeholder="Enter contact number" required />
        </div>
        <div class="form-group col-md-6">
            <label for="email">Email</label>
            <input id="email" type="email" class="form-control" name="email" placeholder="Enter email address" required />
        </div>
    </div>

    <div class="form-group">
        <label for="experience">Previous Experience (in years)</label>
        <input id="experience" type="number" class="form-control" name="experience" placeholder="Enter previous experience" required />
    </div>
    <div class="form-group">
        <label for="degree">Degree</label>
        <select class="form-control" name="degree" id="degree" required>
            <option value="Audiologist" selected>Audiologist</option>
            <option value="Other">Other</option>
        </select>
    </div>
    <div class="form-group">
        <label for="otherdegree">If Other, Please Specify</label>
        <input id="otherdegree" type="text" class="form-control" name="otherdegree" placeholder="Specify other degree" />
    </div>
    
    <center><button type="submit" class="btn btn-info">Submit</button></center>
</form>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
    
    <script src="../../assets/libs/jquery/dist/jquery.min.js"></script>
    <script src="../../assets/libs/popper.js/dist/umd/popper.min.js"></script>
    <script src="../../assets/libs/bootstrap/dist/js/bootstrap.min.js"></script>
    <script src="../../dist/js/app.min.js"></script>
    <script src="../../dist/js/app.init.js"></script>
    <script src="../../dist/js/app-style-switcher.js"></script>
    <script src="../../assets/libs/perfect-scrollbar/dist/perfect-scrollbar.jquery.min.js"></script>
    <script src="../../assets/extra-libs/sparkline/sparkline.js"></script>
    <script src="../../dist/js/waves.js"></script>
    <script src="../../dist/js/sidebarmenu.js"></script>
    <script src="../../dist/js/custom.js"></script>
    <script src="../../assets/libs/jquery-steps/build/jquery.steps.min.js"></script>
    <script src="../../assets/libs/jquery-validation/dist/jquery.validate.min.js"></script>

</body>
</html>
''')
