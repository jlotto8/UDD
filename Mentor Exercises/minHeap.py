class MinHeap:

    def __init__(self,nodes,cmp):
        self.nodes = []

        for node in nodes: # adds each node from  the input list to the heap
            self.add(node)
    
    # Method to return the number of elements in the heap
    def __len__(self): # double underscore method
        return len(self.nodes)

    # Method to calculate the index of the left child of a given parent index
    def __get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    # Method to calculate the index of the right child of a given parent index
    def __get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    # Method to calculate the index of the parent of a given child index
    def __get_parent_index(self, child_index):
        return (child_index - 1) // 2

    # Method to check if a given parent index has a left child
    def __has_left_child(self, parent_index):
        return self.__get_left_child_index(parent_index) < len(self.nodes)

    # Method to check if a given parent index has a right child
    def __has_right_child(self, parent_index):
        return self.__get_right_child_index(parent_index) < len(self.nodes)

    # Method to check if a given index has a parent; root will always be first index
    def __has_parent(self, index):
        return self.__get_parent_index(index) >= 0  # if index != 0

    """
Adding/inserting
Get the element (starting with the last one)
Check if it disobeys the priority rule, in this case (min-heap), check if its key value is smaller than the parent
If smaller, then swap with its parent
Recurse in the index of the parent
Keep bubbling up/sifting up until reaching the root
    """

    # Method to swap the elements at two given indices
    def __swap(self, first_index, second_index):
        if first_index >= len(self.nodes) or second_index >= len(self.nodes):  # use assert statement(s) with and 
            print(f'first ({first_index}) or second ({second_index}) are invalid') # raise  IndexError and message
            # return 
        temp = self.nodes[first_index]  # Temporarily store the value at the first index
        self.nodes[first_index] = self.nodes[second_index]  # Assign the value at the second index to the first index
        self.nodes[second_index] = temp  # Assign the temporarily stored value to the second index

    # Method to maintain the heap property by moving the last added element up to its correct position
    def __heapify_up(self, child=None):
        if child is None:
            # If no child index is provided, start with the last element
            child = len(self.nodes) - 1
        # Check if the current child has a parent and if it is smaller than the parent
        parent_idx = self.__get_parent_index(child)
        if self.__has_parent(child) and self.nodes[child] < self.nodes[parent_idx]:
            # Swap the child with its parent
            self.__swap(child, parent_idx)
            # Recursively call heapify_up on the parent index
            self.__heapify_up(child=parent_idx)
        # Return the updated heap
        # return self.nodes return value not needed
      
    # Method to add an element to the heap
    def add(self, item):
        self.nodes.append(item)  # Append the new item to the end of the list
        self.__heapify_up()  # Move the new item to its correct position in the heap

    """
    Deleting
    Get the element key (starts with the first element)
    Check if the key is greater than any of the children (left or right)
    If greater, than it is in the wrong position, swap with the smallest between left and right
    Continue to heapify down with the smallest child index
    Repeat until no more children
    """

    # Method to maintain the heap property by moving the root element down to its correct position
    def __heapify_down(self, index=0):
        if index >= len(self.nodes) or not self.__has_left_child(index): # split these conditions; first condition make an assert statement; second condition just return if it happens
            return self.nodes  # If the index is out of bounds or has no left child, return the heap
        # Determine the index of the smaller child
        smaller_child_idx = self.__get_left_child_index(index)
        if self.__has_right_child(index) and self.nodes[self.__get_right_child_index(index)] < self.nodes[smaller_child_idx]:
            smaller_child_idx = self.__get_right_child_index(index)

        if self.nodes[index] > self.nodes[smaller_child_idx]:
            # Swap the current element with its smaller child if it's larger
            self.__swap(index, smaller_child_idx)
            # Recursively call heapify_down on the smaller child index
            self.__heapify_down(smaller_child_idx)
        return self.nodes

# public method to remove; takes an index as input; calls heapify down to complete it
# consider other public methods
# check if a value exists 

        """
        Removing the minimum element
        Polls lowest element from the heap (usually root). To avoid memory shift
        of first-element removal, copy the last element to the first
        position, shrink the size by 1 and heapify down.
        """
        # Method to remove and return the minimum element (root) from the heap
    def poll(self):
        if not self.nodes:
            return None

        # Remove the root element and replace it with the last element
        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()  # Remove the last element
        # Move the new root element to its correct position in the heap
        self.__heapify_down()
        return removed_node  # Return the removed element

    def peek(self):
        if not self.nodes:
            return None
        return self.nodes[0]

# Sample usage of the MinHeap class
# Initialize the heap with a list of elements
initial_nodes = [3, 1, 6, 5, 9, 8]
min_heap = MinHeap(initial_nodes)

# Print the heap after initialization
print("Initial heap:", min_heap.nodes)

# Add new elements to the heap
min_heap.add(2)
min_heap.add(4)

# Print the heap after adding elements
print("Heap after adding 2 and 4:", min_heap.nodes)

# Poll (remove) the minimum element from the heap
min_element = min_heap.poll()
print("Polled element:", min_element)

# Print the heap after polling the minimum element
print("Heap after polling the minimum element:", min_heap.nodes)

# Check the size of the heap
heap_size = min_heap.size()
print("Current heap size:", heap_size)
