"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    if (not headA and headB) or (not headB and headA):
        return 0
    if not headA and not headB:
        return 1
    lA = headA
    lB = headB
    while True:
        if (lA.data != lB.data):
            return 0
        elif (not lA.next and lB.next) or (not lB.next and lA.next):
            return 0
        elif not lA.next and not lB.next:
            return 1
        else:
            lA = lA.next
            lB = lB.next
        