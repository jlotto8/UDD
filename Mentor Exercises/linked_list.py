class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


# Insertion at Beginning in Linked List 
# Create a new_node with the given data and check if the head is an empty node or not if the head is empty then we make the new_node as head and return 
# else insert the head at the next new_node and make the head equal to new_node.

def insertAtBegin(self, data):
    new_node = Node(data)
    if self.head is None: #None meaning empty list
        self.head = new_node
        return
    else:
        new_node.next = self.head
        self.head = new_node


#Insertion in Linked List at End
# Create a new_node with the given data and check if the head is an empty node or not if the head is empty then we make the new_node as head and return 
# else make a current_node equal to the head traverse to the last node of the linked list and when we get None after the current_node the while loop breaks and insert the new_node in the next of current_node which is the last node of linked list.

def inserAtEnd(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return
 
    current_node = self.head
    while(current_node.next):
        current_node = current_node.next
 
    current_node.next = new_node

#Insert a Node at a Specific Position in a Linked List
#  Create a new_node with given data, a current_node that equals to the head, and a counter ‘position’ initializes with 0. Now, if the index is equal to zero it means the node is to be inserted at begining so we called insertAtBegin() method, 
# else: run a while loop until the current_node is not equal to None or (position+1) is not equal to the index at the one position back to insert at a given position to make the linking of nodes and in each iteration, we increment the position by 1 and make the current_node next of it. When the loop breaks and if current_node is not equal to None we insert new_node at after to the current_node. If current_node is equal to None it means that the index is not present in the list and we print “Index not present”.

def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
 
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")


# #Update the Node of a Linked List
# This code defines a method called updateNode in a linked list class. It is used to update the value of a node at a given position in the linked list.
def updateNode(self, val, index):
    current_node = self.head
    position = 0
    if position == index:
        current_node.data = val
    else:
        while(current_node != None and position != index):
            position = position+1
            current_node = current_node.next
        if current_node != None:
            current_node.data = val
        else:
            print("Index not present")

# Remove First Node from Linked List
# removes the first node of the linked list simply by making the second node head of the linked list.

def remove_first_node(self):
    if(self.head == None):
        return
     
    self.head = self.head.next

#Remove Last Node from Linked List
# First, traverse to the second last node using the while loop, and then make the next of that node None and last node will be removed.

def remove_last_node(self):
 
    if self.head is None:
        return
 
    current_node = self.head
    while(current_node.next.next):
        current_node = current_node.next
 
    current_node.next = None

# Delete a Linked List Node at a given Position
# In this method, we will remove the node at the given index, this method is similar to the insert_at_inded() method. In this method, if the head is None we simply return else we initialize a current_node with self.head and position with 0. If the position is equal to the index we called the remove_first_node() method else we traverse to the one node before that we want to remove using the while loop. After that when we out of the while loop we check that current_node is equal to None if not then we make the next of current_node equal to the next of node that we want to remove else we print the message “Index not present” because current_node is equal to None.

def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
# Delete a Linked List Node of a given value
# This method removes the node with the given data from the linked list. In this method, firstly we made a current_node equal to the head and run a while loop to traverse the linked list. This while loop breaks when current_node becomes None or the data next to the current node is equal to the data given in the argument. Now, After coming out of the loop if the current_node is equal to None it means that the node is not present in the data and we just return, and if the data next to the current_node is equal to the data given then we remove that node by making next of that removed_node to the next of current_node. And this is implemented using the if else condition.
def remove_node(self, data):
	current_node = self.head

	# Check if the head node contains the specified data
	if current_node.data == data:
		self.remove_first_node()
		return

	while current_node is not None and current_node.next.data != data:
		current_node = current_node.next

	if current_node is None:
		return
	else:
		current_node.next = current_node.next.next
# Linked List Traversal in Python
# Traverse the linked list and print the data of each node. Current_node equals the head and iterates through the linked list using a while loop until the current_node becomes None and prints the data of current_node in each iteration and makes the current_node next to it.

def printLL(self):
	current_node = self.head
	while(current_node):
		print(current_node.data)
		current_node = current_node.next

# Get Length of a Linked List in Python
# Returns the size of the linked list. Initialized a counter ‘size’ with 0, and then if the head is not equal to None traverse the linked list using a while loop and increment the size with 1 in each iteration and return the size when current_node becomes None 
# else: return 0.
def sizeOfLL(self):
	size = 0
	if(self.head):
		current_node = self.head
		while(current_node):
			size = size+1
			current_node = current_node.next
		return size
	else:
		return 0
