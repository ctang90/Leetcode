# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            if c == 0:
                return None
            else:
                return ListNode(c)
        
        if l1 != None and l2 == None:
            if c == 0:
                return l1
            else:
                val = l1.val + c
                if val < 10:
                    node = ListNode(val)
                    node.next = l1.next
                    return node
                else:
                    node = ListNode(val % 10)
                    nextNode = self.addTwoNumbers(l1.next, None, val/10)
                    node.next = nextNode
                    return node
        
        if l1 == None and l2 != None:
            if c == 0:
                return l2
            else:
                val = l2.val + c
                if val < 10:
                    node = ListNode(val)
                    node.next = l2.next
                    return node
                else:
                    node = ListNode(val % 10)
                    nextNode = self.addTwoNumbers(None, l2.next, val/10)
                    node.next = nextNode
                    return node
        
        val = l1.val + l2.val + c
        node = ListNode(val % 10)
        nextNode = self.addTwoNumbers(l1.next, l2.next, val / 10)
        node.next = nextNode
        return node
        
        
        
        
        