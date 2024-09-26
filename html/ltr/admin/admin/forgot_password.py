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
    <title>Forgot Password</title>
    <link href="../../dist/css/style.min.css" rel="stylesheet">
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    <style>
        .password-fields {{
            display: none;
        }}
    </style>
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
                        <br><h2 class="font-medium m-b-20" style="text-align:center;color:#2962ff;"><b>Forgot Password</b></h2>
                    </div>
                    <div class="row">
                        <div class="col-12">
                            <form class="form-horizontal m-t-20" id="forgotPasswordForm" method="post">
                                <div class="form-group row">
                                    <div class="col-12">
                                        <input class="form-control form-control-lg" name="email" id="email" type="email" placeholder="Enter your email" required>
                                    </div>
                                </div>
                                <div class="password-fields" id="password-fields">
                                    <div class="form-group row">
                                        <div class="col-12">
                                            <input class="form-control form-control-lg" name="new_password" id="new_password" type="password" placeholder="New Password" required>
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <div class="col-12">
                                            <input class="form-control form-control-lg" name="confirm_new_password" id="confirm_new_password" type="password" placeholder="Confirm New Password" required>
                                        </div>
                                    </div>
                                    <div class="form-group row">
                                        <div class="col-md-12">
                                            <div class="">
                                                <center><label class="form-control-label" id="password-message"></label></center>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group text-center">
                                    <div class="col-xs-12 p-b-20">
                                        <button class="btn btn-block btn-lg btn-info" type="submit">Reset Password</button>
                                    </div>
                                </div>
                                <div class="form-group m-b-0 m-t-10">
                                    <div class="col-sm-12 text-center">
                                        Remember your password? <a href="login.py" class="text-info m-l-5"><b>Log In</b></a><br>
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
        $(document).ready(function() {{
            $("#forgotPasswordForm").on("submit", function(e) {{
                e.preventDefault();
                $.ajax({{
                    type: "POST",
                    url: "forgot_passwordbackend.py",
                    data: $(this).serialize(),
                    success: function(response) {{
                        if (response.trim() === "Email exists") {{
                            $("#password-fields").show();
                            $("#password-message").text("");
                        }} else if (response.trim() === "Email not found") {{
                            alert("Email not found.");
                        }} else if (response.trim() === "Password updated") {{
                            alert("Password updated successfully.");
                            window.location.href = "login.py";
                        }} else {{
                            $("#password-message").text(response);
                        }}
                    }},
                    error: function() {{
                        alert("An error occurred.");
                    }}
                }});
            }});
        }});
        $(".preloader").fadeOut();
    </script>
</body>
</html>
''')
