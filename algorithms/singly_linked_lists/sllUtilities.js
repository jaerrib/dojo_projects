// SLL Utilities

class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    addFront(val) {
        let new_node = new Node(val);
        if (!this.head) {
            this.head = new_node;
            return this;
        }
        new_node.next = this.head
        this.head = new_node;
        return this.head.data;
    }


    // Add a method contains(value) to your SLL class, which is given a value
    // as a parameter.  Return a boolean (true/false); true, if the list
    // possesses a node that contains the provided value.

    contains(value) {
        // is "value" to be found anywhere in this list?
        let runner = this.head
        while (runner !== null) {
            //Since the runner is set to the current node, its value will be equal to the value of the node they                 are currently on
            if (runner.data == value) {
                return true
            }
            //Tell our attendant to move to the next car
            runner = runner.next
        }
        return false
    }


    // Length
    //  Create a new SLL method length() that returns number of nodes in that list.


    length() {
        // how many nodes are in my list?
        let runner = this.head
        let sum = 0
        while (runner !== null) {
            //Since the runner is set to the current node, its value will be equal to the value of the node they                 are currently on
            sum += 1
            //Tell our attendant to move to the next car
            runner = runner.next
        }
        return sum
    }



    // Display
    // Create display() that returns a string containing all list values.
    // Build what you wish console.log(myList) did!


    display() {
        // neatly display nodes in my list
        let runner = this.head
        let nodeList = []
        while (runner !== null) {
            //Since the runner is set to the current node, its value will be
            // equal to the value of the node they are currently on
            nodeList.push(runner.data)
            //Tell our attendant to move to the next car
            runner = runner.next
        }
        return nodeList
    }
}

myList = new SLL();
myList.addFront(1);
myList.addFront(2);
myList.addFront(3);
myList.addFront(4);
console.log("The length of the list is", myList.length())
console.log(myList.contains(5))
console.log(myList.contains(3))
console.log(myList.display())