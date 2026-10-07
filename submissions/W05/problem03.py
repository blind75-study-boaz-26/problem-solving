# https://leetcode.com/problems/missing-number/submissions/2164980059/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        duplicate = {}

        for i, num in enumerate(nums):
            duplicate[num] = True

        for a in range(len(nums)):
            if a not in duplicate:
                return a
        return max(duplicate)+1