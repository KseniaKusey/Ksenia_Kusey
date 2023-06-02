var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

var bird = new Image();
var bg = new Image();
var fg = new Image();
var pipeUp = new Image();
var pipeBottom = new Image();

bird.scr = "picture/bird.png";
bg.scr = "picture/bg.png";
fg.scr = "picture/fg.png";
pipeUp.scr = "picture/pipeUp.png";
pipeBottom.scr = "picture/pipeBottom.png";

var gap = 90;

//клик на любую кнопку
document.addEventListener("keydown", moveUp);

function moveUp() {
    yPos -= 25;
}

//блоки
var pipe = [];
pipe[0] = {
    x : cvs.clientWidth,
    y : 0
}
var score = 0;

//птичка
var xPos = 10;
var yPos = 150;
var grav = 1.5;

function draw() {
    ctx.drawImage(bg, 0, 0);
    
    for(var i = 0; i < pipe.length; i++) {
        ctx.drawImage(pipeUp, pipe[i].x, pipe[i].y);
        ctx.drawImage(pipeBotton, pipe[i].x, pipe[i].y + pipeUp.height + gap);

        pipe[i].x--;

        if(pipe[i].x == 125) {
            pipe.push({
                x : cvs.clientWidth,
                y : Math.floor(Math.random() * pipeUp.height) - pipeUp.height
            });
        }
    
    }
    
    if(xPos + bird.width >= pipe[i].x
        && xPos <= pipe[i]/x + pipeUp.width
        && (yPos <= pipe[i].y + pipeUp.height
            || yPos + bird.height >= pipe[i].y + pipeUp.height + gap) || yPos + bird.height >= cvs.height - fg.height) {
                location.reload();
            }

        if(pipe[i].x == 5) {
            score++;
        }


    ctx.drawImage(fg, 0, cvs.height - fg.height);
    ctx.drawImage(bird, 10, 150);

    yPos += grav;

    ctx.fillStyle = "#000";
    ctx.font = "24px Verdana";
    ctx.fillText("Счет:" + score, 10, cvs.height - 20);
    requestAnimationFrame(draw);
}

pipeBotton.onload = draw;