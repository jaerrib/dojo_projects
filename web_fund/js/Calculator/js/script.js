console.log("JS running")

var displayDiv = document.querySelector("#display");
var operation = null;
var num1 = "";
var num2 = "";
var display = 0;

function press(val) {
    if (operation === null) {
        num1 += val;
        display = num1;
    }
    else {
        num2 += val;
        display = num2;
    }
    displayDiv.innerText = display;
}

function setOP(operator) {
    operation = operator;
}

function reset() {
    operation = null;
    num1 = "";
    num2 = "";
}

function clr() {
    displayDiv.innerText = 0;
    reset();
}

function calculate() {
    var result = 0;
    num1 = Number(num1);
    num2 = Number(num2);
    if (operation === "+") {
        result = num1 + num2;
    }
    else if (operation === "-") {
        result = num1 - num2;
    }
    else if (operation === "*") {
        result = num1 * num2;
    }
    else if (operation === "/") {
        result = num1 / num2;
    }
    displayDiv.innerText = result;
    reset();
}