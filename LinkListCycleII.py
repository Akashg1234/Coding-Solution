class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow,fast,start=head,head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=start:
                    slow=slow.next
                    start=start.next
                return start
        return None
