# https://leetcode.com/problems/invert-binary-tree/submissions/2164998494/?envType=problem-list-v2&envId=oizxjoit
# 풀이: 재귀(DFS). 현재 노드의 왼쪽/오른쪽 자식을 서로 바꾼 뒤, 양쪽 서브트리에도 같은 작업을 맡긴다.
#       종료 조건 → 내 자식 교환 → 자식에게 재귀 호출 순서
# 시간 복잡도: O(n) - 모든 노드를 정확히 한 번씩 방문 (n = 노드 수)
# 공간 복잡도: O(h) - 재귀 호출 스택의 깊이 = 트리 높이 h
#             균형 트리면 O(log n), 한쪽으로 치우친 트리면 최악 O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        # 종료 조건: 빈 노드는 뒤집을 것이 없음
        if root is None:
            return None

        # 현재 노드의 왼쪽/오른쪽 자식 교환
        root.left, root.right = root.right, root.left

        # 양쪽 서브트리도 같은 방식으로 뒤집기
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root