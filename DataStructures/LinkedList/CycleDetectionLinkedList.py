"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if not head:
        return
    visited = set()
    cursor = head
    while cursor.next:
        if cursor in visited:
            return True
        visited.add(cursor)
        cursor = cursor.next
    return False
    
