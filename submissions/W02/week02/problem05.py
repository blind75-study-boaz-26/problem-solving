class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_value = float('inf')
        for num in nums:
            if min_value > num:
                min_value = num
        return min_value
'''
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # 최솟값은 mid보다 오른쪽에 있음
                left = mid + 1
            else:
                # 최솟값은 mid이거나 그보다 왼쪽에 있음
                right = mid
                
        return nums[left]
'''