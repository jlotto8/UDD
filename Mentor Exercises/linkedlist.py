class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


# Insertion at Beginning in Linked List 
# Create a new_node and check if the head is an empty node or not- if empty, list is empty
# if the head is empty then make the new_node as head and return 
# else: insert the head at the next new_node and make the head equal to new_node.
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

#Insertion in Linked List at End
# Create a new_node and check if the head is an empty node or not if the head is empty then make the new_node as head and return (same as above)
# else make a current_node equal to the head traverse to the last node of the linked list and when we get None after the current_node the while loop breaks and insert the new_node in the next of current_node which is the last node of linked list.

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

# Remove the first node of the linked list 
# make the second node head of the linked list
    def remove_first_node(self):
        if self.head is not None:
            self.head = self.head.next


# Get Length of a Linked List in Python
# Initialized a counter ‘size’ with 0, and then if the head is not equal to None traverse the linked list using a while loop and increment the size with 1 in each iteration and return the size when current_node becomes None 
# else: return 0.
    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
        return size
      

    # find node at the current index
    # create node with given data
    # the node before the current index, set it's next pointer to the new node
    # consider drawing a picture, 
    # consider an insertmethod
    # index out of range
    # inserts the node at the given index. create a new_node, a current_node that equals to the head, and a counter ‘position’ initializes with 0. if the index is equal to zero it means the node is to be inserted at begin so we called insertAtBegin() method 
    # else  run a while loop until the current_node is not equal to None or (position+1) is not equal to the index we have to at the one position back to insert at a given position to make the linking of nodes and in each iteration, increment the position by 1 and make the current_node next of it. 
    # When the loop breaks and if current_node is not equal to None, insert new_node at after to the current_node. If current_node is equal to None it means that the index is not present in the list and print “Index not present”.
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
        
#  remove the node at the given index, if the head is None, return 
# else initialize a current_node with self.head and position with 0. If the position is equal to the index we called the remove_first_node() method else we traverse to the one node before that we want to remove using the while loop. After that when we out of the while loop we check that current_node is equal to None if not then we make the next of current_node equal to the next of node that we want to remove else we print the message “Index not present” because current_node is equal to None.
    def deleteAtPosition(self, index):
        pass

    # what if value isn't in the list
    # what if the value is there multiple times
    # consider delete all by value
    def deleteWithValue(self, value):
        

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList()

