function change(){
	var image = document.getElementById("1").src;
	//console.log(document.getElementById("1").src);
	console.log(image);
	 if (image == "file:///C:/Users/student/Desktop/site2/1.jpg")
        {
        console.log('true');
		document.getElementById("1").src = "2.jpg";
        }
    else {
    	console.log('false');
        document.getElementById("1").src = "1.jpg";
        }

        
}
