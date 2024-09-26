#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
form = cgi.FieldStorage()

# Retrieve form data and check for None values
def get_value(field):
    return form.getvalue(field) if form.getvalue(field) else ''

fname = get_value('fname')
mname = get_value('mname')
lname = get_value('lname')
mobno = get_value('mobno')

email = get_value('email')
aadhar = get_value('aadhar')
dob = get_value('dob')

gender = get_value('gender')

institute_name = get_value('institute_name')

university = get_value('university')
course = get_value('course')
passing_year = get_value('passing_year')
percentage = get_value('percentage')
designation = get_value('designation')
experience = get_value('experience')
join_date = get_value('join_date')
password = get_value('password')
country = get_value('country')
state = get_value('states')
city = get_value('city')
area = get_value('area')
build_name = get_value('bld_name')
pincode = get_value('pincode')
bankname = get_value('bnk_name')
branch = get_value('branch')

accountno = get_value('acc_no')
ifsc_code = get_value('ifsc_code')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor = mydb.cursor()

query = """INSERT INTO employee (firstname, middlename, lastname, mobno,  email, aadhar, dob,  gender,  institute_name,  university, course, passing_year, percentage, designation, work_exp, joindate, password, country, state, city, area, bld_name, pincode, bnk_name, bnk_branch,  acc_no, ifsc_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

values = (fname, mname, lname, mobno, email, aadhar, dob, gender,  institute_name,  university, course, passing_year, percentage, designation, experience, join_date, password, country, state, city, area, build_name, pincode, bankname, branch,  accountno, ifsc_code)

mycursor.execute(query, values)
mydb.commit()

print('''
<script>
    alert("Registered a new employee.!!");
    location.href="employeelist.py";
</script>
''')
