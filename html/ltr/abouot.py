#!C:\Python312\python.exe
import user_header
print('''
<script>
    // Retrieve the username from localStorage
    var username = localStorage.getItem("User_Name");

    // If the username is not set or empty, prompt the user to log in
    
        // Get the first letter of the username
        var initialLetter = username.charAt(0).toUpperCase(); // Get first letter and capitalize

        // Create a new 'li' element for the new button
        var newNavItem = document.createElement("li");
        newNavItem.className = "nav-item";
        newNavItem.style.cssText = "margin-right:10px";  // Remove background from 'li', moved to 'a'

        // Create the 'a' element for the new button
        var newNavLink = document.createElement("a");
        newNavLink.className = "nav-link";
        newNavLink.href = "profile.py";  // Set this to the user's profile or dashboard page
        newNavLink.textContent = initialLetter;  // Display the initial letter of the username

        // Style the new button to make it a circle
        newNavLink.style.cssText = "background-color: rgb(34, 139, 34); color:white; text-align:center; display:flex; justify-content:center; align-items:center; width:50px; height:50px; border-radius:50%; font-size:20px;";

        // Append the 'a' element to the new 'li' element
        newNavItem.appendChild(newNavLink);

        // Find the parent element where you want to add this new button (e.g., the navigation bar)
        var navBar = document.getElementById("loginRegister").parentNode;

        // Remove the original "Login/Register" button
        var loginRegisterElement = document.getElementById("loginRegister");
        if (loginRegisterElement) {
            navBar.removeChild(loginRegisterElement);
        }

        // Append the new button to the navigation bar
        navBar.appendChild(newNavItem);
    
</script>''')
print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - Audiology Assessment Portal</title>
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
                    <span class="text-white">Learn More About Us</span>
                    <h1 class="text-capitalize mb-5 text-lg">About the Audiology Assessment Portal</h1>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="about section">
    <div class="container">
        <div class="row">
            <div class="col-lg-8 offset-lg-2">
                <div class="about-wrap mt-5">
                    <h2 class="mb-4 title-color">Welcome to the Audiology Assessment Portal</h2>
                    <p class="mb-4">Our Audiology Assessment Portal is dedicated to providing comprehensive and accurate hearing assessments for children aged 0-6. Early detection of hearing issues is crucial for ensuring proper development and addressing potential hearing impairments before they impact a child's growth and communication skills.</p>
                    
                    <div class="mb-4">
                        <img src="https://via.placeholder.com/800x400?text=Early+Hearing+Assessment" alt="Early Hearing Assessment" class="img-fluid">
                    </div>
                    
                    <h3 class="mb-3">Why Early Hearing Assessment?</h3>
                    <p class="mb-4">Hearing plays a vital role in a child's overall development, including their ability to speak, understand language, and interact socially. Identifying and treating hearing issues early can significantly improve a child's quality of life and developmental outcomes. Our portal offers a range of specialized tests and assessments tailored for young children, ensuring that their hearing health is monitored and managed effectively.</p>
                    
                    <div class="mb-4">
                        <img src="https://via.placeholder.com/800x400?text=Importance+of+Early+Hearing+Tests" alt="Importance of Early Hearing Tests" class="img-fluid">
                    </div>
                    
                    <h3 class="mb-3">Features of Our Portal</h3>
                    <ul class="mb-4">
                        <li>Comprehensive Hearing Tests: Designed specifically for children to accurately assess their hearing abilities.</li>
                        <li>User-Friendly Interface: Easy navigation for parents and guardians to book appointments and access results.</li>
                        <li>Expert Guidance: Access to audiologists and specialists who provide expert advice and support.</li>
                        <li>Confidential and Secure: Ensuring the privacy and security of your child's health information.</li>
                    </ul>
                    
                    <div class="mb-4">
                        <img src="https://via.placeholder.com/800x400?text=Features+of+Our+Portal" alt="Features of Our Portal" class="img-fluid">
                    </div>
                    
                    <h3 class="mb-3">How It Works</h3>
                    <p class="mb-4">Booking an appointment is simple and convenient. Parents can select a suitable time and date for their child's assessment through our online portal. Once the appointment is confirmed, our team will guide you through the assessment process and provide detailed results and recommendations.</p>
                    
                    <div class="mb-4">
                        <img src="https://via.placeholder.com/800x400?text=How+It+Works" alt="How It Works" class="img-fluid">
                    </div>

                    <h3 class="mb-3">Contact Us</h3>
                    <p class="mb-4">If you have any questions or need assistance, please feel free to contact us. Our dedicated team is here to help and ensure that your child's hearing health is taken care of.</p>
                </div>
            </div>
        </div>
    </div>
</section>

</body>
</html>
''')
import user_footer
