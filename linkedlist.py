class Element(object):
    def __init__(self, value): #creating an individual cell in a linked list
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, newElement):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = newElement
        else:
            self.head = newElement

    def get_position(self, position):
        counter = 1
        current = self.head
        if position<1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        return None

