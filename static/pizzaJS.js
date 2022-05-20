
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

/* go to order afer answer thw qution*/
function go(){
    findpizza();
  
    location.href ="file:///C:/Users/User/Desktop/%D7%A9%D7%A0%D7%94%20%D7%92/%D7%A1%D7%99%D7%9E%D7%A1%D7%98%D7%A8%20%D7%91/WEB%20%D7%A4%D7%A8%D7%95%D7%99%D7%A7%D7%98/team3/templates/order.html" ;
    document.getElementById("pizzaChosen").innerHTML = localStorage.getItem("pizza_ty");

    console.log(pizza);
    console.log(pizza_ty);
}


  var count = 0;
  var pizza_ty =localStorage.getItem("pizza");
  
  

  function findpizza(){

if(document.getElementById("Que1").value=="winter"){
    count=count+1;
}
if(document.getElementById("Que1").value=="summer"){
    count=count+2;
}
if(document.getElementById("Que1").value=="Fall"){
    count=count+3;
}
if(document.getElementById("Que1").value=="Spring"){
    count=count+4;
}
if(document.getElementById("Que2").value=="America"){
    count=count+5;
}
if(document.getElementById("Que2").value=="Asia"){
    count=count+6;
}
if(document.getElementById("Que2").value=="Australia"){
    count=count+7;
}
if(document.getElementById("Que2").value=="Europe"){
    count=count+8;
}
if(document.getElementById("Que2").value=="Antarctica"){
    count=count+9;
}
if(document.getElementById("Que3").value=="yes"){
    count=count+10;
}
if(document.getElementById("Que3").value=="no"){
    count=count+11;
}

if(count<=66){
    document.getElementById("type_pizza").innerHTML="crazy pizza" ; 
    localStorage.setItem("pizza", "1");

}

if(count<=40){
    document.getElementById("type_pizza").innerHTML="pizza Mexican" ; 
    localStorage.setItem("pizza", "2");

}

if(count<=20){
document.getElementById("type_pizza").innerHTML="pizza italy";
localStorage.setItem("pizza", "3");
}
  }



function discription(){

    if(document.getElementById("type_pizza").value=="crazy pizza"){
      document.getElementById("descriptionPizza").innerHTML="crazzyyy";
    }
    if(document.getElementById("type_pizza").value=="pizza italy"){
        document.getElementById("descriptionPizza").innerHTML="ITALYYY";
      }
      if(document.getElementById("type_pizza").value=="pizza Mexican"){
        document.getElementById("descriptionPizza").innerHTML="Mexicannnn";
      }
}

function pricePizza(){
    if(document.getElementById("type_pizza").value=="crazy pizza"){
      document.getElementById("pizza_price").innerHTML="90";
    }
    if(document.getElementById("type_pizza").value=="pizza italy"){
        document.getElementById("pizza_price").innerHTML="100";
      }
      if(document.getElementById("type_pizza").value=="pizza Mexican"){
        document.getElementById("pizza_price").innerHTML="80";
      }
}
