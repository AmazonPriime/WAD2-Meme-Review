var collapseButton = document.getElementById("collapseButton");
var expand = "Expand";
var collapse= "Collapse";
collapseButton.textContent=expand; //Initially it is not expanded so set text to expand
collapseButton.addEventListener("click",function(){
	if(collapseButton.textContent==collapse){
		collapseButton.textContent=expand;
	}else{
		collapseButton.textContent=collapse;
	}
	
});