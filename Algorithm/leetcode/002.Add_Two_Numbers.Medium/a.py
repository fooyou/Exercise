# !/usr/bin/env python
# @File Name: a.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2016-10-27 14:10:45
# @Last Modified: 2016-10-27 15:10:48
# @Description:
# 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lr = ListNode(0)
        lrh = lr
        jump = 0
        while l1 and l2:
            ltmp = ListNode((l1.val + l2.val + jump) % 10)
            jump = (l1.val + l2.val + jump) // 10
            lr.next = ltmp
            l1 = l1.next
            l2 = l2.next
            lr = lr.next
        lrest = l1 if l1 else l2
        while lrest:
            ltmp = ListNode((lrest.val + jump) % 10)
            jump = (lrest.val + jump) // 10
            lr.next = ltmp
            lrest = lrest.next
            lr = lr.next
        if jump:
            ltmp = ListNode(jump)
            lr.next = ltmp
        return lrh.next

if __name__ == '__main__':
    a = [1]
    b = [9, 9]
    la = ListNode(0)
    lah = la
    for n in a:
        ltmp = ListNode(n)
        la.next = ltmp
        la = la.next
    lah = lah.next

    lb = ListNode(0)
    lbh = lb
    for n in b:
        ltmp = ListNode(n)
        lb.next = ltmp
        lb = lb.next
    lbh = lbh.next

    sol = Solution()
    result = sol.addTwoNumbers(lah, lbh)
    while result:
        print(result.val)
        result = result.next



        
