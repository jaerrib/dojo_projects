// 26. Swap Toward the Center - Given an array, swap the first and last
// values, third and third-to-last values, etc.  Example:
// swapTowardCenter([true,42,"Ada",2,"pizza"]) turns the array into
// ["pizza", 42, "Ada", 2, true].  swapTowardCenter([1,2,3,4,5,6]) turns
// the array into [6,2,4,3,5,1].  No need to return the array this time

function swapTowardCenter(arr) {
    var midpoint = Math.ceil(arr.length / 2)
    for (var i = 0; i < midpoint; i++) {
        if (i % 2 == 0) {
            var swapPos = arr.length - i - 1;
            var tempVal = arr[i];
            arr[i] = arr[swapPos];
            arr[swapPos] = tempVal;
        }
    }
    console.log(arr)
}


swapTowardCenter([true,42,"Ada",2,"pizza"])
swapTowardCenter([1,2,3,4,5,6])