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
</head>

<style>
        /* Importing fonts from Google */
 @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

/* Reseting */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    background: #ecf0f3;
}

.login {
    max-width: 350px;
    min-height: 500px;
    margin: 80px auto;
    padding: 40px 30px 30px 30px;
    background-color: #ecf0f3;
    border-radius: 15px;
    box-shadow: 13px 13px 20px #cbced1, -13px -13px 20px #fff;
}

.logo {
    width: 80px;
    margin: auto;
}

.logo img {
    width: 100%;
    height: 80px;
    object-fit: cover;
    border-radius: 50%;
    box-shadow: 0px 0px 3px #5f5f5f,
        0px 0px 0px 5px #ecf0f3,
        8px 8px 15px #a7aaa7,
        -8px -8px 15px #fff;
}

.login .name {
    font-weight: 600;
    font-size: 1.4rem;
    letter-spacing: 1.3px;
    padding-left: 10px;
    color: #555;
}

.login .form-field input {
    width: 100%;
    display: block;
    border: none;
    outline: none;
    background: none;
    font-size: 1.2rem;
    color: #666;
    padding: 10px 15px 10px 10px;
    /* border: 1px solid red; */
}

.login .form-field {
    padding-left: 10px;
    margin-bottom: 20px;
    border-radius: 20px;
    box-shadow: inset 8px 8px 8px #cbced1, inset -8px -8px 8px #fff;
}

.login .form-field .fas {
    color: #555;
}

.login .btn {
    box-shadow: none;
    width: 100%;
    height: 40px;
    background-color: #03A9F4;
    color: #fff;
    border-radius: 25px;
    box-shadow: 3px 3px 3px #b1b1b1,-3px -3px 3px #fff;
    letter-spacing: 1.3px;
}

.login .btn:hover {
    background-color: #039BE5;
}

.login a {
    text-decoration: none;
    font-size: 0.8rem;
    color: #03A9F4;
}

.login a:hover {
    color: #039BE5;
}

@media(max-width: 380px) {
    .login {
        margin: 30px 20px;
        padding: 40px 15px 15px 15px;
    }
}
</style>
<script>
    var userName,pwd;
    function validate()
    {
        userName=document.forms["login1"]["userName"];
        pwd=document.forms["login1"]["pwd"];
        if(userName.value=="")
        {
            alert("ENTER THE USERNAME");
            userName.focus()
            return false;
        }
        if (pwd.value=="")
        {
            alert("PLEASE ENTER PASSWORD");
            pwd.focus()
            return false;
        }
        
    if(userName.value=="praveen" && pwd.value=="aac")
        {
            alert("LOGIN SUCCESSFUL");
            return true;
        }
    
    else
    {
        alert("INVALID DETAILS");
        return false;
    }
    
        
    }
</script>
<body>
<a href ="./aac.py"> <input type="button" value="Logout" style="float:right;"></a></h1>
    <form action="./volunReg.py" name="login1" onsubmit="return validate()">
    <div class="login">
        <div class="logo">
            <img src="./image/logo.png" alt="">
        </div>
        <div class="text-center mt-4 name">
            SPORTS EVENT
        </div>
        <form class="p-3 mt-3">
            <div class="form-field d-flex align-items-center">
                <span class="far fa-user"></span>
                <input type="text" name="userName" id="userName" placeholder="Username">
            </div>
            <div class="form-field d-flex align-items-center">
                <span class="fas fa-key"></span>
                <input type="password" name="password" id="pwd" placeholder="Password">
            </div>
            <button class="btn mt-3">Login</button>
        </form>
        <div class="text-center fs-6">
            <a href="#">Forget password?</a> or <a href="#">Sign up</a>
        </div>
    </div>
    </form>
</body>
</html>""")