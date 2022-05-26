
 var pizza;


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



  //sign in function
function LogIn() {
    window.alert("Logged in successfully"); 
}


var count = 0;
  


/* go to order afer answer thw qution*/
function go(){
    console.log("ncncnc");
    findpizza();
   location.href ="../templates/order.html" ;
    
}


 
  

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
    pizza=1;
    localStorage.setItem("pizzaCh",pizza);

}

if(count<=40){
   pizza=2;
   localStorage.setItem("pizzaCh",pizza);

}

if(count<=20){
pizza=3;
localStorage.setItem("pizzaCh",pizza);
}
  }



var pizzaForYou=0;
function discription( ){

   
    document.getElementById("step1").disabled=true;

    pizzaForYou=localStorage.getItem("pizzaCh");
    

    if(pizzaForYou=="1"){
        document.getElementById("pizzaChosen").innerHTML="crazy pizza";
      document.getElementById("descriptionPizza").innerHTML="Sweet s'mores pizza";
      document.getElementById("pizza_price").innerHTML="90";
      var img = document.createElement('img');
      img.src ="../static/pizza5.jpg" ;
      document.getElementById("pic").appendChild(img);
    }
    if(pizzaForYou=="2"){
        document.getElementById("pizzaChosen").innerHTML= "pizza Mexican" ; 
        document.getElementById("descriptionPizza").innerHTML="Guacamole, jalapeno and mozzarella pizza";
        document.getElementById("pizza_price").innerHTML="100";
        var img = document.createElement('img');
        img.src ="../static/pizza7.jpg" ;
        document.getElementById("pic").appendChild(img);
      }
      if(pizzaForYou=="3"){
        document.getElementById("pizzaChosen").innerHTML="pizza italy";
        document.getElementById("descriptionPizza").innerHTML="Corn, tomato, bell pepper and olive pizza";
        document.getElementById("pizza_price").innerHTML="110";

        var img = document.createElement('img');
            img.src ="../static/pizza1.png" ;
            document.getElementById("pic").appendChild(img);
    
      }
}

function calPrice(){

    if(document.getElementById("num_pizza").value!==""){

        if(pizzaForYou=="1"){
            document.getElementById("total_price").innerHTML=  document.getElementById("pizza_price").textContent*document.getElementById("num_pizza").value+20 ;
            }
        
            if(pizzaForYou=="2"){
            document.getElementById("total_price").innerHTML= document.getElementById("pizza_price").textContent*document.getElementById("num_pizza").value+20 ;
             } 
        
            if(pizzaForYou=="3"){
             document.getElementById("total_price").innerHTML= document.getElementById("pizza_price").textContent *document.getElementById("num_pizza").value+20 ;
             }

    }
    else{
        window.alert("מלא את מספר הפיצות");
    }
    
  
}

function goToOC(){
    const qty = document.getElementById("num_pizza").value;
    if (qty== ""){
        alert(`please fill out the wanted quantity`);
       }
    else{
        location.href ="../templates/OrderConfirmation.html" ;
    }

}

// When the user clicks -> open the popup


function openPopUp(){ 
    event.preventDefault(); //to prevent the oage reload
    document.getElementById("overlay").style.display = "block";
    document.getElementById("modal").style.display = "block";
}


function closePopUp(){
    location.href ="../templates/home.html" ;
}



// OC page
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth() + 1; //January is 0!
var yyyy = today.getFullYear();

if (dd < 10) {
   dd = '0' + dd;
}

if (mm < 10) {
   mm = '0' + mm;
} 
    
today = yyyy + '-' + mm + '-' + dd;


const curPage = window.location.pathname;
if (curPage.includes("sign%20up.html")){
    document.getElementById("birthdate").setAttribute("max", today); //birthday must be in the past
}
if (curPage.includes("OrderConfirmation.html")){
    document.getElementById("expDate").setAttribute("min", today); //exp. must be in the future
}



