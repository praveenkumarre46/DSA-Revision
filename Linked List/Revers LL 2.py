class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        before = dummy
        
        for _ in range(left - 1):
            before = before.next
            
        curr = before.next
        prev = None
        
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        before.next.next = curr
        before.next = prev
        
        return dummy.next