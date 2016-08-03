"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if not headA and headB:
        return headB
    elif not headB and headA:
        return headA
    if headA.data <= headB.data:
        result = headA
        result.next = MergeLists(headA.next, headB)
    elif headB.data <= headA.data:
        result = headB
        result.next = MergeLists(headA, headB.next)
    return result