#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Transparent Login Form with Blur Background</title>
	<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap" rel="stylesheet">
<script>
function myFunction() {
    alert("Adding Succesful!");
}
</script>
<style>
body {
	margin: 0;
	padding: 0;
	font-family: 'Poppins', sans-serif;
}
body:before {
	content: '';
	position: fixed;
	width: 100vw;
	height: 100vh;
	background-image: url(https://i.postimg.cc/8cf6v1rk/1.jpg);
	background-position: center center;
	background-repeat: no-repeat;
	background-attachment: fixed;
	-webkit-background-size: cover;
	background-size: cover;
	-webkit-filter: blur(10px);
	-moz-filter: blur(10px);
	filter: blur(10px);
}
.contact-form {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	width: 400px;
	height: 320px;
	padding: 80px 40px;
	background: rgba(0, 0, 0, 0.5);
}
.avatar {
	position: absolute;
	width: 80px;
	height: 80px;
	border-radius: 50%;
	overflow: hidden;
	top: calc(-80px/2);
	left: 190px;
}
.contact-form h2 {
	margin: 0;
	padding: 0 0 20px;
	color: #fff;
	text-align: center;
	text-transform: uppercase;
}
.contact-form p {
	margin: 0;
	padding: 0;
	font-weight: bold;
	color: #fff;
}
.contact-form input {
	width: 100%;
	margin-bottom: 20px;
}
.contact-form input[type=email], .contact-form input[type=password] {
	border: none;
	border-bottom: 1px solid #fff;
	background: transparent;
	outline: none;
	height: 40px;
	color: #fff;
	font-size: 16px;
}
.contact-form input[type=submit] {
	height: 30px;
	color: #fff;
	font-size: 15px;
	background: red;
	cursor: pointer;
	border-radius: 25px;
	border: none;
	outline: none;
	margin-top: 15%;
}
.contact-form a {
	color: #fff;
	font-size: 14px;
	font-weight: bold;
	text-decoration: none;
}
input[type=checkbox] {
	width: 20%;
}

</style>
</head>

<body>
    
	<div class="contact-form">
		<img alt="" class="avatar" src="./image/logo.png">
		<h3>Sports report</h3>
		<form method="POST" action="volunReg.py">
		<p style="font-size:20px;color:red" ><label for="event">Event</label></p>
			<select name="event" style="height:fit-content;width:250px;height:20px">
				<option value="none" selected>Event</option>
				<option value="Sports Event" selected>Sports Event</option>
				<option value="Running race">Running race</option>
				<option value="Hockey">Hockey</option>
				<option value="Kabadi">Kabadi</option>
				<option value="shot put">Shot Put</option>
				<option value="Long Jump">Long Jump</option>
				<option value="Football">Football</option>
				<option value="Vollyball">Volley Ball</option>
			</select>
		<p style="font-size:20px;color:red" ><label for="event">Category</label></p>
			<select name="Category" style="height:fit-content;width:250px;height:20px">
				<option value="none" selected>Event</option>
				<option value="Single player">Single player</option>
				<option value="Team Players">Team Players</option>
				<option value="Over All Championship">Over All Championship</option>
			</select>
		<p style="font-size:20px;color:red"><label for="name">Enter Name/Team</label></p>
		<input type="text" id="name" name="name" style="width:250px;height:20px">
		<p style="font-size:20px;color:red"><label for="Department">Department</label></p>
			<select name="Department" style="height:fit-content;width:250px;height:20px">
				<option value="none" selected>Department</option>
				<option value="TAMIL">DEPARTMENT OF TAMIL</option>
				<option value="ENGLISH">DEPARTMENT OF ENGLISH</option>
				<option value="COMPUTER">DEPARTMENT OF COMPUTER SCIENCE</option>
				<option value="HISTORY">DEPARTMENT OF HISTORY</option>
				<option value="ECONOMICS">DEPARTMENT OF ECONOMICS</option>
				<option value="PHILOSOPHY">DEPARTMENT OF PHILOSOPHY</option>
				<option value="MATHEMATICS">DEPARTMENT OF MATHEMATICS</option>
				<option value="PHYSICS">DEPARTMENT OF PHYSICS</option>
				<option value="CHEMISTRY">DEPARTMENT OF CHEMISTRY</option>
				<option value="RURAL DEVELOPMENT SCIENCE">DEPARTMENT OF RURAL DEVELOPMENT SCIENCE</option>
				<option value="COMMERCE WITH CA">DEPARTMENT OF COMMERCE WITH CA</option>
				<option value="PHYSICAL EDUCATION">DEPARTMENT OF PHYSICAL EDUCATION</option>
			</select>
		<p style="font-size:20px;color:red"><label for="position">Position</label></p>
			<select name="Position" style="height:fit-content;width:250px;height:30px">
				<option value="none" selected>Position</option>
				<option value="Winner">Winner</option>
				<option value="1st RunnerUp">1st RunnerUp</option>
				<option value="2nd RunnerUp">2nd RunnerUp</option>
			</select>
		<input type="submit" value="submit" onclick="myFunction()">
	</form>
	</div>
</body>
</html>""")
print()
import cgi
form = cgi.FieldStorage()

event = form.getvalue("event")
Category = form.getvalue("Category")
name = form.getvalue("name")
Department = form.getvalue("Department")
Position = form.getvalue("Position")


import mysql.connector
con = mysql.connector.connect(user='root',password='',host='localhost',database='sportsscoreresult')
cur = con.cursor()

if form.getvalue("Category") == "Single player":
    cur.execute("insert into singleplayer values(%s,%s,%s,%s,%s)",(event,Category,name,Department,Position))
    con.commit()
elif form.getvalue("Category") == "Team Players":
    cur.execute("insert into teamplayer values(%s,%s,%s,%s,%s)",(event,Category,name,Department,Position))
    con.commit()
elif form.getvalue("Category") == "Over All Championship":
    cur.execute("insert into overchampion values(%s,%s,%s,%s,%s)",(event,Category,name,Department,Position))
    con.commit()
cur.close()
con.close()
# print("<h1>click below the 'Home' link</h1>")
# print("<h1><a href='./aac.py'>Back to Home</a></h1>")

