# https://leetcode.com/problems/missing-number/submissions/2164980059/?envType=problem-list-v2&envId=oizxjoit
# 풀이: 등장한 숫자를 딕셔너리에 기록한 뒤, 0 ~ n-1 중 기록에 없는 숫자를 찾는다.
#       0 ~ n-1이 모두 있으면 빠진 숫자는 n(= 최댓값 + 1)이다.
# 시간 복잡도: O(n) - nums를 한 번 순회해 기록 + 0 ~ n-1을 한 번 순회하며 O(1) 조회 + max() O(n)
# 공간 복잡도: O(n) - 숫자 n개를 저장하는 딕셔너리
# 참고: 0 ~ n의 합(n*(n+1)//2)에서 sum(nums)를 빼면 공간 O(1)로도 풀 수 있음

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # 등장한 숫자 기록 (key 조회가 평균 O(1))
        duplicate = {}

        for i, num in enumerate(nums):
            duplicate[num] = True

        # 0 ~ n-1 중 기록에 없는 숫자가 빠진 숫자
        for a in range(len(nums)):
            if a not in duplicate:
                return a
        # 0 ~ n-1이 모두 있으면 빠진 숫자는 n (최댓값 n-1 + 1)
        return max(duplicate)+1