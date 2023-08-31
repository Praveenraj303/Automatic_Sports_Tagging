#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html")
print("""
<!DOCTYPE html>
<html>

<head>
  <title>Event Registration Form.</title>
</head>
<style>
	body {
		font-family: "Raleway", sans-serif;
		background-color: #ff6655;
	  }
	  h1 {
		text-align: center;
		margin: 20px auto;
	  }
	  form {
		width: 50%;
		height:700px;
		margin: auto;
	  }
	  fieldset {
		padding: 20px;
		border: 1px solid #ccc;
		border-radius: 10px;
		margin: 20px auto;
		box-shadow: 0 0 5px #333;
		background-color: #eee;
	  }
	  label {
		display: block;
		
		margin-bottom: 5px;
	  }
	  input[type="text"],input[type="email"],select{
		width: calc(100% - 20px);
		height: 20px;
		padding: 5px;
		border-radius: 6px;
		border: 1px solid #ccc;
		margin-bottom: 10px;
	  }
	  button {
		width: 100%;
		text-align: center;
		margin: auto !important;
		height: 40px;
		border-radius: 10px;
		background-color: #eee;
	  }
	  
</style>
<script>
function myFunction() {
    alert("Registerd Successfully!");
}
</script>
<body>
	<div id="event-registration">
		<h1>AAC SPORTS REGISTRATION</h1>
		<form id="event-registration-form" method="POST" action="studentreg.py">
		  <!-- Form contents will go here -->
		  <fieldset>
			<h3>STUDENT PARTICIPATE FORM</h3>
			<label for="rollno">Roll_no</label>
			<input type="text" id="rollno" name="rollno" />
			<label for="name">Enter Name</label>
			<input type="text" id="name" name="name" />
			<label for="department">Department</label>
			<input type="text" id="department" name="department" />
			<label for="email">Email</label>
			<input type="email" id="email" name="email" />
			<label for="event">Event</label>
			<select name="event" style="height:fit-content;">
				<option value="none" selected>Event</option>
				<option value="Running race">Running race</option>
				<option value="kabadi">kabadi</option>
				<option value="Hockey">Hockey</option>
				<option value="Basketball">Basketball</option>
				<option value="Vollyball">Vollyball</option>
				<option value="TableTennis">TableTennis</option>
				<option value="Badminton">Badminton</option>
				<option value="Football">Football</option>
				<option value="KhoKho">KhoKho</option>
				<option value="Handball">Handball</option>
			</select>
			<label for="gender">Gender</label>
			<select name="gender" style="height:fit-content;">
				<option value="none" selected>Gender</option>
				<option value="male">Male</option>
				<option value="female">Female</option>
				<option value="other">other</option>
			</select>
			<label for="state">District</label>
			<!-- <select id="states" style="height: 35px;">
				<option>-- Choose your state --</option>
			  </select> -->
			  <select name="district" id="district" class="form-control" style="height:fit-content;">
				<option value="Ariyalur">Ariyalur</option>
				<option value="Chennai">Chennai</option>
				<option value="Coimbatore">Coimbatore</option>
				<option value="Cuddalore">Cuddalore</option>
				<option value="Dharmapuri">Dharmapuri</option>
				<option value="Dindigul">Dindigul</option>
				<option value="Erode">Erode</option>
				<option value="Kallakurichi">Kallakurichi</option>
				<option value="Kanchipuram">Kanchipuram</option>
				<option value="Kanniyakumari">Kanniyakumari</option>
				<option value="Karur">Karur</option>
				<option value="Krishnagiri">Krishnagiri</option>
				<option value="Madurai">Madurai</option>
				<option value="Nagapattinam">Nagapattinam</option>
				<option value="	Namakkal">Namakkal</option>
				<option value="Nilgiris">Nilgiris</option>
				<option value="	Perambalur">Perambalur</option>
				<option value="Pudukkottai">Pudukkottai</option>
				<option value="Ramanathapuram">Ramanathapuram</option>
				<option value="Salem">Salem</option>
				<option value="Sivaganga">Sivaganga</option>
				<option value="	Thanjavur">Thanjavur</option>
				<option value="	Theni">Theni</option>
				<option value="Thoothukudi">Thoothukudi</option>
				<option value="	Tiruchirappalli">Tiruchirappalli</option>
				<option value="Tirunelveli">Tirunelveli</option>
				<option value="	Tiruppur">Tiruppur</option>
				<option value="Tiruvallur">Tiruvallur</option>
				<option value="Tiruvannamalai">Tiruvannamalai</option>
				<option value="Tiruvarur">Tiruvarur</option>
				<option value="Vellore">Vellore</option>
				<option value="Viluppuram">Viluppuram</option>
				<option value="Virudhunagar">Virudhunagar</option>

				</select>
				<label for="state">State</label>
			<select name="state" id="state" class="form-control" style="height:fit-content;">
				<option value="Andhra Pradesh">Andhra Pradesh</option>
				<option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
				<option value="Arunachal Pradesh">Arunachal Pradesh</option>
				<option value="Assam">Assam</option>
				<option value="Bihar">Bihar</option>
				<option value="Chandigarh">Chandigarh</option>
				<option value="Chhattisgarh">Chhattisgarh</option>
				<option value="Dadar and Nagar Haveli">Dadar and Nagar Haveli</option>
				<option value="Daman and Diu">Daman and Diu</option>
				<option value="Delhi">Delhi</option>
				<option value="Lakshadweep">Lakshadweep</option>
				<option value="Puducherry">Puducherry</option>
				<option value="Goa">Goa</option>
				<option value="Gujarat">Gujarat</option>
				<option value="Haryana">Haryana</option>
				<option value="Himachal Pradesh">Himachal Pradesh</option>
				<option value="Jammu and Kashmir">Jammu and Kashmir</option>
				<option value="Jharkhand">Jharkhand</option>
				<option value="Karnataka">Karnataka</option>
				<option value="Kerala">Kerala</option>
				<option value="Madhya Pradesh">Madhya Pradesh</option>
				<option value="Maharashtra">Maharashtra</option>
				<option value="Manipur">Manipur</option>
				<option value="Meghalaya">Meghalaya</option>
				<option value="Mizoram">Mizoram</option>
				<option value="Nagaland">Nagaland</option>
				<option value="Odisha">Odisha</option>
				<option value="Punjab">Punjab</option>
				<option value="Rajasthan">Rajasthan</option>
				<option value="Sikkim">Sikkim</option>
				<option value="Tamil Nadu">Tamil Nadu</option>
				<option value="Telangana">Telangana</option>
				<option value="Tripura">Tripura</option>
				<option value="Uttar Pradesh">Uttar Pradesh</option>
				<option value="Uttarakhand">Uttarakhand</option>
				<option value="West Bengal">West Bengal</option>
				</select>
		  </fieldset>
		<center><input type="submit" value="Submit" onclick="myFunction()" style="color:black;size:300px;height:60px;width:200px;background:blue"></center>
	  </div>
</body>

</html>""")
print()
import cgi



form=cgi.FieldStorage()

rollno=form.getvalue("rollno")
name=form.getvalue("name")
department=form.getvalue("department")
email=form.getvalue("email")
event=form.getvalue("event")
gender=form.getvalue("gender")
district=form.getvalue("district")
state=form.getvalue("state")

import mysql.connector
con=mysql.connector.connect(user='root',password='',host='localhost',database='stusportreg')
cur=con.cursor()

if form.getvalue("event")=="Running race":
    cur.execute("insert into runrace values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="Hockey":
    cur.execute("insert into hockey values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="kabadi":
    cur.execute("insert into kabadi values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="Basketball":
    cur.execute("insert into basketball values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="Vollyball":
    cur.execute("insert into vollyball values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="TableTennis":
    cur.execute("insert into tabletennis values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="Badminton":
    cur.execute("insert into badminton values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="Football":
    cur.execute("insert into football values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="KhoKho":
    cur.execute("insert into khokho values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
if form.getvalue("event")=="Handball":
    cur.execute("insert into handball values(%s,%s,%s,%s,%s,%s,%s,%s)",(rollno,name,department,email,event,gender,district,state))
    con.commit()
cur.close()
con.close()

print("<h1><a href='./studentview.py'>EXIT</a></h1>")
