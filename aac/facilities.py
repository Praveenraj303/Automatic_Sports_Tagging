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
    .container-fluid{
        background-image: linear-gradient( 109.6deg, rgba(156,252,248,1) 11.2%, rgba(110,123,251,1) 91.1% );
    }
    .foot1{
      margin-top:-20px;
      background-color: darkgray;
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
                    <img src="./image/sports.jpg" style="height:400px" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/cricket.jfif" style="height:400px" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/sports1.jpg" style="height:400px" class="d-block w-100" alt="...">
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
        <form id="ldc" name="ldc" method="post">
            <center><h3 class="btn" style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:32px">SPORTS & GAMES</h3></center>
            <h4 style="background-color:#1B9E98;  text-align:left; color:#FFF;font-size:30px">PHYSICAL EDUCATION FACILITIES</h4>
            <table border="0" cellpadding="5" width="100%">
                <tr class="bg-primary" style="color:#FFFFFF;font-size:27px"><th align="left" style="width:8%">1.</th><th align="left" colspan="2">Major Games</th><th align="center" style="width:20%">Court</th></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Football</td><td align="center">2</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Hockey</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Basketball</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Volleyball</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Cricket</td><td align="center">1</td></tr>
                <tr class="bg-primary" style="color:#FFFFFF;font-size:27px"><th align="left" style="width:8%">2.</th><th align="left" colspan="2">Minor Games</th><th align="center">Court</th></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Kabaddi</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Handball</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Kho-Kho</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Ball Badminton</td><td align="center">1</td></tr>
                <tr class="bg-primary" style="color:#FFFFFF;font-size:27px"><th align="left" style="width:8%">3.</th><th align="left" colspan="2">Indoor Games</th><th>&nbsp;</th></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Chess</td><td align="center">5 Boards</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Table Tennis</td><td align="center">1</td></tr>
                <tr><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td><td align="left" style="font-size:24px">Badminton</td><td align="center">1</td></tr>
                <tr class="bg-primary" style="color:#FFFFFF;font-size:27px"><th align="left" style="width:8%">4.</th><th align="left" colspan="2">Athletics</th><th>&nbsp;</th></tr>
                <tr valign="top"><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td>
                <td align="justify" style="font-size:24px" colspan="2">Stadium with Multi-Gym facilities and Galleries. 8 line Track with international measurements and facilities for track and field events.</td>
            </tr>
            <tr class="bg-primary" style="color:#FFFFFF;font-size:27px"><th align="left" style="width:8%">5.</th><th align="left" colspan="2">Indoor Stadium</th><th>&nbsp;</th></tr>
            <tr valign="top"><td align="center">&nbsp;</td><td align="left" style="width:5%;font-size:30px">&raquo;&nbsp;&nbsp;</td>
                <td align="justify" style="font-size:24px" colspan="2">Indoor Stadium with facilities for Basketball, Volleyball, Badminton, Ball Badminton and T.T Courts.</td>
            </tr>
            <tr class="bg-primary" style="color:#FFFFFF;font-size:27px"><th align="left" style="width:8%">6.</th><th align="left" colspan="2">Multi GYM</th><th>&nbsp;</th></tr>
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