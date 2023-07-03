// Remove Blanks
// Create a function that, given a string, returns all of that string’s
// contents, but without blanks.
// If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

function removeBlanks(string) {
    return string.split(" ").join("");
}

console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "))


// Get Digits
// Create a JavaScript function that given a string, returns the integer made
// from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function
// should return the number 1357924680.

function getDigits(string) {
    let tempArr = string.split("")
    let newArr = []
    for (let i = 0; i < tempArr.length; i++) {
        if (Number(!isNaN(tempArr[i]))) {
            newArr.push(tempArr[i]);
        }
    }
    return Number(newArr.join(""))
}

console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"))


// Acronyms
// Create a function that, given a string, returns the string’s acronym
// first letters only, capitalized).
// Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW".
// Given "Live from New York, it's Saturday Night!", return "LFNYISN".

function acronym(string) {
    let tempArr = string.split(" ");
    let newArr = []
    for (let i = 0; i < tempArr.length; i++) {
        newArr.push(tempArr[i][0]);
    }
    return newArr.join("");
}

console.log(acronym(" there's no free lunch - gotta pay yer way. "))
console.log(acronym("Live from New York, it's Saturday Night!"))


// Zip Arrays into Dictionary
// Dictionaries are sometimes called maps because a key (string) maps to a
// value. Given two arrays, create an associative array (map) containing keys
// of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and
// arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

function zipArrays(arr1, arr2) {
    let newDict = {}
    for (let i = 0; i < arr1.length; i++) {
        newDict[arr1[i]] = arr2[i]
    }
    return newDict
}

let arr1 = ["abc", 3, "yo"]
let arr2 = [42, "wassup", true]
let dict = zipArrays(arr1, arr2)
console.log(dict)


// Invert Hash
// Dictionaries are also called hashes (we’ll learn why later). Build
// invertHash(assocArr) to convert hash keys to values, and values to keys.
// Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"},
// return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

function invertHash(dict) {
    let tempDict = {}
    for (key in dict) {
        tempDict[dict[key]] = key;
    }
    return tempDict
}

let myDict = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
console.log(invertHash(myDict))