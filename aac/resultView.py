#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import mysql.connector
import cgitb
cgitb.enable()
con = mysql.connector.connect(user='root', password='', host='localhost', database='sportsscoreresult')
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Transparent Login Form with Blur Background</title>
	<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;900&display=swap" rel="stylesheet">
<style>
body{
  font-family: 'Helvetica Neue', Helvetica, Arial;
  font-size: 14px;
  line-height: 20px;
  font-weight: 400;
  color: #3b3b3b;
  -webkit-font-smoothing: antialiased;
  font-smoothing: antialiased;
  background: #2b2b2b;
  }
  @media screen and (max-width: 580px){
    font-size: 16px;
    line-height: 22px;
}
.wrapper
 {
  margin: 0 auto;
  padding: 40px;
  max-width: 800px;
}
.table
 {
  margin: 0 0 40px 0;
  width: 100%;
  box-shadow: 0 1px 3px rgba(0,0,0,0.2);
  display: table;
  }
  @media screen and (max-width: 580px){
    display: block;
}
.row
 {
  display: table-row;
  background: #f6f6f6;
  }
.nth-of-type(odd){
    background: red;
  }
.header{
    font-weight: 900;
    color: #ffffff;
    background: #ea6153;
  }
.green
   {
    background: #27ae60;
  }
.blue
   {
    background: #2980b9;
   }
  @media screen and (max-width: 580px)
    {
    padding: 14px 0 7px;
    display: block;
    }
.header{
      padding: 0;
      height: 6px;
      }
.cell{
    display: none;
}
.cell{
    margin-bottom: 10px;
}
      &:before{
        margin-bottom: 3px;
        content: attr(data-title);
        min-width: 98px;
        font-size: 10px;
        line-height: 10px;
        font-weight: bold;
        text-transform: uppercase;
        color: #969696;
        display: block;
}
.cell{
  padding: 6px 12px;
  display: table-cell;}
  @media screen and (max-width: 580px){
    padding: 2px 16px;
    display: block;
    }
</style>
</head>
<body>
<a href ="./TeamPlayer.py"> <input type="button" value="TeamPlayer" style="padding:10px 42px;float:right"></a></h1>
<a href ="./overallchampion.py"> <input type="button" value="OverAllChampion" style="padding:10px 42px;float:right"></a></h1>
<center><h1 style="color:red">STUDENTS RESULTS</H1></center>
</body>
</html>""")
q = """select * from singleplayer"""
cur.execute(q)
rec = cur.fetchall()
print("""
<div class="wrapper">
<h2 style="color:#00FA9A">Single Game result</h2>
  <div class="table">

    <div class="row header" style="color:#4876FF">
      <div class="cell">
        Event
      </div>
      <div class="cell">
        Category
      </div>
      <div class="cell">
        Name
      </div>
      <div class="cell">
        Department
      </div>
      <div class="cell">
        Position
      </div>
    </div>""")
for i in rec:
    print("""

    <div class="row">
      <div class="cell" data-title="event">
        %s
      </div>
      <div class="cell" data-title="Category">
        %s
      </div>
      <div class="cell" data-title="Name">
        %s
      </div>
      <div class="cell" data-title="Department">
        %s
      </div>
      <div class="cell" data-title="Position">
        %s
      </div>
    </div>"""% (i[0], i[1], i[2], i[3],i[4]))

print("<h3><a href='./studentview.py'>EXIT</a></h3>")

# T = """select * from teamplayer"""
# cur.execute(T)
# tp = cur.fetchall()
# print("""
# <div class="wrapper">
# <h3 style="color:blue">Team Game result</h3>
#   <div class="table">
#
#     <div class="row header">
#       <div class="cell">
#         Event
#       </div>
#       <div class="cell">
#         Name
#       </div>
#       <div class="cell">
#         Department
#       </div>
#       <div class="cell">
#         Position
#       </div>
#     </div>""")
# for i in tp:
#     print("""
#
#     <div class="row">
#       <div class="cell" data-title="event">
#         %s
#       </div>
#       <div class="cell" data-title="Name">
#         %s
#       </div>
#       <div class="cell" data-title="Department">
#         %s
#       </div>
#       <div class="cell" data-title="Position">
#         %s
#       </div>
#     </div>"""% (i[0], i[1], i[2], i[3]))
# print("""
#   <div class="table">
#
#     <div class="row header green">
#       <div class="cell">
#         Event
#       </div>
#       <div class="cell">
#         Name
#       </div>
#       <div class="cell">
#         Department
#       </div>
#       <div class="cell">
#         Position
#       </div>
#     </div>""")
# for i in tp:
#     print("""
#
#     <div class="row">
#       <div class="cell" data-title="event">
#         %s
#       </div>
#       <div class="cell" data-title="Name">
#         %s
#       </div>
#       <div class="cell" data-title="Department">
#         %s
#       </div>
#       <div class="cell" data-title="Position">
#         %s
#       </div>
#     </div>"""% (i[0], i[1], i[2], i[3]))
#
#     <div class="row">
#       <div class="cell" data-title="Product">
#         Solid oak work table
#       </div>
#       <div class="cell" data-title="Unit Price">
#         $800
#       </div>
#       <div class="cell" data-title="Quantity">
#         10
#       </div>
#       <div class="cell" data-title="Date Sold">
#         03/15/2014
#       </div>
#       <div class="cell" data-title="Status">
#         Waiting for Pickup
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Product">
#         Leather iPhone wallet
#       </div>
#       <div class="cell" data-title="Unit Price">
#         $45
#       </div>
#       <div class="cell" data-title="Quantity">
#         120
#       </div>
#       <div class="cell" data-title="Date Sold">
#         02/28/2014
#       </div>
#       <div class="cell" data-title="Status">
#         In Transit
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Product">
#         27" Apple Thunderbolt displays
#       </div>
#       <div class="cell" data-title="Unit Price">
#         $1000
#       </div>
#       <div class="cell" data-title="Quantity">
#         25
#       </div>
#       <div class="cell" data-title="Date Sold">
#         02/10/2014
#       </div>
#       <div class="cell" data-title="Status">
#         Delivered
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Product">
#         Bose studio headphones
#       </div>
#       <div class="cell" data-title="Unit Price">
#         $60
#       </div>
#       <div class="cell" data-title="Quantity">
#         90
#       </div>
#       <div class="cell" data-title="Date Sold">
#         01/14/2014
#       </div>
#       <div class="cell" data-title="Status">
#         Delivered
#       </div>
#     </div>
#
#   </div>
#
#   <div class="table">
#
#     <div class="row header blue">
#       <div class="cell">
#         Username
#       </div>
#       <div class="cell">
#         Email
#       </div>
#       <div class="cell">
#         Password
#       </div>
#       <div class="cell">
#         Active
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Username">
#         ninjalug
#       </div>
#       <div class="cell" data-title="Email">
#         misterninja@hotmail.com
#       </div>
#       <div class="cell" data-title="Password">
#         ************
#       </div>
#       <div class="cell" data-title="Active">
#         Yes
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Username">
#         jsmith41
#       </div>
#       <div class="cell" data-title="Email">
#         joseph.smith@gmail.com
#       </div>
#       <div class="cell" data-title="Password">
#         ************
#       </div>
#       <div class="cell" data-title="Active">
#         No
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Username">
#         1337hax0r15
#       </div>
#       <div class="cell" data-title="Email">
#         hackerdude1000@aol.com
#       </div>
#       <div class="cell" data-title="Password">
#         ************
#       </div>
#       <div class="cell" data-title="Active">
#         Yes
#       </div>
#     </div>
#
#     <div class="row">
#       <div class="cell" data-title="Username">
#         hairyharry19
#       </div>
#       <div class="cell" data-title="Email">
#         harryharry@gmail.com
#       </div>
#       <div class="cell" data-title="Password">
#         ************
#       </div>
#       <div class="cell" data-title="Active">
#         Yes
#       </div>
#     </div>
#
#   </div>
#
# </div>""")
print("""</table>""")
# T = """select * from teamplayer"""
# cur.execute(T)
# tp = cur.fetchall()
# print("""
# <h3 style="color:blue">Team Game result</h3>
#   <div class="table">
#
#     <div class="row header">
#       <div class="cell">
#         Event
#       </div>
#       <div class="cell">
#       Category
#       </div>
#       <div class="cell">
#         Name
#       </div>
#       <div class="cell">
#         Department
#       </div>
#       <div class="cell">
#         Position
#       </div>
#     </div>""")
# for i in tp:
#     print("""
#
#     <div class="row">
#       <div class="cell" data-title="event">
#         %s
#       </div>
#       <div class="cell" data-title="Category">
#       %s
#       </div>
#       <div class="cell" data-title="Name">
#         %s
#       </div>
#       <div class="cell" data-title="Department">
#         %s
#       </div>
#       <div class="cell" data-title="Position">
#         %s
#       </div>
#     </div>"""% (i[0], i[1], i[2], i[3],i[4]))
# print("""</table>""")