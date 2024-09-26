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
    <title>Patient Agewise Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* Ensure canvas has full height and width */
        #ageBarChart {
            height: 250px;  /* Increase the height of the chart */
            width: 100%;    /* Adjust width if necessary */
        }
    </style>
</head>
<body>
<h2>Age-wise Distribution of Patients : </h2><br>
<!-- Adjust canvas size for Horizontal Bar Chart -->
<canvas id="ageBarChart"></canvas><br>
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

# Age-wise patient distribution
age_range = range(0, 7)  # Ages 0 to 6
age_counts = {age: sum(1 for x in myresult if x['age'] == age) for age in age_range}

# Define different colors for each age group
age_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF2', '#FFC733', '#A133FF']

# Create the age-wise horizontal bar chart
print(f'''
    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>

    <script>
    // Age-wise Patient Horizontal Bar Chart
    var ctxBar = document.getElementById('ageBarChart').getContext('2d');
    var ageBarChart = new Chart(ctxBar, {{
        type: 'bar',
        data: {{
            labels: ['0', '1', '2', '3', '4', '5', '6'],  // Age groups
            datasets: [{{
                label: 'Number of Patients',
                data: [{age_counts[0]}, {age_counts[1]}, {age_counts[2]}, {age_counts[3]}, {age_counts[4]}, {age_counts[5]}, {age_counts[6]}],
                backgroundColor: {age_colors},  // Use different colors for each bar
                barThickness: 80,  // Control the thickness of each bar
                maxBarThickness: 80  // Maximum thickness for bars
            }}]
        }},
        options: {{
            indexAxis: 'y',  // This makes the bar chart horizontal
            responsive: false,
            maintainAspectRatio: false,
            scales: {{
                x: {{
                    title: {{
                        display: true,
                        text: 'Number of Patients'
                    }},
                    beginAtZero: true
                }},
                y: {{
                    title: {{
                        display: true,
                        text: 'Age Groups'
                    }}
                }}
            }},
            plugins: {{
                title: {{
                    display: true,
                    text: 'Age-wise Distribution of Patients'
                }}
            }}
        }}
    }});
    </script>
</body>
</html>
''')
