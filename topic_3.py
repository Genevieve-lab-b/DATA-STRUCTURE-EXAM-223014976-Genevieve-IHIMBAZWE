class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first occurrence of a node with the given data."""
        if self.head is None:
            return "List is empty"
        if self.head.data == key:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None and current.next.data != key:
            current = current.next
        
        if current.next is not None:
            current.next = current.next.next
        else:
            return "Key not found"

    def display(self):
        """Display the list contents."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        return elements

milestone_list = SinglyLinkedList()
milestone_list.append("Site Preparation")
milestone_list.append("Foundation Laying")
milestone_list.append("Structural Work")
milestone_list.prepend("Project Initiation")
print(milestone_list.display()) 
milestone_list.delete("Foundation Laying")
print(milestone_list.display())
