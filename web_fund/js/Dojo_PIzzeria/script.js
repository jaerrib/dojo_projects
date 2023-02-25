function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {}
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

function randomPizza() {
    var crustList = ["hand tossed", "handmade pan", "gluten-free", "Brooklyn style"]
    var sauceList = ["marinara", "honey BBQ", "garlic parmesan", "alfredo", "ranch"]
    var cheeseList = ["mozzarella", "provolone", "cheddar", "feta", "parmesan asiago"]
    var toppingList = ["ham", "beef", "salami", "pepperoni", "sausage", "chicken", "bacon", "Philly steak", "jalapenos", "onions", "banana peppers", "diced tomatoes", "black olives", "pineapple", "green peppers", "spinach", "roasted red peppers"]
    var crustChoice = crustList[Math.floor(Math.random() * crustList.length)]
    var sauceChoice = sauceList[Math.floor(Math.random() * sauceList.length)]
    var cheeseChoice = cheeseList[Math.floor(Math.random() * cheeseList.length)]
    var numToppings = Math.floor(Math.random() * toppingList.length)
    var toppingsChoice = []
    for (var i = 0; i < numToppings; i++) {
        var toppingSelection = toppingList[Math.floor(Math.random() * toppingList.length)]
        toppingsChoice[i] = toppingSelection
    }
    var myPizza = pizzaOven(crustChoice, sauceChoice, cheeseChoice, toppingsChoice)
    return myPizza
}

var p1 = pizzaOven("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"])
var p2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"])
var p3 = pizzaOven("thin crust", "alfredo", "mozzarella", ["chicken", "bacon", "tomatoes"])
var p4 = pizzaOven("gluten-free", "traditonal", "mozzarella", ["pepperono", "sausage", "mushroom"])

console.log(p1)
console.log(p2)
console.log(p3)
console.log(p4)

var p5 = randomPizza()
 
console.log(p5)