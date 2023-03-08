// 16. Print One, Return Another - Build a function that takes in an array
// of numbers. The function should print the second-to-last value in the
// array, and return the first odd value in the array

function printOneReturnAnother(arr) {
    console.log(arr[arr.length - 2]);
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < 0) {
            return arr[i];
        }
    }
}

console.log(printOneReturnAnother([4, 11, -2, 19, 3, 15]))