class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1
        return True

    def pop(self):
        if self.size == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.size -= 1
        return temp.value

    def peek(self):
        """Return the value of the top node without popping."""
        if self.size == 0:
            return None
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

class SearchHistory:
    def __init__(self):
        self.history_stack = Stack()  # Stack to store user search history

    def push_search(self, search_details):
        """Push a new search detail onto the history stack."""
        self.history_stack.push(search_details)

    def pop_search(self):
        """Pop the last search detail from the history stack."""
        return self.history_stack.pop()

    def view_history(self):
        """View all past searches."""
        history = []
        current = self.history_stack.top
        while current is not None:
            history.append(current.value)
            current = current.next
        return history  # You may want to implement a method to list all searches

    def get_last_search(self):
        """Get the last search (top of the stack)."""
        return self.history_stack.peek()  