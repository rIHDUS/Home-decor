#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
id=form.getvalue('id')
#print(id)

fname = form.getvalue('fname')
mname = form.getvalue('mname')
lname = form.getvalue('lname')
mobno = form.getvalue('mobno')
altmobno = form.getvalue('altmobno')
email = form.getvalue('email')
aadhar = form.getvalue('aadhar')
dob = form.getvalue('dob')
pan = form.getvalue('pan')
gender = form.getvalue('gender')
maritual_status = form.getvalue('mar_status')
institute_name = form.getvalue('institute_name')
institute_city = form.getvalue('institute_city')
university = form.getvalue('university')
course = form.getvalue('course')
passing_year = form.getvalue('passing_year')
percentage = form.getvalue('percentage')
designation = form.getvalue('designation')
experience = form.getvalue('experience')
join_date = form.getvalue('join_date')
password = form.getvalue('password')
country = form.getvalue('country')
state = form.getvalue('states')
city = form.getvalue('city')
area = form.getvalue('area')
build_name = form.getvalue('bld_name')
pincode = form.getvalue('pincode')
bankname = form.getvalue('bnk_name')
branch = form.getvalue('branch')
accounttype = form.getvalue('acc_type')
accountno = form.getvalue('acc_no')
ifsc_code = form.getvalue('ifsc_code')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE employee SET firstname = '{fname}', middlename = '{mname}', lastname = '{lname}', mobno = '{mobno}', alt_mobno = '{altmobno}', email = '{email}', aadhar = '{aadhar}', dob = '{dob}', pan_no = '{pan}', gender = '{gender}', maritual_status = '{maritual_status}', institute_name = '{institute_name}', institute_city = '{institute_city}', university = '{university}', course = '{course}', passing_year = '{passing_year}', percentage = '{percentage}', designation = '{designation}', work_exp = '{experience}', joindate = '{join_date}', password = '{password}', country = '{country}', state = '{state}', city = '{city}', area = '{area}', bld_name = '{build_name}', pincode = '{pincode}', bnk_name = '{bankname}', bnk_branch = '{branch}', acc_type = '{accounttype}', acc_no = '{accountno}', ifs_code = '{ifsc_code}' WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Employee Record Updated Successfully !!!");
        location.href="employeelist.py";
    </script>''')