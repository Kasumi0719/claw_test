# 001_two_sum.py
# LeetCode 1. Two Sum
# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    """
    给定一个整数数组 nums 和一个整数目标值 target，
    请你在该数组中找出和为目标值 target 的那两个整数，
    并返回它们的数组下标。
    
    假设每种输入只会对应一个答案，并且你不能使用相同的元素。
    """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        使用哈希表解法，时间复杂度 O(n)，空间复杂度 O(n)
        
        思路：遍历数组，对于每个数，检查 (target - num) 是否在哈希表中
              如果在，返回两个下标；如果不在，将当前数加入哈希表
        """
        num_map = {}  # 值 -> 下标的映射
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []  # 根据题意，一定有解，这里不会执行到


# 测试用例
if __name__ == "__main__":
    sol = Solution()
    
    # 示例 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {sol.twoSum(nums1, target1)}")  # [0, 1]
    
    # 示例 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {sol.twoSum(nums2, target2)}")  # [1, 2]
    
    # 示例 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {sol.twoSum(nums3, target3)}")  # [0, 1]
