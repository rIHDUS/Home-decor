#!C:/Python312/python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-type: text/html\n")
form=cgi.FieldStorage()
#print(form)
sid=form.getvalue('sid')
#print(sid)

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


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hds"
)
mycursor=mydb.cursor(dictionary=True)
query = f"""UPDATE staff SET Firstname = '{Firstname}', Middlename = '{Middlename}', Lastname = '{Lastname}', Phone = '{Phone}',Gender='{Gender}', Address = '{Address}', Maritalstatus = '{Maritalstatus}',Bloodgroup='{Bloodgroup}',Dob='{Dob}', Adhar = '{Adhar}', Pan = '{Pan}', Passport = '{Passport}', Mobile = '{Mobile}',Email = '{Email}',Mobile2='{Mobile2}',Email2='{Email2}',Country='{Country}',State='{State}', City = '{City}', Pincode = '{Pincode}', Address2 = '{Address2}', Education = '{Education}',Specilisation = '{Specilisation}',Institute=''{Institute},Percentage='{Percentage}', Year = '{Year}', Bankname = '{Bankname}', Accountno = '{Accountno}', Accountholder = '{Accountholder}', Accountype = '{Accountype}', Ifsccode = '{Ifsccode}', Bankbranch = '{Bankbranch}', Department = '{Department}', Jobtitle = '{Jobtitle}', Employmentstatus = '{Employmentstatus}',Staffid='{Staffid}', Experience = '{Experience}',Joiningdate='{Joiningdate}' WHERE sid = {sid}"""
#print(query)

mycursor.execute(query)
mydb.commit()

print('''
    <script>alert("!!! Staff Record Updated Successfully !!!");
        location.href="stafflist.py";
    </script>''')