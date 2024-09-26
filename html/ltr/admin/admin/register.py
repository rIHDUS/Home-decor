#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

print(f'''
<!DOCTYPE html>
<html dir="ltr">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" type="image/png" sizes="16x16" href="../../assets/images/favicon.png">
    <title>Registration</title>
    <link href="../../dist/css/style.min.css" rel="stylesheet">
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>
    <div class="main-wrapper">
        <div class="preloader">
            <div class="lds-ripple">
                <div class="lds-pos"></div>
                <div class="lds-pos"></div>
            </div>
        </div>
        <div class="auth-wrapper d-flex no-block justify-content-center align-items-center" style="background:url(../../assets/images/big/auth-bg.jpg) no-repeat center center;">
            <div class="auth-box">
                <div>
                    <div class="logo">
                        <br><h2 class="font-medium m-b-20" style="text-align:center;color:#2962ff;"><b>Registration</b></h2>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <form class="form-horizontal m-t-20" method="post" action="registerbackend.py" onsubmit="return validatePasswords()">
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" name="username" id="username" type="text" placeholder="Name" required>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" name="email" id="email" type="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$" placeholder="Email" required>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" name="password" id="id_password" type="password" placeholder="Password" required>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" name="cpassword" id="cpassword" type="password" placeholder="Confirm Password" required>
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <div class="col-md-12">
                                        <div class="">
                                            <center><label class="form-control-label">Password and confirm password must be same.</label><center>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group text-center">
                                    <div class="col-xs-12 p-b-20">
                                        <button class="btn btn-block btn-lg btn-info" type="submit">Register</button>
                                    </div>
                                </div>
                                <div class="form-group m-b-0 m-t-10">
                                    <div class="col-sm-12 text-center">
                                        Already have an account? <a href="login.py" class="text-info m-l-5"><b">Log In</b></a><br>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="../../assets/libs/jquery/dist/jquery.min.js"></script>
    <script src="../../assets/libs/popper.js/dist/umd/popper.min.js"></script>
    <script src="../../assets/libs/bootstrap/dist/js/bootstrap.min.js"></script>
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
</html>
''')
