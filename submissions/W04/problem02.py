# https://leetcode.com/problems/product-of-array-except-self/
# 시간 복잡도: O(n) - 배열을 왼→오, 오→왼 두 번 순회
# 공간 복잡도: O(1) - 결과 리스트 answer 제외, 변수 left/right만 추가 사용

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # 1단계: 왼쪽 → 오른쪽, answer[i]에 i 왼쪽 원소들의 곱 저장
        left = 1                      # 지금까지의 왼쪽 누적 곱
        for i in range(n):
            answer[i] = left          # 자기 자신은 아직 안 곱한 상태로 저장
            left *= nums[i]           # 다음 칸을 위해 자기 자신을 누적

        # 2단계: 오른쪽 → 왼쪽, answer[i]에 i 오른쪽 원소들의 곱을 곱함
        right = 1                     # 지금까지의 오른쪽 누적 곱
        for i in range(n - 1, -1, -1):  # n-1부터 0까지 거꾸로
            answer[i] *= right        # 왼쪽 곱 × 오른쪽 곱 완성
            right *= nums[i]          # 다음 칸을 위해 자기 자신을 누적

        return answer