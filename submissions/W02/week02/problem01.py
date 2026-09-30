# https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # 숫자의 값과 인덱스를 저장할 해시 맵(딕셔너리)이다.
        
        for i, num in enumerate(nums):  # 리스트를 순회하며 인덱스(i)와 값(num)을 하나씩 가져온다.
            complement = target - num   # target을 만들기 위해 현재 숫자(num)에 더해야 하는 '수'를 구한다.
            
            if complement in seen:      # 구한 보수가 이미 해시 맵(seen)에 존재한다면
                return seen[complement], num  # 보수의 인덱스와 현재 숫자 값을 반환한다.
                
            seen[num] = i               # 존재하지 않는다면, 현재 숫자와 그 인덱스를 해시 맵에 기록한다.

'''
시간 복잡도: O(n)
리스트를 한 번만 순회 (for i, num in enumerate(nums))
딕셔너리 조회/삽입(in seen, seen[num] = i)은 해시맵이라 평균 O(1)
총 n번 반복 × O(1) = O(n)

공간 복잡도: O(n)
최악의 경우 (정답을 못 찾고 끝까지 순회) seen에 n개의 원소가 모두 들어감
'''