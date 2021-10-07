class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        ans = ListNode(0)
        ans_tail = ans
        
        while l1 or l2 or carry > 0: 
            num1 = (l1.val if l1 else 0)
            num2 = (l2.val if l2 else 0)
            
            total = num1 + num2 + carry
            
            if total >= 10: 
                carry = 1 
            else:
                carry = 0 
                
            ans_tail.next = ListNode(total % 10)
            ans_tail = ans_tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return ans.next
            
        
            
