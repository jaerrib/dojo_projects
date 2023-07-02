// 1. Countdown
// Create a function that accepts a number as an input. Return a new array
// that counts down by one, from the number (as array’s ‘zeroth’ element)
// down to 0 (as the last element). How long is this array?

function countdown(num) {
    let tempArr = []
    for (let i = num; i >= 0; i--) {
        tempArr.push(i)
    }
    console.log("The length of the array is " + tempArr.length)
    return tempArr
}

console.log(countdown(5))

// 2. First Plus Length
// Given an array, return the sum of the first value in the array, plus the
// array’s length. What happens if the array’s first value is not a number,
// but a string (like "what?") or a boolean (like false).

function firstPlusLength(arr) {
    return arr[0] + arr.length
}

console.log(firstPlusLength([1, 2, 3, 4]))
console.log(firstPlusLength(["what?", 2, 3, 4]))
console.log(firstPlusLength([false, 1, 1, 1, 1]))

// 3. Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2nd value.
// Return how many values this is.

function valuesGreaterThanSecond(arr) {
    let accum = 0
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > arr[1]) {
            console.log(arr[i] + " is greater than " + arr[1])
            accum++
        }
    }
    return accum
}

console.log("Total is " + valuesGreaterThanSecond([1, 3, 5, 7, 9, 13]))

// 4. Values Greater than Second, Generalized
// Write a function that accepts any array, and returns a new array with the
// array values that are greater than its 2nd value. Print how many values
// this is. What will you do if the array is only one element long?

function valuesGreaterThanSecondGen(arr) {
    let accum = 0
    if (arr.length == 1) {
        accum++
    }
    else {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] > arr[1]) {
                accum++
            }
        }
    }
    return accum
}

valuesGreaterThanSecondGen([1, 3, 5, 7, 9, 13])
valuesGreaterThanSecondGen([1])

// 5. This Length, That Value
// Given two numbers, return array of length num1 with each value num2.
// Print "Jinx!" if they are same.

function thisLengthThatValue(num1, num2) {
    if (num1 == num2) {
        console.log("Jinx!")
    }
    else {
        tempArr = []
        for (let i = 0; i < num1; i++) {
            tempArr.push(num2)
        }
        return tempArr
    }
}

thisLengthThatValue(3, 3)
newArr = thisLengthThatValue(3, 2)
console.log(newArr)

// 6. Fit the First Value
// Your function should accept an array. If value at [0] is greater than
// array’s length, print "Too big!"; if value at [0] is less than array’s
// length, print "Too small!"; otherwise print "Just right!".

function fitTheFirstValue(arr) {
    if (arr[0] > arr.length) {
        console.log("Too big!")
    }
    else if (arr[0] < arr.length) {
        console.log("Too small!")
    }
    else {
        console.log("Just right!")
    }
}

fitTheFirstValue([5, 3, 1])
fitTheFirstValue([2, 3, 1])
fitTheFirstValue([3, 3, 1])

// 7. Fahrenheit to Celsius
// Kelvin wants to convert between temperature scales. Create
// fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit
// and returns the equivalent temperature as expressed in Celsius degrees. For
// review, Fahrenheit = (9/5 * Celsius) + 32.

function fahrenheitToCelsius(fDegrees) {
    return (fDegrees - 32) / (9 / 5)
}

console.log(fahrenheitToCelsius(212))
console.log(fahrenheitToCelsius(32))
console.log(fahrenheitToCelsius(80))
