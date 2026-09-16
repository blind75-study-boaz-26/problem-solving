# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:      # 숫자가 이미 딕셔너리 키로 존재한다면 중복!
                return True
            seen[num] = True     # 숫자를 딕셔너리 키로 기록
            
        return False
'''
해시 맵(딕셔너리)을 사용할 때의 시간 복잡도와 공간 복잡도이다.

* **시간 복잡도**: O(N)이다.
* **이유**: 리스트의 원소 개수($N$)만큼 처음부터 끝까지 한 번 순회하며, 딕셔너리의 키 검색(`in`)과 삽입(`seen[num] = True`) 연산은 평균적으로 O(1)의 시간이 걸리기 때문이다.


* **공간 복잡도**: O(N)이다.
* **이유**: 최악의 경우(중복이 전혀 없는 경우) 리스트의 모든 원소($N$개)를 딕셔너리의 키로 저장해야 하므로 원소 개수에 비례하는 추가 메모리 공간이 필요하기 때문이다.
'''
