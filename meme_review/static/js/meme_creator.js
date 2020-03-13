//https://www.youtube.com/watch?v=aIgWxXlpRvU
let canvas,ctx, uploadedImage, topText, bottomText, createButton;
function createMeme(img, topText, bottomText){
	canvas.width = img.width;
	canvas.height = img.height;
	ctx.clearRect(0,0,canvas.width, canvas.height);
	ctx.drawImage(img,0,0);
	
	let fontSize = canvas.width/18;
	ctx.font = fontSize + 'px Arial Black';
	ctx.fillStyle = "white";
	ctx.strokeStyle = "black";
	ctx.lineWidth = fontSize / 15;
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

function start(){
	canvas = document.getElementById("memeCanvas");
	ctx = canvas.getContext("2d");
	canvas.width = canvas.height = 0;
	topText = document.getElementById("top");
	bottomText = document.getElementById("bottom");
	uploadedImage = document.getElementById("uploadedImage");
	createButton = document.getElementById("create-meme");
	createButton.addEventListener("click", function(){
		let reader = new FileReader();
		reader.onload = function(){
			let img = new Image;
			img.src = reader.result;
			createMeme(img,topText.value,bottomText.value);
		};
		reader.readAsDataURL(uploadedImage.files[0]);
	});

}

start();
