// 15. Print Low, Return High - Create a function that takes in an array of
// numbers. The function should print the lowest value in the array, and
// return the highest value in the array

function printLowReturnHigh(arr) {
    var lowVal = arr[0];
    var highVal = arr[0];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < lowVal) {
            lowVal = arr[i];
        }
        if (arr[i] > highVal) {
            highVal = arr[i];
        }
    }
    console.log(lowVal);
    return highVal;
}

console.log(printLowReturnHigh([4, 11, -2, 19, 3, 15]))