# 002_add_two_numbers.py
# LeetCode 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """用于打印链表"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)


class Solution:
    """
    给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
    并且每个节点只能存储一位数字。
    
    请你将两个数相加，并以相同形式返回一个表示和的链表。
    
    假设除了数字 0 之外，这两个数都不会以 0 开头。
    """
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        逐位相加，处理进位
        时间复杂度: O(max(m, n))，其中 m 和 n 分别是两个链表的长度
        空间复杂度: O(max(m, n))，结果链表的长度
        """
        dummy = ListNode(0)  # 虚拟头节点
        current = dummy
        carry = 0  # 进位
        
        while l1 or l2 or carry:
            # 获取当前位的值，如果链表已遍历完则为 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 计算当前位的和
            total = val1 + val2 + carry
            carry = total // 10  # 新的进位
            digit = total % 10   # 当前位的结果
            
            # 创建新节点
            current.next = ListNode(digit)
            current = current.next
            
            # 移动到下一个节点
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next


def create_linked_list(digits: list) -> Optional[ListNode]:
    """从列表创建链表（逆序存储）"""
    if not digits:
        return None
    
    head = ListNode(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = ListNode(digit)
        current = current.next
    return head


# 测试用例
if __name__ == "__main__":
    sol = Solution()
    
    # 示例 1: l1 = [2,4,3], l2 = [5,6,4] -> 342 + 465 = 807 -> [7,0,8]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print(f"示例 1: {l1} + {l2} = {result}")  # 2->4->3 + 5->6->4 = 7->0->8
    
    # 示例 2: l1 = [0], l2 = [0] -> 0 + 0 = 0 -> [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    print(f"示例 2: {l1} + {l2} = {result}")  # 0 + 0 = 0
    
    # 示例 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> 9999999 + 9999 = 10009998 -> [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)
    print(f"示例 3: {l1} + {l2} = {result}")  # 8->9->9->9->0->0->0->1
