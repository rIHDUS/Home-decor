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
    <title>Employee Report</title>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/buttons/2.3.2/css/buttons.dataTables.min.css">
</head>
<body>
    <h1>
        <hr>
        <center>Employee Report</center>
        <hr>
    </h1>
    <table id="example" class="display" style="width:100%">
        <thead>
                                    <tr style="background-color:powderblue;">
                                           
                                           <th scope="col">Sr.No</th>
                                           <th scope="col">First</th>
                                           <th scope="col">Middle</th>
                                           <th scope="col">Last</th>
                                           <th scope="col">Contact</th>
                                          
                                           <th scope="col">Email</th>
                                        
                                           <th scope="col">DOB</th>
                                          
                                           <th scope="col">M/F</th>
                                         
                                           <th scope="col">Designation</th>
                                           <th scope="col">Experience</th>
                                           
                                           
                                           <th scope="col">Pincode</th>
                                           <th scope="col">Bank</th>
                                           <th scope="col">Branch</th>
                                          
                                           <th scope="col">Acc No.</th>
                                           <th scope="col">IFSC Code</th>
                                        </tr>
                                </thead><tbody>
''')

form = cgi.FieldStorage()

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor(dictionary=True)

# Constants
RECORDS_PER_PAGE = 10

# Get the current page number, search query, and sort option from the form data
current_page = int(form.getvalue('page', 1))
search_query = form.getvalue('search', '')
sort_option = form.getvalue('sort', 'id_asc')  # Default sort option

# SQL query for fetching employees with search functionality
query = """
SELECT id, firstname, middlename, lastname, mobno,  email, dob, gender, 
designation, work_exp, city, pincode, 
bnk_name, bnk_branch,  acc_no, ifsc_code
FROM employee
"""

if search_query:
    query += (f" WHERE firstname LIKE '%{search_query}%' OR middlename LIKE '%{search_query}%' OR "
              f"lastname LIKE '%{search_query}%' OR mobno LIKE '%{search_query}%'  OR "
              f"email LIKE '%{search_query}%'  OR dob LIKE '%{search_query}%' OR "
              f"gender LIKE '%{search_query}%' OR  "
              f"designation LIKE '%{search_query}%' OR "
              f"joindate LIKE '%{search_query}%' OR country LIKE '%{search_query}%' OR state LIKE '%{search_query}%' OR "
              f"city LIKE '%{search_query}%' OR area LIKE '%{search_query}%' OR bld_name LIKE '%{search_query}%' OR "
              f"pincode LIKE '%{search_query}%' OR bnk_name LIKE '%{search_query}%' OR bnk_branch LIKE '%{search_query}%' OR "
              f"acc_type LIKE '%{search_query}%' OR acc_no LIKE '%{search_query}%' OR ifsc_code LIKE '%{search_query}%'")

# Apply sorting based on the selected option
if sort_option == 'id_desc':
    query += " ORDER BY id DESC"
elif sort_option == 'name_asc':
    query += " ORDER BY lastname ASC, firstname ASC"
elif sort_option == 'name_desc':
    query += " ORDER BY lastname DESC, firstname DESC"
else:
    query += " ORDER BY id ASC"

# Get total number of records
mycursor.execute(query)
total_records = len(mycursor.fetchall())

# Calculate the starting point for the current page
start = (current_page - 1) * RECORDS_PER_PAGE

# Fetch only the required records for the current page
query += f" LIMIT {start}, {RECORDS_PER_PAGE}"
mycursor.execute(query)
myresult = mycursor.fetchall()

# Generate table rows
tr_html = ''
for x in myresult:
    tr_html += f'''
         <tr>
            <td>{x['id']}</td>
            <td>{x['firstname']}</td>
            <td>{x['middlename']}</td>
            <td>{x['lastname']}</td>
            <td>{x['mobno']}</td>
           
            <td>{x['email']}</td>
            
            <td>{x['dob']}</td>
           
            <td>{x['gender']}</td>
           
            
            <td>{x['designation']}</td>
            <td>{x['work_exp']}</td>
            
            <td>{x['city']}</td>
           
            <td>{x['pincode']}</td>
            <td>{x['bnk_name']}</td>
            <td>{x['bnk_branch']}</td>
          
            <td>{x['acc_no']}</td>
            <td>{x['ifsc_code']}</td>
        
    '''

# Pagination controls
total_pages = (total_records + RECORDS_PER_PAGE - 1) // RECORDS_PER_PAGE
pagination_html = ''
if current_page > 1:
    pagination_html += f'<a href="?page={current_page-1}&search={search_query}&sort={sort_option}"><button class="btn btn-primary" style="background-color:#2962ff">Previous</button></a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
if current_page < total_pages:
    pagination_html += f'<a href="?page={current_page+1}&search={search_query}&sort={sort_option}"><button class="btn btn-primary" style="background-color:#2962ff">Next</button></a>'

# Search form and table display
print(f'''
        {tr_html}
        </tbody>
    </table>
   <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/buttons/2.3.2/js/dataTables.buttons.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
    <script src="https://cdn.datatables.net/buttons/2.3.2/js/buttons.html5.min.js"></script>
    <script>
        $(document).ready(function() {{
            $('#example').DataTable({{
                dom: 'Bfrtip',
                buttons: [
                    'copyHtml5',
                    'excelHtml5',
                    'csvHtml5',
                    'pdfHtml5'
                ]
            }});
        }});
    </script>
    <footer class="footer text-center">All Rights Reserved by <a href="https://wolfox.in">Wolfox Services Pvt.Ltd.</a></footer>
</body>
</html>
''')
