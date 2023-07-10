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

    // Front
    // Write a method to return the value (not the node) at the head of the list.
    // If the list is empty, return null.

    front() {
        if (!this.head) {
            return null;
        }
        return this.head.data;
    }

    // Add Front
    // Write a method that accepts a value and create a new node, assign it to the
    // list head, and return a pointer to the new head node.
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

    // Remove Front
    // Write a method to remove the head node and return the new list head node.
    // If the list is empty, return null.

    removeFront() {
        if (!this.head) {
            return null;
        }
        this.head = this.head.next;
        return this;
    }

    // Bonus
    // Add to Back
    // Write a method that accepts a value and create a new node, assign it to the
    // end of the listFront

}

myList = new SLL();
console.log("front is", myList.front())
myList.addFront(1);
myList.addFront(2);
myList.addFront(3);
myList.addFront(4);
console.log(myList);
myList.removeFront();
console.log(myList);
console.log("front is", myList.front())

