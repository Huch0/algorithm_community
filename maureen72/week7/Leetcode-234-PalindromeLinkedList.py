class Solution(object):
    def isPalindrome(self, head):
        q = []
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop() != q.pop(0):
                return False

        return True
        