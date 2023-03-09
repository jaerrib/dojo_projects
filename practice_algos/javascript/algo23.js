// 23. Reverse Array - Given an array, write a function that reverses its
// values, in-place. Example: reverse([3,1,6,4,2]) returns the same array,
// but now contains values reversed like so... [2,4,6,1,3]. Do this without
// creating an empty temporary array.  (Hint: you'll need to swap values)

function reverse(arr) {
    for (var i = 0; i < arr.length / 2; i++) {
        var temp = arr[i];
        arr[i] = arr[arr.length - (i + 1)]
        arr[arr.length - (i + 1)] = temp
    }
    return arr
}

console.log(reverse([3,1,6,4,2]))