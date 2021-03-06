import random
#Code in part by: GeeksForGeeks.com
#Video link of code compiling: https://www.screencast.com/t/buzr5XDf6zB
#search function looks for the 
def search(root,key):

	if root is None or root.val == key:
		return root

	if root.val < key:
		return search(root.right,key)

	return search(root.left,key)

#Constructor for a node class with members key, right, and left.
class Node: 
    def __init__(self, key): 
        self.left = None
        self.right = None
        self.key = key 
  
# A utility function to insert  
# a new node with the given key 
  
#insert function adds nodes to a tree. If the node is None, we return a new node with the input key value to add it to the tree. If node is not None, then we recurse down either
#the left or right nodes, depending on the value of the input key.
def insert(node, key): 
    if node is None: 
        return Node(key) 
    else: 
        if key < node.key:
            node.left = insert(node.left, key)
        else:
            node.right = insert(node.right, key)
    return node

#This function recurses down left nodes, to find the smallest value in a tree.
def minValueNode(node):
    current = node
    
    while (current.left is not None):
        current = current.left
   
    return current
 
#This function recurses down left or right nodes to find the node with the value equal to the input key.
#Upon finally reaching a node with an equal value, it then checks to see if it has children. If it has one, it saves the old value into a temp variable, sets the root
#equal to None, then returns the temp value. If it has two children, it looks for the minimum value in the right node of that tree, and uses that value to swap with the deleting
#node, then does not return the old node value.
def deleteNode(root, key):
    if root is None:
        return root
        
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

# A utility function to do inorder tree traversal 
#Recurses down the left tree to find the smallest values first, printing key values when it gets to the bottom. When it gets to a node with no children, 
#"Leaf Node" is printed before the value, denoting it as per requirement guidelines. After going through the left subtree, it then recurses through the right
#subtree, printing those values as well.
def inorder(root): 
    if root: 
        inorder(root.left)
        if root.left is None and root.right is None:
            leafNodes.append(root.key)
            print("Leaf node: ", end='')
        print(root.key) 
        inorder(root.right) 
  
#generates random numbers to be potentially added. The numbers will only be added as long as they are not in a list that holds all of the values for checking, or if they equal
#the root node value. This is all in part to assure that numbers are unique. Upon adding a number to the bst, "i" increments, getting ever so closer to breaking the while loop
#and continuting with the program.
def generate20(root):
    i = 0
    j = 19
   
    print("The random numbers generated are, in order:")
    while (i < j):
        generatedVal = random.randrange(1, 100)
        if generatedVal not in generatedList and generatedVal is not root.key:          
            generatedList.append(generatedVal)
            insert(r, generatedVal)
            #print(random.randrange(1,100))
            i += 1



   


#generatedList holds all values generated by generate20
generatedList = []
#Holds all nodes that become leaf nodes, for clarification during delete operation
leafNodes = []

#Randomly generates the first key value, to create the tree.
firstVal = random.randrange(1,100)

#Creates the root of the tree.
r = Node(firstVal) 
generate20(r)

print("Root Node:" , firstVal)

print("Nodes added to the bst are: ", generatedList)


  
# Print inoder traversal of the BST 
print("Inorder traversal")
inorder(r) 
print("Print childNodes: ", leafNodes)

#Takes user input to choose a node that is not a leaf node. Since using input() for the user to choose a node returns a string, we must type cast it into an int.
#The program then deletes the node.
deletedVal = int(input("Enter a number that is not a leaf node, but is in the generated list: "))
deleteNode(r, deletedVal)

print("Inorder traversal after root is deleted")
inorder(r)


#This part of the script generates one last unique number to be added to the bst.
u = 0
while (u < 1):
    rv2 = random.randrange(1,100)
    if rv2 not in generatedList and rv2 not in leafNodes:
        u += 1
    else:
        rv2 = random.randrange(1,100)
 
print("The new generated number is: ", rv2)
insert(r, rv2)

print("Traversal after adding new random number:")
inorder(r)


