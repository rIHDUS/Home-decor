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
query = f"""UPDATE patient SET firstname = '{fname}', middlename = '{mname}', lastname = '{lname}', mothername = '{momname}', gender = '{gender}', dob = '{dob}',  age = {age}, bld_grp = '{blood_grp}', doct_refference = '{doct_refference}', mobno='{mobno}', email = '{email}', occuption = '{occuption}', relation = '{relation}',password='{password}', country = '{country}', state = '{state}', city = '{city}', area = '{area}', bld_name = '{build_name}', pincode = {pincode} WHERE id = {id}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Patient Record Updated Successfully !!!");
        location.href="patientlist.py";
    </script>''')