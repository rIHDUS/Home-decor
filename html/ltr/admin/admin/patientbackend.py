#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

fname = form.getvalue('fname')
mname = form.getvalue('mname')
lname = form.getvalue('lname')
momname = form.getvalue('momname')
gender = form.getvalue('gender')
dob = form.getvalue('dob')
age = form.getvalue('age')
blood_grp = form.getvalue('bloodgroup')
doct_refference = form.getvalue('refference')
mobno = form.getvalue('mobno')
email = form.getvalue('email')
occuption = form.getvalue('occuption')
relation = form.getvalue('relation')
password = form.getvalue('password')
country = form.getvalue('country')
state = form.getvalue('states')
city = form.getvalue('city')
area = form.getvalue('area')
build_name = form.getvalue('bld_name')
pincode = form.getvalue('pincode')

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)

mycursor=mydb.cursor(dictionary=True)

query=f"""INSERT INTO patient (firstname,middlename,lastname,mothername,gender,dob,age,bld_grp,doct_refference,mobno,email,occuption,relation,country,state,city,area,bld_name,pincode) VALUES ('{fname}','{mname}','{lname}','{mname}','{gender}','{dob}',{age},'{blood_grp}','{doct_refference}','{mobno}','{email}','{occuption}','{relation}','{country}','{state}','{city}','{area}','{build_name}','{pincode}')"""
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Patient Register Successfully !!!");
    location.href="dashboard.py";
</script>''')