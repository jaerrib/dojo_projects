// 19. Evens and Odds - Create a function that accepts an array. Every time
// that array has three odd values in a row, print "That's odd!". Every time
// the array has three evens in a row, print "Even more so!"

function evensAndOdds(arr) {
    var evenCount = 0;
    var oddCount = 0;
    for (var i = 0; i < arr.length; i++) {
        if ( arr[i] % 2 != 0) {
            oddCount++;
            evenCount = 0;
            if (oddCount == 3) {
                console.log("That's odd!");
                oddCount = 0;
            }
        }
        if ( arr[i] % 2 == 0 ) {
            evenCount++;
            oddCount = 0;
            if (evenCount == 3) {
                console.log("Even more so!");
                evenCount = 0;
            }
        }
    }
}

var testArr = [1, 3, 7, 2, 8, 4, 3, 5, 10, 11, 17, 15, 18]
evensAndOdds(testArr)