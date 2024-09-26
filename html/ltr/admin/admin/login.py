#!C:/Python312/python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
# print(form)

email=form.getvalue('email')
# print(username)
password=form.getvalue('password')
# print(password)
print(f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" type="image/png" sizes="16x16" href="../../assets/images/favicon.png">
        <title>Admin Login</title>
        <link href="../../dist/css/style.min.css" rel="stylesheet">
        <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <div class="main-wrapper">
            <div class="auth-wrapper d-flex no-block justify-content-center align-items-center" style="background:url(../../assets/images/big/auth-bg.jpg) no-repeat center center;">
                <div class="auth-box">
                    <div id="loginform">
                        <div class="logo">
                            <br><h2 class="font-medium m-b-20" style="text-align:center;color:#2962ff"><b>Admin Login</b></h2><br><br>
                        </div>
                        <!-- Form -->
                        <div class="row">
                            <div class="col-12">
                                <form class="form-horizontal m-t-20" id="loginform" method="post" action="loginbackend.py">
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text" id="basic-addon1"><i class="ti-user"></i></span>
                                        </div>
                                        <input type="email" name="username" class="form-control form-control-lg" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" required>
                                    </div>
                                    <div class="input-group mb-3">
                                        <div class="input-group-prepend">
                                            <span class="input-group-text" id="basic-addon2"><i class="ti-pencil"></i></span>
                                        </div>
                                        <input type="password" name="password" id="password" class="form-control form-control-lg" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1" required>
                                    </div>
                                    <div class="form-group row">
                                        <div class="col-md-12"><br>
                                            <div class="custom-control custom-checkbox">
                                                <input type="checkbox" class="custom-control-input" id="customCheck1" onclick="togglePassword()">
                                                <label class="custom-control-label" for="customCheck1">Show Password</label>
                                                <a href="javascript:void(0)" id="to-recover" class="text-dark float-right"><i class="fa fa-lock m-r-5"></i> Forgot pwd?</a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group text-center">
                                        <div class="col-xs-12 p-b-20">
                                            <button class="btn btn-block btn-lg btn-info" type="submit" >Log In</button>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col-xs-12 col-sm-12 col-md-12 m-t-10 text-center">
                                            <div class="social">
                                                <a href="javascript:void(0)" class="btn btn-facebook" data-toggle="tooltip" title="" data-original-title="Login with Facebook"> <i aria-hidden="true" class="fab  fa-facebook"></i> </a>
                                                <a href="javascript:void(0)" class="btn btn-googleplus" data-toggle="tooltip" title="" data-original-title="Login with Google"> <i aria-hidden="true" class="fab  fa-google-plus"></i> </a>
                                                <a href="javascript:void(0)" class="btn btn-success" data-toggle="tooltip" title="" data-original-title="Login with WhatsApp"> <i aria-hidden="true" class="fab  fa-whatsapp"></i> </a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="form-group m-b-0 m-t-10">
                                        <div class="col-sm-12 text-center"><br>
                                            Don't have an account? <a href="register.py" class="text-info m-l-5"><b">Sign Up</b></a>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div id="recoverform">
                        <div class="logo">
                            <br><h2 class="font-medium m-b-20" style="text-align:center;center;color:royalblue;"><b>Recover Password</b></h2><br>
                            <span>Enter your Email and instructions will be sent to you!</span>
                        </div>
                        <div class="row">
                        <div class="col-12">
                            <form class="form-horizontal m-t-20" action="login.py">
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" type="text" required="" placeholder="Name">
                                    </div>
                                </div>
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" type="text" required="" placeholder="Email">
                                    </div>
                                </div>
                                <div class="form-group text-center">
                                    <div class="col-xs-12 p-b-20">
                                        <button class="btn btn-block btn-lg btn-info" type="submit">RESET</button>
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

            // Function to toggle the password visibility
            function togglePassword() {{
                var passwordField = document.getElementById("password");
                if (passwordField.type === "password") {{
                    passwordField.type = "text";
                }} else {{
                    passwordField.type = "password";
                }}
            }}
        </script>
    </body>
    </html>
''')