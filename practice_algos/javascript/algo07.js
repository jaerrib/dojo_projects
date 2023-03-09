// 7. Array odd - Write a function that would return an array of all the odd
// numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method

function arrayOdd(rr) {
    arr = [];
    for (var i = 1; i < 50; i++) {
        if (i % 2 != 0) {
            arr.push(i)
        }
    }
    return arr
}

console.log(arrayOdd())