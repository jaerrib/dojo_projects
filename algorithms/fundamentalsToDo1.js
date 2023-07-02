// 1. Multiples of Three – but Not All
// Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

function multiplesOf3() {
    for (let i = -300; i <= 0; i+=3) {
        if (i !== -3 && i !== -6) {
            console.log(i)
        }
    }
}

multiplesOf3()


// 2. Printing Integers with While
// Print integers from 2000 to 5280, using a WHILE.

function intWithWhile() {
    let i = 2000;
    while (i <= 5280) {
        console.log(i);
        i++;
    }
}

intWithWhile()

// 3. Counting, the Dojo Way
// Print integers 1 to 100. If divisible by 5, print "Coding" instead.
// If by 10, also print " Dojo".

function countingDojo() {
    for (let i = 1; i <= 100; i++) {
        if (i % 10 === 0) {
            console.log("Dojo")
        } else if (i % 5 === 0) {
            console.log("Coding")
        } else {
            console.log(i)
        }
    }
}

countingDojo()

// 4. Flexible Countdown
// Given lowNum, highNum, mult, print multiples of mult from highNum down
// to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).

function flexCount(lowNum, highNum, mult) {
    console.log(lowNum, highNum, mult)
    for (let i = highNum; i >= lowNum; i--) {
        if (i % mult === 0) {
            console.log(i)
        }
    }
}

flexCount(2, 9 , 3)
