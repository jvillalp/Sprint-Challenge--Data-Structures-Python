class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        #when node is None, set head to prev. (will be done at the end when list is created for reversal)
        if node is None:
            self.head = prev
            #recursive
        else:
            # takes all nodes into consideration, including 'none' at beginning of line
            #(1, none)(2,1)(3,2)(none,3)
            #goes through the entire list until hits 'none'
            self.reverse_list(node.next_node, node)
            #goes through reverse_list and node.set_next to prev (3 -> 2 -> 1 -> none)
            node.set_next(prev)


