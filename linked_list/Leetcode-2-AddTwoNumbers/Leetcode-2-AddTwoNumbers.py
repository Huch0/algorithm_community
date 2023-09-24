class Solution(object):
    def addTwoNumbers(self, l1, l2):
        prefixSum = 0
        digitNumber = 1
        while l1:
            prefixSum += l1.val * digitNumber
            digitNumber *= 10
            l1 = l1.next
        digitNumber = 1
        while l2:
            prefixSum += l2.val * digitNumber
            digitNumber *= 10
            l2 = l2.next

        return prefixSum
# 정수를 출력하는 걸로 이해했는데, ListNode를 출력해야 한다고 함

# def addTwoNumbers(self, l1, l2):
#     root = head = ListNode(0)
#     carry = 0
#     while l1 or l2 or carry:
#         sum = 0
#         if l1:
#             sum += l1.val
#             l1 = l1.next
#         if l2:
#             sum += l2.val
#             l2 = l2.next
#         carry, val = divmod(sum + carry, 10)
#         head.next = ListNode(val)
#         head = head.next
#     return root.next