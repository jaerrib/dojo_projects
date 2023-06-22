console.log("Javascript is connected")

let banner = document.querySelector("#cookie_banner")
let today_high = document.querySelector("#today_high")
let today_low = document.querySelector("#today_low")
let tomorrow_high = document.querySelector("#tomorrow_high")
let tomorrow_low = document.querySelector("#tomorrow_low")
let fri_high = document.querySelector("#fri_high")
let fri_low = document.querySelector("#fri_low")
let sat_high = document.querySelector("#sat_high")
let sat_low = document.querySelector("#sat_low")


let tempC = [24, 18, 27, 19, 21, 16, 26, 21]
let tempF = [75, 65, 80, 66, 69, 61, 78, 70]

function loadReport() {
    alert("Loading weather report...")
}

function hide() {
    banner.remove();
}

function recalcTemps(val) {
    let newTemps = []
    console.log("Recalculating in "+val)
    if(val == "C") {
        newTemps = tempC;
    }
    if(val == "F") {
        newTemps = tempF;
    }
    today_high.innerText = newTemps[0];
    today_low.innerText = newTemps[1];
    tomorrow_high.innerText = newTemps[2];
    tomorrow_low.innerText = newTemps[3];
    fri_high.innerText = newTemps[4];
    fri_low.innerText = newTemps[5]
    sat_high.innerText = newTemps[6];
    sat_low.innerText = newTemps[7]
}