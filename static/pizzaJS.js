
function SignUp() {

    //password validation
    const password = document.getElementById("password").value;
    const verifyPassword = document.getElementById("verifyPassword").value;
    // at least one number, one lowercase and one uppercase letter and at least 8 characters
    var valid = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
    if (valid.test(password) == false){
        document.getElementById("errorMessage").innerHTML = "The password must contain at least one number, one lowercase and one uppercase letter";
    }
    else if (password !== verifyPassword){
        document.getElementById("errorMessage").innerHTML = "The passwords does not match";
    }
    else {
        window.alert("Sign up successfully"); 
    }

  }

