#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Bootstrap CSS carousel-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>

    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<style>
    header{background-color: #4e608d;}
    .head1 img{
        height: 130px;
        width: 50%;
        margin-left: 130px;
        margin-right: 130px;
    }
    .carousel{
      margin-top: -40px;
    }
    .foot1{
      margin-top:-20px;
      background-color: darkgray;
    }
    .container-fluid{
        background-image: linear-gradient( 109.6deg, rgba(156,252,248,1) 11.2%, rgba(110,123,251,1) 91.1% );
    }
    </style>
<body>
    <header>
        <div class=" head1">
            <img src="./image/AAC3_1.png" alt="raj" >
        </div>
    </header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="./aac.py">HOME</a>
        <a class="navbar-brand" href="./facilities.py">Facilities</a>
        <a class="navbar-brand" href="./policies.py">Policies</a>
        <a class="navbar-brand" href="./activity.py">Activities</a>
        <a class="navbar-brand" href="./image/Achievements.pdf">Acheivement</a>
        <a class="navbar-brand" href="./gym.py">Gymnasium</a><a class="collapse navbar-collapse" id="navbarNavDropdown"></a>
        <ul class="nav navbar-nav navbar-right">
        <li><a class="navbar-brand" href="./studentview.py"><span class="glyphicon glyphicon-education"></span>Students</a></li>
            <li><a class="navbar-brand" href="./prince.py"><span class="glyphicon glyphicon-user"></span>Sign up</a></li>
            <li><a class="navbar-brand" href="./sporthlogin.py"><span class="glyphicon glyphicon-log-in"></span>Log-in</a></li>
        </ul>
    </nav>
       <div class="carousel" style="width: 100%;">
        <div id="carouselExampleIndicators" class="carousel-slide" data-ride="carousel">
            <ol class="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="./image/images (9).jfif" style="height:400px" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/baseball1.jpg" style="height:400px" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/american-football-touchdown-tackle-fight-sports - Copy.jpg" style="height:400px" class="d-block w-100" alt="...">
                </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
    <marquee behavior="scroll" scrolldelay="1" scrollamount="4"  height="30px">		    
        <a  style="color:#000; font-size: 18px;font-weight:bold;" target="_blank">ARUL ANANDAR COLLEGE</a>&nbsp;|&nbsp;&nbsp;
        <a  style="color:#000; font-size: 18px;font-weight:bold;" target="_blank">SPORTS EVENT</a>&nbsp;|&nbsp;&nbsp;
        <a  style="color:#000; font-size: 18px;font-weight:bold;" target="_blank">INDOOR / OUTDOOR GAMES</a>&nbsp;|&nbsp;&nbsp;
        <a  style="color:#000; font-size: 18px;font-weight:bold;" target="_blank">PARTICIPANT STUDENTS </a>&nbsp;|&nbsp;&nbsp;
    </marquee>
    <div class="container-fluid">
        <center><h4 class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:30px">GYMNASIUM</h4></center>
        <form id="ldc" name="ldc" method="post">
            <table >
                <tr><td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Policy Details of System & Procedures of Sports Complex & Activities
                </h4>
                <h5 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">I. Sports Complex</h5>
                <h5 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">	Indoor Stadium</h5>
                
                <p>1.The indoor stadium shall be kept open from 6.00am to 8.00am and from 4.00 pm to 6.30pm every day. </p>
                <p>2.	Players must sign in the attendance register. </p>
                <p>3.	The players shall participate or practice in proper sportswear. </p>
                <p>4.	Basketball, Volleyball, Table Tennis and Badminton games are conducted. </p>
                <p>5.	They shall avoid using slippers inside the stadium. </p>
                <p>6.	They must keep the stadium clean. </p>
                <p>7.	Safety measures will be maintained by the department. </p>
                <p>8.	First Aid materials will be available at any time. </p>
                
                </td></tr>
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Play Grounds </h4>
                <p>   1.	Practice will be conducted in all the above games in the morning and evening (6.00 – 8.30 am & 4.00 – 6.00 pm). </p>
                <p>2.	Students are provided ample opportunities with adequate facilities to participate in the tournaments and to practice for college teams. </p>
                <p>3.	Football, Hockey, Volleyball, Basketball, Kabaddi, Kho Kho, Handball and Track & Fields courts are well maintained. </p>
                <p>4.	The selection of teams will be conducted for all the above games. </p>
                <p>5.	Selective zonal and MKU tournaments are organized as decided in the respective general body meetings. </p>
                <p>6.	We provide facilities to the nearby schools to practice games in our play grounds and also helps them to conduct the tournaments and competitions.</p>
                
                </td>
                </tr>
                
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Multipurpose Gym </h4>
                <strong>     The facilities at AAC gym are to be utilized only by AAC students  </strong>
                <p> 1.The students should strictly follow the time schedule. </p>
                <p>2.	They must sign in the attendance register. </p>
                <p>3.	They should wear proper uniform and shoe.</p>
                <p>4.	They should not use slippers inside the gym.</p>
                <p>5.	They should handle the equipments of the gym safely. </p>
                <p>6.	They should maintain silence inside the gym. </p>
                <p>7.	They should maintain discipline and order during their practice.</p>
                <p>8.	First Aid materials will be available at any time </p>
                <p>9.	They must keep the gym clean. </p>
                <p>10.	Outsiders are not allowed.</p>
                
                </td>
                </tr>
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Timing</h4>
                <p>For students of other departments </p>
                <p>	Morning - 6.00 a.m. - 7.30 a.m. </p>
                <p>	Evening - 4.00 p.m. - 6.00 p.m.  
                <p>Women Students: 9.00 am – 11.00 am / 2.30 pm – 4.00 pm</p>
                <p>Physical Education Students: </p>
                <p>	Morning - 6.00 a.m. - 7.30 a.m. </p>
                <p>Evening - 5.30 p.m. - 6.00 p.m.  </p>
                <p>Sunday: Holiday</p>
                
                </td>
                </tr>
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Yoga and Meditation Centre </h4>
                
                
                <p> 1. Yoga center will be kept open from 6.00am to 7.30 am and 4.00 pm to 6.00 pm </p>
                <p>2. the students will be provided with yoga mats. </p>
                <p>3. They shall wear loose – cotton clothes for yoga classes. </p>
                <p>4. They should practice yoga on empty stomach </p>
                <p>5. Yoga exercises shall be practiced slowly on counts. </p>
                <p>6. They should maintain silence in the hall. </p>
                <p>7. They should abide by the instructions of the yoga teacher. </p>
                <p>8. Yoga competitions, tests and measurements shall be conducted at the end of the year. </p>
                
                </td>
                </tr>
                <tr>
                <td align="justify" colspan="2">
                <h2 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Activities</h2>
                <h4  class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Sports Day </h4>
                <p> 1. The Competitors shall participate in department-wise in all the sports events. </p>
                <p>2. They should participate in proper uniform (Sports Wear).</p>
                <p>3. A Competitor shall take part in any of the three events excluding relay from the given events. </p>
                <p>4. Only two competitors shall participate from a particular department so as to enable other departments to get a place in an event. </p>
                <p>5. All the departments shall participate in the march past which is also one of the competitions that involves rolling trophy and prizes up to the third place</p>
                <p>6. The winners of I, II & III places shall be honored by and medals and credentials. </p>
                <p>7. The participants or teams who/that violate the norms and discipline will be disqualified. </p>
                
                </td>
                </tr>
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Rural Sports Meet </h4>
                <p>
                <p> 1. The rural sports meet is open to all the metric and Govt. schools of Madurai district. </p>
                <p>2. The eligibility form of the athletes and players of these schools is submitted on or before competitions. </p>
                <p>3.	Only two competitors are permitted from each school and as the one reserves for a particular event. </p>
                <p>4.	A student can participate only in any three events. </p>
                <p>5.	All athletes should be in proper uniform </p>
                <p>6.	The athletes who are not present at the stipulated time will be disqualified from the events.  </p>
                <p>7.	The decision of jury of appeal will be final on all matters concerning the game and athletic events. </p>
                <p>8.	All communications and entries should be sent to the HOD, Department of Physical Education. </p>
                <p>9.	All participants will be provided with a working lunch. </p>
                <p>10.	All communications and entries should be sent to the HOD, Department of Physical Education. </p>
                <p>11.	They have to maintain discipline and order within the campus. </p>
                
                </td>
                </tr>
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Jogging & Walking – Outsiders </h4>
                
                <p>1.	The outsiders shall have their jogging and walking between 5.15am to 7.15 am only. </p>
                <p>2.	They should show the entry pass while entering the college gate. </p>
                <p>3.	They should not come in lungis inside the campus. </p>
                <p>4.	They can participate in games and walking only in the allotted areas. (Fr.Prince ground & badminton Court) </p>
                <p>5.	They should not enter boys’ hostel, offices, class rooms and also fathers residency. </p>
                <p>6.	They should keep the ground clean and shall not bring plastic items. </p>
                <p>7.	They should not cause damage to the properties of the college. </p>
                <p>8.	They should not cause an damage to the trees and plants on campus </p>
                <p>9.	They abide by the instructions of the gate keeper. </p>
                <p>10.	If any controversial opining, they shall approach the Director of Physical Education   </p>
                <p>11.	They should not disturb the students who are studing in the college by all means. </p>
                <p>12.	A permit ID card must be renewed once a year with the permission of the Rev.Fr.Secretary.  </p>
                <p>13.	The management will not be responsible for their personal belongings and the problems, if any occurs or arises. </p>
                <p>14.	If they don’t abide by the instructions of the college, they will be confined by the actions taken by the management. </p>
                
                </td>
                </tr> 
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Privileges for Sports Students </h4>
                <p> 1. Students’ privileges likes DA & TA of Rs 150 per head and actual travelling allowances (to & fro) respectively will be met out by the college. </p>
                <p>2. Uniforms shall be provided at free of cost. </p>
                <p>3. O.D. shall be arranged during practices and competitions.</p>
                <p>4. Re exams or doubling of the marks for the internal exams will be arranged accordingly. </p>
                <p>5. Management scholarships shall be provided for the best players. </p>
                <p>6. Admissions in to college with half – fee / full fee concessions will be provided according to their performance at state/ National level tournaments.</p> 
                <p>7. Free day – mid meals for days scholar players will be provided during team practice sessions. </p>
                <p>8. Nutrition (milk, egg & grams) shall be supplied during the team practices. </p>
                
                
                </td>
                </tr>
                <tr>
                <td align="justify" colspan="2">
                <h4 class="btn" style="background-color:#1B9E98;color:#fff;font-size:18pt;">Sports Coaches</h4>
                
                <p>	1. They will be recruited as sports coaches based on of their performance. </p>
                <p>	2. Consolidated remuneration or honourium will be given.</p>
                <p>	3. They have to train the teams from 6.00 to 8.00 am and from 4.00 to 6.00 pm. </p>
                <p>	4. They shall come in necessary uniform.</p>
                <p>	5. Boarding and lodging will be provided at free of cost </p>
                <p>	6. They should maintain decorum on the campus. </p>
                <p>	7. They should maintain attendance registers players’ participation. </p>
                <p>	8. They shall submit periodical reports of the performance of the teams / players. </p>
                
                </td>
                </tr>
                <tr>
                <td align="center" colspan="2">
                <img src="./image/g4.png" alt="image"><br>Dr. Vanitha J<br>
                Coordinator
                
                
                </td>
                </tr>
                
                </table>
        </form>
    </div>
    <footer class="foot1">
        <div id="gdlr-core-custom-menu-widget-4" class="widget widget_gdlr-core-custom-menu-widget kingster-widget">
            <h3 class="kingster-widget-title">Contact Us</h3><span class="clear"></span>
            <div class="menu-academics-container">
                <ul id="menu-academics" class="gdlr-core-custom-menu-widget gdlr-core-menu-style-plain">
                    <li class="menu-item"><a href="#">OFFICE : 04549-287221 / 04549-287208</a></li>
                    <li class="menu-item"><a href="#">PRINCIPAL : 9486379272</a></li>
                    <li class="menu-item"><a href="#">IQAC : 9442003808</a></li> 
                    <li class="menu-item"><a href="#">CONTROLLER OF EXAMINATIONS : 7092619782</a></li>
                    <li class="menu-item"><a href="#">FOR ADMISSION : <br> 6382842033 <br> 9444215203 <br> 9442128397 <br> 9788220257 <br> 9003398422</a></li>
                </ul>
            </div>
        </div>
    </footer>
</body>
</html>""")