# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        reverse_list = ListNode(0,None)
        reverse_temp = reverse_list
        while(temp != None):
            #print(temp.val)
            rev_node = ListNode(temp.val, None)
            rev_node.next = reverse_temp.next
            reverse_temp.next = rev_node
            #reverse_temp = reverse_temp.next
            temp = temp.next
        temp1 = reverse_list.next
        temp2 = head
        while(temp1 != None):
            if temp1.val == temp2.val:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False
        return True
            