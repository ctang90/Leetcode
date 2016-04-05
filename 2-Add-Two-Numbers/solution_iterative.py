# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2, c=0):
        sum = 0
        prehead = ListNode(-1)
        tail = prehead
        while True:
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            if l1 == None and l2 == None and sum == 0:
                break
            node = ListNode(sum % 10)
            sum = sum / 10
            tail.next = node
            tail = tail.next
        return prehead.next
        
            
            
        
        
        
        
        