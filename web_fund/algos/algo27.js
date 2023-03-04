// 27. Scale the Array - Given an array arr and a number num, multiply
// all values in the array arr by the number num, and return the changed
// array arr.  For example, scaleArray([1,2,3], 3) should return [3,6,9]

function scaleArray(arr, num) {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i] * num;
    }
    return arr
}

console.log(scaleArray([1,2,3], 3))