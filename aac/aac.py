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
      margin-top:-20px;
      background-color: darkgray;
    }
    .container-fluid{
        background: linear-gradient(135deg,rgba(0,0,0,0.4)0%,rgba(0,0,0,0.4)25%,rgba(0,23,149,0.6)50%,rgba(255,0,0,0.6)75%,rgba(0,23,149,0.6)100%);
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
                    <img src="./image/arul4.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/arul3.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="./image/arul1.jpg" class="d-block w-100" alt="...">
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
        <center><h4 class="btn" style="background-color:#22ce00;  text-align:left; color: #d54d7b; text-shadow: 0 1px 1px #fff; font-size:25px; font-family: 'Great Vibes', cursive; font-weight: normal;">SPORTS & GAMES</h4></center><br><br>
        <form id="ldc" name="ldc" method="post">
            <table>
                <tr>
                    <td>            	</td>
                </tr>
                <tr><td align="justify">
                    <div class="row">
                        <div class="col-sm-10">
                            <label class="btn" style="background-color:#1B9E98; text-align:left; color:#FFF; font-size:22px">ABOUT AAC SPORTS & GAMES</label><br />
                            <br>                            
                            <p style="font-size:19px">Sports and games is includes in physical, mental, social and spiritual formation of the students through sports and games. In addition to the regular academic activities, the Department formulates and implements the programmes and builds up various teams like Football, Hockey, Volleyball, Basketball, Hand ball, Athletic team etc. The teams participate in the M.K.U “C” Zonal M.K.U Champion Trophy tournaments and open tournaments such as Block, District, State and National level Tournaments and bring laurels to our institution.</p>
                            <p style="font-size:19px">As part of the Curriculum, we have part V Physical Education. Motivation and encouragement are given to the students to opt for part V physical Education.</p>
                            <p style="font-size:19px">The Department renders its services and extends its facilities to local schools and sports clubs to organize tournaments as well as  train their students in sports and games.</p>
                            <p style="font-size:19px">The Department organises state level tournaments in Hockey and Football and Inter Departmental tournaments for the integrated development of the students.</p>
                        </div >
                        <div class="col-sm-2">
                            <div style="color:#13ff01; font-size:16pt; font-weight:bold; background-color:#1f42a7; text-align:centre; vertical-align:middle; height:35px; width:200px; text-shadow: 2px 2px 4px #000000;">Physical Director </div>
                            <br><img src="./image/g4.png" width="170px"/><br>
                            <span style="color:#CC0000; font-size:14pt; font-weight:bold"><a href="../faculty/biodata/10267.pdf" target="_blank"><p> <strong>Dr. Vanitha J.</strong></p></a> </span>
                        </div>
                    </div>
                </tr>
                <tr><td align="justify">
                    <label class="btn" style="background-color:#1B9E98; text-align:left; color:#FFF;font-size:22px">VISION</label><br />
                    <p style="font-size: 19px;">Physical, Mental, Social, and Holistic development of the students through Sports, Games and Yoga.</p> 
                </td></tr>
                <tr><td align="justify">
                    <label class="btn" style="background-color:#1B9E98; text-align:left; color:#FFF;font-size:22px">MISSION</label><br />
                    <p style="font-size:19px; color:#FFF">1.Formulating and implementing programmes aimed at facilitating the personality development of the students through sports, games and yoga.</p>
                    <p style="font-size:19px">2.Formulating programmes aimed at promotion and development of sports in our college. </p>
                    <p style="font-size:19px">3.Formulating programmes and encouraging sports in our college to achieve excellence in sports and establish our college as a leading institution. </p>
                    <p style="font-size:19px">4.To inculcate the traits like, inter human relationship, courtesy, loyalty perseverance, co-operation, understanding, team spirit, sportsmanship and unity among students. </p>
                </td></tr>
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