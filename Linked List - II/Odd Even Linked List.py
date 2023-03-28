# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode(0, None)
        temp = head
        evenList = newNode
        if head == None:
            return head
        while(temp.next):
            temp_val = ListNode(temp.next.val, None)
            newNode.next = temp_val
            temp.next = temp.next.next
            if temp.next != None:
                temp = temp.next
            newNode = newNode.next
              
        temp.next = evenList.next

        return head