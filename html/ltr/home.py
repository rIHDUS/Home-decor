#!C:\Python312\python.exe
import user_header

print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Audiology Assessment Portal</title>
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
        .hero-section {
            background-image: url('https://via.placeholder.com/1920x600?text=Welcome+to+Audiology+Assessment+Portal');
            background-size: cover;
            background-position: center;
            color: #fff;
            padding: 100px 0;
        }
        .hero-section .hero-content {
            text-align: center;
        }
        .hero-section .hero-content h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        .hero-section .hero-content p {
            font-size: 1.2em;
        }
        .features-section {
            padding: 60px 0;
        }
        .feature-box {
            text-align: center;
            margin-bottom: 30px;
        }
        .feature-box img {
            max-width: 100px;
            margin-bottom: 20px;
        }
        .feature-box h3 {
            font-size: 1.5em;
            margin-bottom: 10px;
        }
        .feature-box p {
            font-size: 1em;
        }
        .testimonial-section {
            background-color: #f8f9fa;
            padding: 60px 0;
        }
        .testimonial-slider {
            text-align: center;
        }
        .testimonial-slider .testimonial-item {
            padding: 20px;
            background: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .testimonial-slider .testimonial-item p {
            font-size: 1.1em;
            margin-bottom: 20px;
        }
        .testimonial-slider .testimonial-item h4 {
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>

<section class="page-title bg-1">
    <div class="overlay"></div>
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="block text-center">
                    <span class="text-white">Providing early and accurate hearing assessments for children aged 0-6</span>
                    <h1 class="text-capitalize mb-5 text-lg">Welcome to the Audiology Assessment Portal</h1>
                     <a href="abouot.py" class="btn btn-main btn-round-full">Learn More</a>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="features-section">
    <div class="container">
        <div class="row">
            <div class="col-lg-4 col-md-6 feature-box">
                <img src="https://via.placeholder.com/100x100?text=Comprehensive" alt="Comprehensive Testing">
                <h3>Comprehensive Testing</h3>
                <p>Detailed assessments to ensure accurate results for your child's hearing health.</p>
            </div>
            <div class="col-lg-4 col-md-6 feature-box">
                <img src="https://via.placeholder.com/100x100?text=User+Friendly" alt="User Friendly">
                <h3>User Friendly</h3>
                <p>Easy-to-use interface for parents to book appointments and track results effortlessly.</p>
            </div>
            <div class="col-lg-4 col-md-6 feature-box">
                <img src="https://via.placeholder.com/100x100?text=Expert+Guidance" alt="Expert Guidance">
                <h3>Expert Guidance</h3>
                <p>Access to experienced audiologists who provide valuable insights and support.</p>
            </div>
        </div>
    </div>
</section>

<section class="testimonial-section">
    <div class="container">
        <h2 class="text-center mb-4">What Parents Say</h2>
        <div class="testimonial-slider">
            <div class="testimonial-item">
                <p>"The assessment process was smooth and the results were clear. The staff were very supportive throughout."</p>
                <h4>- Jane Doe</h4>
            </div>
            <div class="testimonial-item">
                <p>"We appreciate the comprehensive tests and the ease of booking an appointment. Highly recommended!"</p>
                <h4>- John Smith</h4>
            </div>
            <!-- Add more testimonials as needed -->
        </div>
    </div>
</section>

<!-- Include necessary scripts -->
<script src="plugins/jquery/jquery.min.js"></script>
<script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="plugins/slick-carousel/slick/slick.min.js"></script>
<script src="js/main.js"></script>

<script>
    $(document).ready(function(){
        $('.testimonial-slider').slick({
            infinite: true,
            dots: true,
            arrows: false,
            autoplay: true,
            autoplaySpeed: 3000
        });
    });
</script>

</body>
</html>
''')
import user_footer
