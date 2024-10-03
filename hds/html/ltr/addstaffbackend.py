#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()

#Personal Details
Firstname=form.getvalue("Firstname")
Middlename=form.getvalue("Middlename")
Lastname=form.getvalue("Lastname")
Phone=form.getvalue("Phone")
Gender=form.getvalue("Gender")
Address=form.getvalue("Address")
Maritalstatus=form.getvalue("Maritalstatus")
Bloodgroup=form.getvalue("Bloodgroup")
Dob=form.getvalue("Dob")
Adhar=form.getvalue("Adhar")
Pan=form.getvalue("Pan")
Passport=form.getvalue("Passport")

#Contact Details
Mobile=form.getvalue("Mobile")
Email=form.getvalue("Email")
Mobile2=form.getvalue("Mobile2")
Email2=form.getvalue("Email2")
Country=form.getvalue("Country")
State=form.getvalue("State")
City=form.getvalue("City")
Pincode=form.getvalue("Pincode")
Address2=form.getvalue("Address2")
Education=form.getvalue("Education")
Specilisation=form.getvalue("Specilisation")
Institute=form.getvalue("Institute")
Percentage=form.getvalue("Percentage")
Year=form.getvalue("Year")

#Bank Details
Bankname=form.getvalue("Bankname")
Accountno=form.getvalue("Accountno")
Accountholder=form.getvalue("Accountholder")
Accountype=form.getvalue("Accountype")
Ifsccode=form.getvalue("Ifsccode")
Bankbranch=form.getvalue("Bankbranch")

#Employement Details
Department=form.getvalue("Department")
Jobtitle=form.getvalue("Jobtitle")
Employmentstatus=form.getvalue("Employmentstatus")
Staffid=form.getvalue("Staffid")
Experience=form.getvalue("Experience")
Joiningdate=form.getvalue("Joiningdate")
Stime=form.getvalue("Stime")
Etime=form.getvalue("Etime")


mydb=mysql.connector.connect(host="localhost",user="root",password="",database="hds")
mycursor=mydb.cursor()

query=f'''INSERT INTO staff (Firstname, Middlename, Lastname, Phone, Gender, Address, Maritalstatus, Bloodgroup, Dob, Adhar, Pan, Passport, Mobile, Email, Mobile2, Email2, Country, State, City, Pincode, Address2, Education,   Specilisation, Institute, Percentage, Year, Bankname, Accountno, Accountholder, Accountype, Ifsccode, Bankbranch, Department, Jobtitle, Employmentstatus, Staffid, Experience, Joiningdate, Stime, Etime) VALUES ('{Firstname}','{Middlename}','{Lastname}','{Phone}','{Gender}','{Address}','{Maritalstatus}','{Bloodgroup}','{Dob}','{Adhar}','{Pan}','{Passport}','{Mobile}','{Email}','{Mobile2}','{Email2}','{Country}','{State}','{City}','{Pincode}','{Address2}','{Education}','{Specilisation}','{Institute}','{Percentage}','{Year}','{Bankname}','{Accountno}','{Accountholder}','{Accountype}','{Ifsccode}','{Bankbranch}','{Department}','{Jobtitle}','{Employmentstatus}','{Staffid}','{Experience}','{Joiningdate}','{Stime}','{Etime}')'''
#print(query)

mycursor.execute(query)
mydb.commit()

print(f'''
<script>alert("!!! Staff Register Successfully !!!");
    location.href="dashboard.py";
</script>''')