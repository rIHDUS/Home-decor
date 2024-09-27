#!C:\Python312\python.exe
import cgi
import cgitb

# Enable CGI traceback for debugging
cgitb.enable()

# Set the content type for the response
print("Content-Type: text/html\n")


# HTML template for the homepage
home_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="description" content="Orbitor, business, company, agency, modern, bootstrap4, tech, software">
    <meta name="author" content="themefisher.com">
    <title>Audiology Assessment Portal</title>

    <!-- Favicon -->
    <link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico" />

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="plugins/bootstrap/css/bootstrap.min.css">
    <!-- Icon Font CSS -->
    <link rel="stylesheet" href="plugins/icofont/icofont.min.css">
    <!-- Slick Slider CSS -->
    <link rel="stylesheet" href="plugins/slick-carousel/slick/slick.css">
    <link rel="stylesheet" href="plugins/slick-carousel/slick/slick-theme.css">

    <!-- Main Stylesheet -->
    <link rel="stylesheet" href="css/style.css">
    <style>
        label {
            color: black;
        }
    </style>
</head>

<body id="top">

<!-- Header Section -->
<header>
    
    <nav class="navbar navbar-expand-lg navigation" id="navbar" style="background-color:silver;">
        <div class="container">
            <a class="navbar-brand" href="index.html">
                <h1>ADAP</h1>
            </a>
            <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#navbarmain" aria-controls="navbarmain" aria-expanded="false" aria-label="Toggle navigation">
                <span class="icofont-navigation-menu"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarmain">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="home.py">Home</a>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="abouot.py">About</a></li>
                    <!--<li class="nav-item"><a class="nav-link" href="service.py">Services</a></li>-->
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="doctor.html" id="dropdown03" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Doctor <i class="icofont-thin-down"></i></a>
                        <ul class="dropdown-menu" aria-labelledby="dropdown03">
                            <li><a class="dropdown-item" href="doctor.py">Doctors</a></li>
                            <li><a class="dropdown-item" href="appointment.py">Appointment</a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a class="nav-link" href="questions.py">Test</a></li>
                    <li class="nav-item" id="loginRegister" style="background-color: rgb(223, 45, 45); color:white; border-radius:50px; margin-right:10px">
    <a class="nav-link" href="" data-toggle="modal" aria-pressed="false" data-target="#exampleModal">Login/Register</a>
</li>
                </ul>
            </div>
        </div>
    </nav>
</header>

<!-- Login Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Login</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="user_loginbackend.py" method="post">
                    <div class="form-group">
                        <label for="user_name" class="col-form-label">Username</label>
                        <input type="text" class="form-control" placeholder="Email" name="user_name" id="user_name" required="">
                    </div>
                    <div class="form-group">
                        <label for="user_psw" class="col-form-label">Password</label>
                        <input type="password" class="form-control" placeholder="Password" name="user_psw" id="user_psw" required="">
                    </div>
                    <div class="right-w3l">
                        <input type="submit" class="form-control serv_bottom" style="background-color: rgb(223, 45, 45); color:white;" value="Login">
                    </div>
                    <div class="row sub-w3l my-3">
                        <div class="col sub-agile">
                            <input type="checkbox" id="brand1" value="">
                            <label for="brand1" class="text-secondary">
                                <span></span>Remember me?
                            </label>
                        </div>
                        <div class="col forgot-w3l text-right">
                            <a href="#" class="text-secondary">Forgot Password?</a>
                        </div>
                    </div>
                    <p class="text-center text-secondary">Don't have an account?
                        <a href="#" data-toggle="modal" data-target="#exampleModal1" class="text-dark font-weight-bold">Register Now</a>
                    </p>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- Register Modal -->
<div class="modal fade" id="exampleModal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel1" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel1">Register</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form action="user_registerbackend.py" method="post">
                    <div class="form-group">
                        <label for="name" class="col-form-label">Name</label>
                        <input type="text" class="form-control" name="name" id="name" required="">
                    </div>
                    <div class="form-group">
                        <label for="email" class="col-form-label">Email</label>
                        <input type="email" class="form-control" name="email" id="email" required="">
                    </div>
                    <div class="form-group">
                        <label for="password" class="col-form-label">Password</label>
                        <input type="password" class="form-control" name="password" id="password" required="">
                    </div>
                    <div class="form-group">
                        <label for="cpassword" class="col-form-label">Confirm Password</label>
                        <input type="password" class="form-control" name="cpassword" id="cpassword" required="">
                    </div>
                    <div class="sub-w3l">
                        <div class="sub-agile">
                            <input type="checkbox" id="brand2" value="">
                            <label for="brand2" class="mb-3">
                                <span></span>I Accept the Terms & Conditions
                            </label>
                        </div>
                    </div>
                    <div class="right-w3l">
                        <input type="submit" class="form-control serv_bottom" style="background-color: rgb(223, 45, 45); color:white;" value="Register">
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>

<!-- JavaScript Files -->
<script src="js/jquery-2.2.3.min.js"></script>
<script src="js/owl.carousel.js"></script>
<script src="js/jquery.magnific-popup.js"></script>
<script src="js/scrolling-nav.js"></script>
<script src="js/counter.js"></script>
<script src="js/script.js"></script>
<script src="plugins/bootstrap/js/bootstrap.min.js"></script>

</body>
</html>
"""

# Output the HTML content
print(home_html)
