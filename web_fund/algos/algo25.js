// 25. Always Hungry - Create a function that accepts an array, and prints
// "yummy" each time one of the values is equal to "food".  If no array
// values are "food", then print "I'm hungry" once

function alwaysHungry(arr) {
    count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == "food") {
            console.log("yummy");
            count++
        }
    }
    if (count == 0) {
        console.log("I'm hungry")
    }
}

alwaysHungry([1, 3, "food", 5, "food", "cat", 2, "food"])
alwaysHungry([1, 3, -9, "cat", 0, "dog"])