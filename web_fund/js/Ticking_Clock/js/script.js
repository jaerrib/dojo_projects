const minutes = document.querySelector("#minutes")
const seconds = document.querySelector("#seconds")
const hour = document.querySelector("#hour")
let sec = 0
let min = 0
let hr = 0


function getSecondsSinceStartOfDay() {
    let sec =  new Date().getSeconds();
    var min = new Date().getMinutes();
    let hrs = new Date().getHours();
    return [hrs, min, sec]
}


setInterval(function () {
    let time = getSecondsSinceStartOfDay();
    let hrs_deg = (time[0] * 30) + 180;
    let min_deg = (time[1] * 6) + 180;
    let sec_deg = (time[2] * 6) + 180;
    seconds.style.transform = 'rotate('+sec_deg+'deg)';
    minutes.style.transform = 'rotate('+min_deg+'deg)';
    hour.style.transform = 'rotate('+hrs_deg+'deg)';
}, 1000);
