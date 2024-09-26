#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()

# Output the content type for the response

# Footer HTML
footer_html = """
<!-- Footer Start -->
<footer class="footer section" style="background-color:silver;">
    <div class="container">
        <div class="row">
            <!-- About Section -->
            <div class="col-lg-4 mr-auto col-sm-6">
                <div class="widget mb-5 mb-lg-0">
                    <div class="logo mb-4">
                        <h1>ADAP</h1>
                    </div>
                    <p>Your trusted partner for making informed decisions in audiology. Our mission is to ensure clarity and precision in every assessment.</p>
                    <ul class="list-inline footer-socials mt-4">
                        <li class="list-inline-item"><a href="https://www.facebook.com/" aria-label="Facebook"><i class="icofont-facebook"></i></a></li>
                        <li class="list-inline-item"><a href="https://twitter.com/" aria-label="Twitter"><i class="icofont-twitter"></i></a></li>
                        <li class="list-inline-item"><a href="https://www.linkedin.com/" aria-label="LinkedIn"><i class="icofont-linkedin"></i></a></li>
                    </ul>
                </div>
            </div>

            <!-- Support Section -->
            <div class="col-lg-4 col-md-6 col-sm-6">
                <div class="widget mb-5 mb-lg-0">
                    <h4 class="text-capitalize mb-3">Pages</h4>
                    <div class="divider mb-4"></div>
                    <ul class="list-unstyled footer-menu lh-35">
                        <li><a href="home.py">Home</a></li>
                        <li><a href="abouot">About</a></li>
                        <li><a href="#">Doctors</a></li>
                        <li><a href="appointment.py">Appointment</a></li>
                        <li><a href="" data-toggle="modal" aria-pressed="false" data-target="#exampleModal">Sign in / Sign up</a></li>
                    </ul>
                </div>
            </div>

            <!-- Contact Section -->
            <div class="col-lg-3 col-md-6 col-sm-6">
                <div class="widget widget-contact mb-5 mb-lg-0">
                    <h4 class="text-capitalize mb-3">Get in Touch</h4>
                    <div class="divider mb-4"></div>
                    <div class="footer-contact-block mb-4">
                        <div class="icon d-flex align-items-center">
                            <i class="icofont-email mr-3"></i>
                            <span class="h6 mb-0">24/7 Support Available</span>
                        </div>
                        <h4 class="mt-2"><a href="mailto:support@email.com">support@email.com</a></h4>
                    </div>
                    <div class="footer-contact-block">
                        <div class="icon d-flex align-items-center">
                            <i class="icofont-support mr-3"></i>
                            <span class="h6 mb-0">Mon to Fri: 08:30 - 18:00</span>
                        </div>
                        <h4 class="mt-2"><a href="tel:+2345678890">+23-456-6588</a></h4>
                    </div>
                </div>
            </div>
        </div>

        <!-- Footer Bottom -->
        <div class="footer-btm py-4 mt-5">
            <div class="row align-items-center justify-content-between">
                <div class="col-lg-6">
                    <div class="copyright">
                        &copy; 2024 <span class="text-color">ADAP</span>. All Rights Reserved. Design by <a href="https://wolfox.in" target="_blank">Wolfox Services Pvt. Ltd.</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="subscribe-form text-lg-right mt-5 mt-lg-0">
                        <form action="http://localhost/hds/html/ltr/admin/admin/login.py" class="subscribe">
                            <input type="email" class="form-control" placeholder="Are you an Admin" readonly>
                            <button type="submit" class="btn btn-main-2 btn-round-full">Login As Admin</button>
                        </form>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-4">
                    <a class="backtop js-scroll-trigger" href="#top" aria-label="Back to Top">
                        <i class="icofont-long-arrow-up"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>
</footer>

<!-- Essential Scripts -->
<script src="plugins/jquery/jquery.js"></script>
<script src="plugins/bootstrap/js/popper.js"></script>
<script src="plugins/bootstrap/js/bootstrap.min.js"></script>
<script src="plugins/counterup/jquery.easing.js"></script>
<script src="plugins/slick-carousel/slick/slick.min.js"></script>
<script src="plugins/counterup/jquery.waypoints.min.js"></script>
<script src="plugins/counterup/jquery.counterup.min.js"></script>
<script src="plugins/shuffle/shuffle.min.js"></script>
<script src="plugins/google-map/map.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAkeLMlsiwzp6b3Gnaxd86lvakimwGA6UA&callback=initMap"></script>
<script src="js/script.js"></script>
<script src="js/contact.js"></script>
</body>
</html>
"""

# Output the HTML content
print(footer_html)
