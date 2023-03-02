// 18. Count Positives - Given an array of numbers, create a function to
// replace the last value with the number of positive values found in the
// array.  Example, countPositives([-1,1,1,1]) changes the original array
// to [-1,1,1,3] and returns it

function countPositives(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > 0) {
            sum++;
        }
    }
    arr.push(sum);
    return arr
}

console.log(countPositives([-1,1,1,1]))