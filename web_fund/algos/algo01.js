// 1. Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255

function makeArray(num) {
    var arr = []
    for (var i = 0; i <= num; i++) {
        arr[i] = i + 1;
    }
    return arr;
}

console.log(makeArray(255))
