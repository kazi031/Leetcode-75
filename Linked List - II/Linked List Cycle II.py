With Memory:


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        lookup = set()
        while temp:
            if temp in lookup:
                return temp
            lookup.add(temp)
            temp = temp.next
        return None

O(1) solution:

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast.next or not fast.next.next:
            return None
        slow2 = head
        while slow.next:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next  

