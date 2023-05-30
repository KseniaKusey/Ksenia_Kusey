const header = document.querySelector('.site-header');

function magicSound() {
    const audio = new Audio();
    audio.preload = "auto";
    audio.scr = './sound';
    audio.play();
}
site-header-bg.onklick = magicSound;

document.querySelector('.Winx').orchange = function {
    if (this.checked) {
        header.classList.add('site-header-bg');
    }
    else {
        header.classList.remove('site-header-bg');  
    }
}