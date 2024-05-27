class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

# return true if a tree is empty, return false otherwise. 
    def isEmpty(self):
        return self.root is None

# clear a tree.
    def clear(self):
        self.root = None

# Search a node having value x.
    def search(self, x):
        current = self.root
        while current:
            if current.value == x:
                return current
            elif x < current.value:
                current = current.left
            else:
                current = current.right
        return None

# check if the key x does not exists in a tree then insert new node with value x into the tree. 
    def insert(self, x):
        if self.isEmpty():
            self.root = Node(x)
            return

        parent = None
        current = self.root
        while current:
            parent = current
            if x < current.value:
                current = current.left
            else:
                current = current.right

        if x < parent.value:
            parent.left = Node(x)
        else:
            parent.right = Node(x)

# traverse a tree. (level order)
    def breadth(self):
        if self.isEmpty():
            return

        queue = []
        queue.append(self.root)
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()  

# recursive preorder traverse of a tree.
    def preorder(self, p):
        if p:
            print(p.value, end=" ")
            self.preorder(p.left)
            self.preorder(p.right)

# recursive inorder traverse of a tree.
    def inorder(self, p):
        if p:
            self.inorder(p.left)
            print(p.value, end=" ")
            self.inorder(p.right)

# recursive postorder traverse of a tree. 
    def postorder(self, p):
        if p:
            self.postorder(p.left)
            self.postorder(p.right)
            print(p.value, end=" ")
            
# count and return number of nodes in the tree. 
    def count(self):
        if self.isEmpty():
            return 0

        def _count_nodes(node):
            if not node:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)

        return _count_nodes(self.root)

# delete a node having value x. 
    def dele(self, x):
        if self.isEmpty():
            return

        def _find_min(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete_node(node, value):
            if not node:
                return node

            if value < node.value:
                node.left = _delete_node(node.left, value)
            elif value > node.value:
                node.right = _delete_node(node.right, value)
            else:  
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    return temp

                temp = _find_min(node.right)
                node.value = temp.value
                node.right = _delete_node(node.right, temp.value)

            return node

        self.root = _delete_node(self.root, x)

# find and return the node with minimum value in the tree.
    def Min(self):
        if self.isEmpty():
            return None

        current = self.root
        while current.left:
            current = current.left
        return current

# find and return the node with maximum value in the tree.
    def Max(self):
        if self.isEmpty():
            return None

        current = self.root
        while current.right:
            current = current.right
        return current

# return the sum of all values in the tree.
    def Sum(self):
        if self.isEmpty():
            return 0

        def _sum_values(node):
            if not node:
                return 0
            return node.value + _sum_values(node)

# return the average of all values in the tree.
    def avg(self):
        if self.isEmpty():
            return None  

        def _sum_values(node):
            if not node:
                return 0
            return node.value + _sum_values(node.left) + _sum_values(node.right)

        total_sum = _sum_values(self.root)
        node_count = self.count()

        if node_count == 0:
            return None  

        return total_sum/node_count

# height of a binary tree.
    def height(self):
        if self.isEmpty():
            return -1  

        def _get_height(node):
            if not node:
                return -1  
            return 1 + max(_get_height(node.left), _get_height(node.right))

        return _get_height(self.root)

# the cost of the most expensive path from the root to a leaf node.
    def most_expensive_path_cost(self):
        if self.isEmpty():
            return None  

        def _find_max_cost(node, current_cost):
            if not node:
                return current_cost  

            current_cost += node.value

            left_cost = _find_max_cost(node.left, current_cost)
            right_cost = _find_max_cost(node.right, current_cost)

            return max(left_cost, right_cost)

        return _find_max_cost(self.root, 0)  

# determine whether a given binary tree is AVL or not.
    def is_avl(self):
        if self.isEmpty():
            return True  

        def _check_balance(node):
            if not node:
                return 0 

            left_height = _check_balance(node.left)
            right_height = _check_balance(node.right)

            balance = abs(left_height - right_height)
            if balance > 1:
                return float('inf')  

            return 1 + max(left_height, right_height)  
        balance = _check_balance(self.root)
        return balance != float('inf')

# determine whether a given binary tree is a heap
    def is_heap(self):
        if self.isEmpty():
            return True  

        def _check_heap_property(node, parent_value):
            if not node:
                return True

            if node.value < parent_value:
                return False

            return _check_heap_property(node.left, node.value) and _check_heap_property(node.right, node.value)

        return _check_heap_property(self.root, float('-inf'))  



#Driver code

tree = BinarySearchTree()
tree.insert(4)
tree.insert(3)
tree.insert(1)
tree.insert(11)
tree.insert(5)
tree.insert(9)
tree.insert(2)
tree.insert(6)
tree.insert(15)
tree.insert(12)

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
print()
tree.breadth()
tree.count()
print(tree.height())
tree.dele(2)
tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)
print()
print(tree.count())
print(tree.isEmpty())
print(tree.avg())
print(tree.height())
print(tree.most_expensive_path_cost())
print(tree.is_avl())
print(tree.is_heap())
