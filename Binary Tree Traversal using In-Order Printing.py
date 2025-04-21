"""
Title: Binary Tree Traversal using In-Order Printing
Name: shokomori
"""

# Define the Node class for the binary tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # In-order traversal to print nodes
    def Print_Tree(self):
        if self.left:
            self.left.Print_Tree()
        print(self.data, end=' ')
        if self.right:
            self.right.Print_Tree()

# Construct the first binary tree with the letters: M, A, S, A, T, O (Masato)
root = Node('M')
root.left = Node('A')
root.right = Node('S')
root.left.left = Node('A')
root.left.right = Node('T')
root.right.left = Node('O')

# Construct the second binary tree with the letters: M, A, R, T, I, N (Martin)
root2 = Node('M')
root2.left = Node('A')
root2.right = Node('R')
root2.left.right = Node('T')
root2.right.right = Node('I')
root2.right.right.right = Node('N')

# Display in-order traversal of both trees
print("First Binary Tree (Masato):")
root.Print_Tree()
print("\n")

print("Second Binary Tree (Martin):")
root2.Print_Tree()
print("\n")
