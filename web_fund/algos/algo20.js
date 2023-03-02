// 20. Increment the Seconds - Given an array of numbers arr, add 1 to every
// other element, specifically those whose index is odd(arr[1], arr[3],
// arr[5], etc).Afterward, console.log each array value and return arr

function incrementTheSeconds(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (i % 2 != 0) {
            arr[i]++;
        }
    }
    for (var num in arr) {
        console.log(arr[num]);
    }
    return arr
}

var testArr = [8, 6, 7, 5, 3, 0, 9]
console.log(incrementTheSeconds(testArr))