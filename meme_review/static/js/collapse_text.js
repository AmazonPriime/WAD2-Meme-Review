var collapseButton = document.getElementById("collapseButton");
var collapseImg = document.getElementById("collapseImg");
var expandImg = document.getElementById("expandImg");
collapseImg.style.display = "none";//hide by default, one arrow must be visible
var clicked = false;
collapseButton.addEventListener("click",function(){
	//do rotation
	collapseButton.classList.remove("rotate-arrow");
	void collapseButton.offsetWidth;
	collapseButton.classList.add("rotate-arrow");
	//manage which of the images is visible
	if(clicked==true){
		collapseImg.style.display = "block";
		expandImg.style.display = "none";
	}else{
		expandImg.style.display = "block";
		collapseImg.style.display = "none";
	}
	clicked = !clicked;
});