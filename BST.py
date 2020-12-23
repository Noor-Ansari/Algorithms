# To create a new node
class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None

# To insert any new node in the BST
def insertion(root,data):
    if root == None:
        root = Node(data)
    elif data<=root.data:
        root.left = insertion(root.left,data)
    else:
        root.right = insertion(root.right,data)
    return root

# To search any element in the BST
def search(root,data):
    if root==None:
        return False
    elif data==root.data:
        return True
    elif data<root.data:
        return search(root.left,data)
    else:
        return search(root.right,data) 

# Inorder traversal of the BST    
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data)
        in_order(root.right)

# To find the min value in the BST
def min_value(root):
    current = root
    while current.left !=None:
        current  = current.left
    return current.data

# To find the max value in the BST
def max_value(root):
    current = root 
    while current.right !=None:
        current = current.right 
    return current.data

def deletion(root,data):
    if root==None:
        return root
    if root.data>data:
        root.left = deletion(root.left,data)
        return root
    elif root.data<data:
        root.right = deletion(root.right,data)
        return root

    # Now we have reach at the node to be deleted

    # Now let's delete those cases where root has only one child
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp 
        elif root.right is None:
            temp = root.left 
            root = None 
            return temp 

    # If both children exists then find the min of the right subtree
        temp = min_value(root.right)
    # Then copy min of right at the root postion 
        root.data = temp 
    # Now delete the repetated element from the right subtree
        root.right = deletion(root.right,temp)
    return root


root = None
root = insertion(root,18)
root = insertion(root,21)
root = insertion(root,10)
root = insertion(root,20)
root = insertion(root,7)
root = insertion(root,11)

#in_order(root)

result = search(root,10)

if result:
    print("Item found!!!!")
else:
    print("Not found!!!!")

print("Minimum element is :-",min_value(root))

print("Maximum element is :-",max_value(root))

print("In_order traversal of the tree before deletion")
in_order(root)

print("In_order traversal of the tree after deletion")
deletion(root,10)
in_order(root)








