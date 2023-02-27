// 9. Squares - Given an array with multiple values, write a function that
// replaces each value in the array with the value squared by itself.
// (e.g. [1,5,10,-2] will become [1,25,100,4])

function squares(arr) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i] ** 2;
    }
    return arr;
}

console.log(squares([1,5,10,-2]))