# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        nums.sort()

        temp = head
        for i in range(len(nums)):
            temp.val = nums[i]
            temp = temp.next
        
        return head