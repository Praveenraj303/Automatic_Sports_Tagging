#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
print("""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="../css/style.css">
<script>
function myFunction() {
    alert("Adding Succesful!");
}
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-97824898-1', 'auto');
ga('send', 'pageview');
</script>

</head>
<body>

<header>
<img src="./image/logo.png" width="100px" height="80px">
<h1 class="liketext">Sport Event

<a href ="./moduledegn.py"> <input type="button" value="Logout" style="float:right;"></a></h1>
</header>

<div class="row">
<nav>
		<div class="menu-icon">

		</div>
		<ul>
			<li><a href="#" style="color:red;">Add Events</a></li>


		</ul>
	</nav>

<div class="col-12">
<div style="padding-left:2%;width:100%;border-style:solid; border-radius:10px;border-color:#0000ff">
  <center><h1>Add Events</h1></center>                          

<form action="sportaddevent.py" method="post">
Event name:
<input type="text" name="ename" required class="smalltext">
Type: <select name="type" required class="smalltext">
  <option value="indoor">Indoor</option>
  <option value="outoor">Outdoor</option>

</select><br><br>
Description:                                                                      
<input type="text" name="description" required class="bigtext"><br><br>
  Start Date:  
<input type="date" name="start_date" required class="smalltext">
  End Date:  
<input type="date" name="end_date" required class="smalltext"><br><br>
Event Time:  
<input type="time" name="time" required class="smalltext"><br><br>
<center><input type="submit" value="Submit" onclick="myFunction()"></center>
</form>
</div>
</div>
</div>
</body>
</html>""")
print()
import cgi

form=cgi.FieldStorage()

ename=form.getvalue("ename")
type=form.getvalue("type")
description=form.getvalue("description")
start_date=form.getvalue("start_date")
end_date=form.getvalue("end_date")
time=form.getvalue("time")
import mysql.connector

con=mysql.connector.connect(user='root',password='',host='localhost',database='addevent')
cur=con.cursor()

cur.execute("insert into viewevent values(%s,%s,%s,%s,%s,%s)",(ename,type,description,start_date,end_date,time))
con.commit()

cur.close()
con.close()