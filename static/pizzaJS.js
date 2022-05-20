
//function for signing up. checks the validation of the password
function SignUp() {
    const password = document.getElementById("password").value;
    const verifyPassword = document.getElementById("verifyPassword").value;

    //password validation: at least one number, one lowercase and one uppercase letter and at least 8 characters
    var valid = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;

    if (valid.test(password) == false){
        document.getElementById("errorMessage").innerHTML = "The password must contain at least one number, one lowercase and one uppercase letter";
    }
    else if (password !== verifyPassword){
        document.getElementById("errorMessage").innerHTML = "The passwords does not match";
    }
    else{
        document.getElementById("errorMessage").innerHTML = "";
        window.alert("Sign up successfully"); 
    }
  }

