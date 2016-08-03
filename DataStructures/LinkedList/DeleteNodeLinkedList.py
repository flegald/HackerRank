"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position == 0:
        head = head.next
    else:
        cursor = head
        count = position - 1
        while True:
            if count == 0:
                cursor.next = cursor.next.next
                break
            cursor = cursor.next
            count -= 1
    return head
            