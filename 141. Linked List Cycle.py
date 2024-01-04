# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen_nodes = set()
        while head is not None:
            if head in seen_nodes:
                return True
            seen_nodes.add(head)
            head = head.next