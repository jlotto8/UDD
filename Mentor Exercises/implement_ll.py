class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

    def insert_at_beginning(self):
        if self.head is None:
            Node.head = 1
            Node.next = 2

    def list_to_ll(self):
        pass

    def list_from_ll(self): # return an array from a ll ll = a,b,c  ['a','b','c']
        # while self.head != None:
        arry = []
        current = self
        while current != None:
            arry.append(current.data)
            current = current.next
        return arry
        
            
node_one = Node('a')
node_two = Node('b')
node_three = Node('c')
node_four = Node('d')

# finish list to ll method, solve recursively