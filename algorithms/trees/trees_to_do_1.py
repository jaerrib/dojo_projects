class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self, root):
        self.root = root

    def add_node(self, data):
        monkey = self.root
        new_node = Node(data)
        while monkey:
            if data > monkey.data:
                if monkey.right:
                    monkey = monkey.right
                else:
                    monkey.right = new_node
                    return self
            else:
                if monkey.left:
                    monkey = monkey.left
                else:
                    monkey.left = new_node
                    return self
        return self

    def contains(self, data):
        monkey = self.root
        new_node = Node(data)
        while monkey:
            if data == monkey.data:
                return True
            else:
                if data > monkey.data:
                    if monkey.right:
                        monkey = monkey.right
                    else:
                        monkey = monkey.left
                else:
                    if monkey.left:
                        monkey = monkey.left
                    else:
                        monkey = monkey.right
        return False

    def min(self):
        queue = [self.root]
        visited = []
        min = self.root.data
        while queue:
            node = queue.pop(0)
            visited.append(node)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        for index in visited:
            if index.data < min:
                min = index.data
        return min

    def max(self):
        queue = [self.root]
        visited = []
        max = self.root.data
        while queue:
            node = queue.pop(0)
            visited.append(node)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        for index in visited:
            if index.data > max:
                max = index.data
        return max

    def size(self):
        queue = [self.root]
        visited = []
        while queue:
            node = queue.pop(0)
            visited.append(node)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        return len(visited)

    def is_empty(self):
        return (not self.root.left and not self.root.right)


new_bst = BST(Node(42))
new_bst.add_node(57).add_node(42).add_node(
    5).add_node(78).add_node(90).add_node(18)

print(new_bst.contains(18))
print("MIN IS", new_bst.min())
print("MAX IS", new_bst.max())
print("SIZE IS", new_bst.size())

bst2 = BST(Node(27))
bst3 = BST(Node(36)).add_node(45)

print(new_bst.is_empty())
print(bst2.is_empty())
print(bst3.is_empty())

# BST: Add
# Create an add(val) method on the BST object to add new value to the tree.
# This entails creating a BTNode with this value and connecting it at the
# appropriate place in the tree. Unless specified otherwise, BSTs can contain
# duplicate values.


# BST: Contains
# Create a contains(val) method on BST that returns whether the tree contains
# a given value. Take advantage of the BST structure to make this a much more
# rapid operation than SList.contains() would be.


# BST: Min
# Create a min() method on the BST class that returns the smallest value found
# in the BST.


# BST: Max
# Create a max() BST method that returns the largest value contained in the
# binary search tree.


# BONUS: BST: Size
# Write a size() method that returns the number of nodes (values) contained in
# the tree.


# BONUS: BST: Is Empty
# Create an isEmpty() method to return whether the BST is empty (whether it
# contains no values).
