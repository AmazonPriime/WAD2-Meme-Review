//https://www.youtube.com/watch?v=aIgWxXlpRvU
let canvas,ctx, uploadedImage, topText, bottomText, createButton, fontSize, fontName, outlineWidth, submitButton;
function createMeme(img, topText, bottomText,fontSize, fontName, outlineWidth){
	canvas.width = img.width;
	canvas.height = img.height;
	ctx.clearRect(0,0,canvas.width, canvas.height);
	ctx.drawImage(img,0,0);
	
	ctx.font = fontSize + 'px '+fontName;
	ctx.fillStyle = "white";
	ctx.strokeStyle = "black";
	ctx.lineWidth = outlineWidth/10;
	ctx.textAlign = "center";
	ctx.textBaseline = "top";
	topText.split("\n").forEach( function(curText,i){
		ctx.fillText(curText, canvas.width/2, i*fontSize, canvas.width);
		ctx.strokeText(curText, canvas.width/2, i*fontSize, canvas.width);
	});
	ctx.textBaseline = "bottom";
	bottomText.split("\n").forEach( function(curText,i){
		ctx.fillText(curText, canvas.width/2, canvas.height-i*fontSize, canvas.width);
		ctx.strokeText(curText, canvas.width/2, canvas.height-i*fontSize, canvas.width);
	});
}

function drawDefaultCanvas(){
	canvas.width = 200;
	canvas.height = 200;
	ctx.clearRect(0,0,200, 200);
	ctx.lineWidth = 10;
	ctx.fillStyle = "white";
	ctx.strokeStyle = "black";
	ctx.rect(0,0,200,200);
	ctx.fill();
	ctx.stroke();
	ctx.strokeStyle = "red";
	ctx.beginPath();
	ctx.moveTo(0,0);
	ctx.lineTo(200,200);
	ctx.stroke();
	ctx.beginPath();
	ctx.moveTo(200,0);
	ctx.lineTo(0,200);
	ctx.stroke();
}

function start(){
	canvas = document.getElementById("memeCanvas");
	ctx = canvas.getContext("2d");
	topText = document.getElementById("top");
	bottomText = document.getElementById("bottom");
	uploadedImage = document.getElementById("uploadedImage");
	fontSize = document.getElementById("fontSize");
	fontName = document.getElementById("fontType");
	outlineWidth = document.getElementById("outlineWidth");
	submitButton = document.getElementById("submitButton");
	submitButton.style.visibility="hidden";
	var el = document.getElementById("output");
	drawDefaultCanvas();
	createButton = document.getElementById("createMeme");
	createButton.addEventListener("click", function(){
		let reader = new FileReader();
		reader.onload = function(){
			let img = new Image;
			img.src = reader.result;
			createMeme(img,topText.value,bottomText.value,fontSize.options[fontSize.selectedIndex].value, fontName.options[fontName.selectedIndex].value, outlineWidth.value);
			submitButton.style.visibility="visible";
		};
		reader.readAsDataURL(uploadedImage.files[0]);
	});

}

start();
