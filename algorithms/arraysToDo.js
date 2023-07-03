// Shuffle
// In JavaScript, the Array object has numerous useful methods. It does not,
// however, contain a method that will randomize the order of an array’s
// elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s
// values. Work in-place, naturally. Do you need to return anything from your
// function?

function shuffle(arr) {
    for (let idx = arr.length - 1; idx > 0; idx--) {
        randIdx = Math.floor(Math.random() * idx);
        [arr[idx], arr[randIdx]] = [arr[randIdx], arr[idx]];
    }
    return arr;
}

console.log(shuffle([1, 2, 3, 4, 5]))


// Skyline Heights
// Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s
// say you are given an array with heights of consecutive buildings, starting
// closest to you and extending away. Array [-1,7,3] would represent three
// buildings: first is actually out of view below street level, behind it is
// second at 7 stories high, third is 3 stories high (hidden behind the 7-story).
// You are situated at street level. Return array containing heights of buildings
// you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4].
// As always with challenges, do not use built-in array functions such as unshift().

function skyline(arr) {
    let tempArr = []
    let tempVal = null
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > 0 && arr[i] > tempVal) {
            tempArr.push(arr[i])
        }
        if (arr[i] > tempVal) {
            tempVal = arr[i]
        }
    }
    return tempArr
}

console.log(skyline([-1, 1, 1, 7, 3]))
console.log(skyline([0, 4]))

function zipIt(arr1, arr2) {
    let newArr = arr1.concat(arr2)
    for (let mainIdx = 0; mainIdx < newArr.length; mainIdx++) {
        for (let idx = 1; idx < newArr.length; idx++) {
            if (newArr[idx] < newArr[idx - 1]) {
                [newArr[idx], newArr[idx - 1]] =
                    [newArr[idx - 1], newArr[idx]];
            }
        }
    }
    return newArr
}

console.log(zipIt([4, 15, 100], [10, 20, 30, 40]))



// Credit Card Validation (Bonus)
// The Luhn formula is sometimes used to validate credit card numbers. Create
// the function isCreditCardValid(digitArr) that accepts an array of digits on
// the card (13-19 depending on the card), and returns a boolean whether the card
// digits satisfy the Luhn formula, as follows:

//     Set aside the last digit; do not include it in these calculations (until step 5);
//     Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
//     If any results are larger than 9, subtract 9 from them;
//     Add all numbers (not just our odds) together;
//     Now add the last digit back in – the sum should be a multiple of 10.

// For example, when given digit array [5,2,2,8,2], after step 1) it becomes
// [5,2,2,8], then after step 2) it is [5,4,2,16]. Post-3) we have [5,4,2,7],
// then following 4) it becomes 18. After step 5) our value is 20, so ultimately we
// return true. If the final digit were any non-multiple-of-10, we would instead
// return false.

function isCreditCardValid(arr) {
    tempArr = arr;
    lastDigit = tempArr.pop();
    for (let idx = tempArr.length - 1; idx > 0; idx--) {
        if (idx % 2 == 0) {
            tempArr[idx] *= 2;
            if (tempArr[idx] > 9) {
                tempArr[idx] -= 9;
            }
        }
    }
    tempArr.push(lastDigit);
    accum = 0;
    for (let idx = 0; idx < tempArr.length; idx++) {
        accum = +tempArr[idx];
    }
    return accum % 2 == 0;
}

console.log(isCreditCardValid([5, 2, 2, 8, 0]))