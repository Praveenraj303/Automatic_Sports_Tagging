#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
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
      margin-top: -20px;
    }
    .foot1{
      background-color: darkgray;
      margin-top:-20px;
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
                    <img src="./image/kabadi.jfif" style="height:400px" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/images (9).jfif" style="height:400px" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/running.jpg" style="height:400px" class="d-block w-100" alt="...">
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
        <center><h5 class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:28px">Policy Details of System & Procedures of Sports Complex & Activitie</h5></center>
        <form id="ldc" name="ldc" method="post">
            <table border="0" cellpadding="10" style="font-family:calibri; font-size:14pt; width:100%">
                <tr><td align="justify">
                    <label class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:26px">I.Sports Complex</label><br />
                    <label class="btn" style="background-color:#2d57cc;  text-align:left; color:#FFF;font-size:24px">1. Indoor Stadium </label><br />
                    <p>1. The indoor stadium shall be kept open from 6.00am to 8.00am and from 4.00 pm to 6.30pm. </p>
                    <p>2. Players must sign in the attendance register. </p>
                    <p>3. The players shall participate or practice in proper sportswear. </p>
                    <p>4. Basketball, Volleyball, Table Tennis and Badminton games are conducted. </p>
                    <p>5. They shall avoid using slippers inside the stadium. </p>
                    <p>6. They must keep clean the stadium</p>
                    <p>7. Safety measures will be maintained by the department. </p>
                    <p>8. First Aid materials will be available at any time.</p>
                    <label class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:24px">2. Play Grounds</label><br />
                    <p>1. Practice will be conducted in all the above games in the morning and evening (6.00 –8.30 am & 4.00 – 6.00 pm)</p>
                    <p>2. Students are provided ample opportunities with adequate facilities to participate in the tournaments and to practice for college teams. </p>
                    <p>3. Football, Hockey, Volleyball, Basketball, Kabaddi, Kho Kho, Handball and Track & Fields courts are well maintained. </p>
                    <p>4. Team's selections will be conducted on all the above games. </p>
                    <p>5. Selective zonal and MKU tournaments are organized as decided in the respective general body meetings. </p>
                    <p>6. We provide facilities for the nearby schools to practice in our play grounds and to conduct the tournaments and competitions. </p>
                    <label class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:24px">3. Multipurpose Gym</label><br />
                    <p>The facilities at AAC gym are to be utilized only by AAC students</p>
                    <p>1. Students should strictly follow the time schedule. </p>
                    <p>2. The students must sign in the attendance register</p>
                    <p>3. They should wear proper uniform and shoe.</p>
                    <p>4. They should not use slippers inside the gym. </p>
                    <p>5. They should handle the materials safely. </p>
                    <p>6. They should maintain silence inside the gym</p>
                    <p>7. They should maintain discipline and order. </p>
                    <p>8. First Aid materials will be available at any time</p>
                    <p>9. They must keep clean the gym</p>
                    <p>10. Outsiders are not allowed.</p>
                    <label class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:24px">Timing:</label><br />
                    <p>Students from other departments</p>
                    <p> Morning - 6.00 a.m. - 7.30 a.m. </p>
                    <p>Evening - 4.00 p.m. - 6.00 p.m. </p>
                    <p>Women Students: 9.00 am – 11.00 am / 2.30 pm – 4.00 pm</p>
                    <p>Physical Education Students:</p>
                    <p> Morning - 6.00 a.m. - 7.30 a.m.</p>
                    <p> Evening - 5.30 p.m. - 6.00 p.m. </p>
                    <p>Sunday: Holiday</p>
                    <label class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:24px">4. Yoga and Meditation Centre</label><br />
                    <p>1. Yoga center will be kept open from 6.00am to 7.30 am and 4.00 pm to 6.00 pm</p>
                    <p>2. Students will be provided with yoga mats. 3. They shall wear loose – cotton dress</p>
                    <p>4. They should practice yoga on empty stomach</p>
                    <p>5. Yoga exercise shall be practiced slowly on counts.</p> 
                    <p>6. They should maintain silence in the hall</p>
                    <p>7. They should abide by the instructions of the yoga teacher. </p>
                    <p>8. Yoga competitions, tests and measurements shall be conducted at year end</p>
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
    </footer
</body>
</html>""")