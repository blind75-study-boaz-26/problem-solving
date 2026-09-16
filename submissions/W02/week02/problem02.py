# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()  # 방문한 노드를 저장할 집합
        current = head
        
        while current is not None:
            # 이미 방문한 노드라면 사이클 존재!
            if current in seen:
                return True
            
            seen.add(current)      # 현재 노드 기록
            current = current.next # 다음 노드로 이동
            
        return False  # 반복문이 끝났다 = None을 만났다 = 사이클 없음


#시간 복잡도: O(N) (모든 노드를 최대 한 번씩 방문)
#공간 복잡도: O(N) (노드 개수만큼 set에 저장)