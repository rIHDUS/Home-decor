#!C:\Python312\python.exe
import user_header
print('''
      <script>
       var username = localStorage.getItem("User_Name");
       if (username === null || username === "") {
           alert("Login first");
           window.location.href = "home.py";
       }
      </script>''')

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Your Appointment</title>
    <!-- Add your CSS files here -->
    <link rel="stylesheet" href="path/to/your/styles.css">
</head>
<body>

<section class="page-title bg-1">
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="block text-center">
                    <span class="text-white">Book Your Seat</span>
                    <h1 class="text-capitalize mb-5 text-lg">Appointment</h1>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="appointment section">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 offset-lg-2">
                <div class="appointment-wrap mt-5">
                    <h2 class="mb-4 title-color">Make an Appointment</h2>
                    <p class="mb-4">Make an appointmnent for furthur assessment.</p>
<form id="appointment-form" class="appointment-form" method="post" action="appointmentbackend.py">
    <div class="row">
        <div class="col-lg-6">
            <div class="form-group">
                <input name="first_name" id="first_name" type="text" class="form-control" placeholder="First Name" required pattern="[A-Za-z ]{1,}">
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="middle_name" id="middle_name" type="text" class="form-control" placeholder="Middle Name" pattern="[A-Za-z ]*">
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="last_name" id="last_name" type="text" class="form-control" placeholder="Last Name" required pattern="[A-Za-z ]{1,}">
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="mother_name" id="mother_name" type="text" class="form-control" placeholder="Mother's Name" required pattern="[A-Za-z ]{1,}">
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="appointment_date" id="appointment_date" type="date" class="form-control" placeholder="Appointment Date" required>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="appointment_time" id="appointment_time" type="time" class="form-control" placeholder="Appointment Time" required>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="age" id="age" type="number" min="0" max="6" class="form-control" placeholder="Age" required>
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="phone" id="phone" type="tel" class="form-control" placeholder="Phone Number" required pattern="[0-9]{12}">
            </div>
        </div>
        <div class="col-lg-6">
            <div class="form-group">
                <input name="email" id="email" type="email" class="form-control" placeholder="Email" required>
            </div>
        </div>
        <!-- New Test Score Field -->
        <div class="col-lg-6">
            <div class="form-group">
                <input name="test_score" id="test_score" type="number" min="0" max="100" class="form-control" placeholder="Test Score" required>
            </div>
        </div>
    </div>
    <div class="form-group mb-4">
        <textarea name="message" id="message" class="form-control" rows="6" placeholder="Your Message"></textarea>
    </div>
    <button type="submit" class="btn btn-main btn-round-full">Make an Appointment<i class="icofont-simple-right ml-2"></i></button>
</form>

                </div>
            </div>
        </div>
    </div>
</section>




</body>
</html>
''')
import user_footer