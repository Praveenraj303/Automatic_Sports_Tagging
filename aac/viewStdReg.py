#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")

import mysql.connector
import cgitb
cgitb.enable()
con = mysql.connector.connect(user='root', password='', host='localhost', database='stusportreg')
cur = con.cursor()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{
  margin: 0;
  pading: 0;
  box-sizing: border-box;
}
body{
  background-color: rgb(63,72,83);
  font-family: sans-serif;
  color: rgb(220,220,220);
  padding: 50px;
  width: 100vw;
  overflow-x: hidden;
}
h1{
  font-weight: 400;
}
a{
  color: inherit;
}
p{
  margin-top: .7em;
}
.warning{
  color: rgb(62,148,236);
}
.st_viewport{
  max-height: 500px;
  overflow: auto;
}

[data-table_id="1"]{
  background-color: rgb(255,115,0);
}
[data-table_id="2"]{
  background-color: rgb(61,53,39);
  color: rgb(220,220,220);
}
[data-table_id="3"]{
  background-color: rgba(168,189,4, .8);
}

._section1{
  min-width: 130px;
}
._section2{
  min-width: 120px;
}
._section3{
  min-width: 160px;
}
._section4{
  min-width: 280px;
}
._section5{
  min-width: 100px;
}
._section6{
  min-width: 130px;
}
._section7{
  min-width: 130px;
}
._section8{
  min-width: 180px;
}
pre{
  overflow: auto;
}

/** Sticky table styles **/
.st_viewport{
  background-color: rgb(62,148,236);
  color: rgb(27,30,36);
  margin: 20px 0;
}
/* ###  Table wrap */
.st_wrap_table{
  
}
/* ##   header */
.st_table_header{
  position: -webkit-sticky;
  position: sticky;
  top: 0px;
  z-index: 1;
  background-color: rgb(27,30,36);
  color: rgb(220,220,220);
}
.st_table_header h2{
  font-weight: 400;
  margin: 0 20px;
  padding: 20px 0 0;
}
.st_table_header .st_row{
  color: rgba(220,220,220, .7);
}
.st_table_header .st_column{
  
}
/* ##  table */
.st_table{
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-flex-direction: column;
      -ms-flex-direction: column;
          flex-direction: column;
}
/* #   row */
.st_row{
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  margin: 0;
}
.st_table .st_row:nth-child(even){
  background-color: rgba(0,0,0, .1)
}
/* #   column */
.st_column{
  padding: 10px 20px;
}
</style>
</head>
<body>
<header>
<a href ="./moduledegn.py"> <input type="button" value="Logout" style="float:right;"></a></h1>
<h1>STUDENTS REGISTRATION</h1>
</header>
</body>
</html>""")
q = """select * from runrace"""
cur.execute(q)
rec = cur.fetchall()
k = """select * from kabadi"""
cur.execute(k)
ka = cur.fetchall()
rr =cur.fetchall()
h = """select * from hockey"""
cur.execute(h)
hy=cur.fetchall()
b = """select * from basketball"""
cur.execute(b)
bb=cur.fetchall()
v = """select * from vollyball"""
cur.execute(v)
vb=cur.fetchall()
t = """select * from tabletennis"""
cur.execute(t)
tt=cur.fetchall()
m = """select * from badminton"""
cur.execute(m)
bm=cur.fetchall()
f = """select * from football"""
cur.execute(f)
fb=cur.fetchall()

ko= """select * from khokho"""
cur.execute(ko)
kk=cur.fetchall()

hd = """select * from handball"""
cur.execute(hd)
hb=cur.fetchall()
print("""
<main class="st_viewport">
  <div class="st_wrap_table" data-table_id="0">
    <header class="st_table_header">
      <h2>Running Race</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in rec:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))

print("""
  <div class="st_wrap_table" data-table_id="1">
    <header class="st_table_header">
      <h2>KABADI EVENTS</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in ka:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))
print("""

  <div class="st_wrap_table" data-table_id="2">
    <header class="st_table_header">
      <h2>Basket Ball</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in bb:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))
print("""

  <div class="st_wrap_table" data-table_id="3">
    <header class="st_table_header">
      <h2>Volly Ball</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in vb:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))

print("""
  <div class="st_wrap_table" data-table_id="1">
    <header class="st_table_header">
      <h2>Table Tennis</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in tt:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))
print("""

  <div class="st_wrap_table" data-table_id="2">
    <header class="st_table_header">
      <h2>Badminton</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in bm:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))
print("""
  <div class="st_wrap_table" data-table_id="3">
    <header class="st_table_header">
      <h2>Foot Ball</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in fb:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))
print("""
<main class="st_viewport">
  <div class="st_wrap_table" data-table_id="0">
    <header class="st_table_header">
      <h2>Kho Kho</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in kk:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))

print("""
  <div class="st_wrap_table" data-table_id="1">
    <header class="st_table_header">
      <h2>Hand Ball</h2>
      <div class="st_row">
        <div class="st_column _section1">Roll no</div>
        <div class="st_column _section2">Name</div>
        <div class="st_column _section3">department</div>
        <div class="st_column _section4">email</div>
        <div class="st_column _section5">event</div>
        <div class="st_column _section6">gender</div>
        <div class="st_column _section7">district</div>
        <div class="st_column _section8">state</div>
      </div>
    </header>""")
for i in hb:
    print("""
    <div class="st_table">
      <div class="st_row">
        <div class="st_column _section1">%s</div>
        <div class="st_column _section2">%s</div>
        <div class="st_column _section3">%s</div>
        <div class="st_column _section4">%s</div>
        <div class="st_column _section5">%s</div>
        <div class="st_column _section6">%s</div>
        <div class="st_column _section7">%s</div>
        <div class="st_column _section8">%s</div>
      </div>"""% (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7]))

print("""</table>""")