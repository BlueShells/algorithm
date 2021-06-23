# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        protect = ListNode(0,None)
        last = protect

        if not l1:
            return l2 
        if not l2:
            return l1 
        l1end = False 
        l2end = False 
        while l1  and l2 :

            if l1.val <= l2.val :
                last.next = l1 
                last = l1 
                if not l1.next:
                    l1end = True 
                    break 
                else:
                    l1 = l1.next
            else:
                last.next = l2 
                last = l2 
                if not l2.next:
                    l2end = True 
                    break 
                else:
                    l2 = l2.next 
            print(protect.next)

        if l1end:
            l1.next = l2 
        if l2end :
            l2.next = l1
                
        return protect.next
