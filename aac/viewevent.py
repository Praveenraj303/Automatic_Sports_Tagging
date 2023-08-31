#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import mysql.connector
import cgitb
cgitb.enable()
con = mysql.connector.connect(user='root', password='', host='localhost', database='addevent')
cur = con.cursor()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
table {
  border-collapse: collapse;
  width: 100%;
}
th{
color:#CD0000;
}
th, td {
  text-align: left;
  padding: 8px;
}
h1{
color:	#191970;
}
tr:nth-child(even) {background-color: #f2f2f2;}
</style>
</head>
<body>
<h1>  EVENT DETAILS</h1>
</body>
</html>""")
q = """select * from viewevent"""
cur.execute(q)
rec = cur.fetchall()
print("""
<div style="overflow-x: auto;">

<table>
<tr>
    <th>EVENT NAME</th>
    <th>TYPE</th>
    <th>DESCRIPTION</th>
    <th>START_DATE</th>
    <th>END_DATE</th>
    <th>TIME</th>
</tr>""")
for i in rec:
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
</tr>""" % (i[0], i[1], i[2], i[3], i[4], i[5]))
print("""</table>""")

print("<h1><center><a href='./studentview.py'>EXIT</a></center></h1>")