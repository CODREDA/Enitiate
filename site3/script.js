function myFunction() {
    document.getElementById("hi").innerHTML = "Hello World";
    var clr = document.getElementById("hi").style.color;
    if(clr == "blue"){
    	document.getElementById("hi").style.color="red";
    }
    else{
    	document.getElementById("hi").style.color="blue";
    }

}