#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()

# HTML Header and CSS/JS includes
print("Content-type: text/html\n")
print('''<!DOCTYPE html>
<html>
<head>
    <title>Patient Details Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
<h2>Gender of patients : </h2><br>
<!-- Adjust canvas size -->
<canvas id="genderChart" style="max-width: 300px; max-height: 300px;"></canvas><br>
''')

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

# Query to fetch patient data
query = "SELECT * FROM patient"
mycursor = mydb.cursor(dictionary=True)
mycursor.execute(query)
myresult = mycursor.fetchall()

# Calculate gender distribution
male_count = sum(1 for x in myresult if x['gender'] == 'Male')
female_count = sum(1 for x in myresult if x['gender'] == 'Female')

# Calculate total and percentages
total_count = male_count + female_count
male_percentage = (male_count / total_count) * 100 if total_count > 0 else 0
female_percentage = (female_count / total_count) * 100 if total_count > 0 else 0

# Display percentages in HTML after the chart
print(f'''
    <h3>Male : {male_count} ({male_percentage:.2f}%)</h3>
    <h3>Female : {female_count} ({female_percentage:.2f}%)</h3>

    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>

    <script>
    var ctx = document.getElementById('genderChart').getContext('2d');
    var genderChart = new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: ['Male', 'Female'],
                datasets: [{{
                    label: 'Gender Distribution',
                    data: [{male_count}, {female_count}],
                    backgroundColor: ['#36A2EB', '#FF6384'],
                }}]
            }},
            options: {{
                responsive: false,
                maintainAspectRatio: false,  // Ensures custom canvas size is respected
                width: 200,  // Set width and height explicitly if needed
                height: 200
            }}
        }});
    </script>
</body>
</html>
''')
