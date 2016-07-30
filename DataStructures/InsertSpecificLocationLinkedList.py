"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if position == 0:
        return Node(data,head)
    cursor1 = head
    cursor2 = Node()
    new_node = Node(data)
    count = 0
    while True:
        count += 1
        cursor2 = cursor1
        cursor1 = cursor1.next
        if count == position:
            cursor2.next = new_node
            new_node.next = cursor1
            return head
            