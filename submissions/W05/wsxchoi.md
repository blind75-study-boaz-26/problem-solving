<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W05 — 최우성

| | |
|---|---|
| **주차 주제** | Tree |
| **선언한 목표** | 1문제 |
| **실제로 푼 수** | 1문제 |
| **패턴 태그** | `Tree`, `Depth-First Search`, `Breadth-First Search`, `Binary Tree` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 100. Same Tree

**[문제 링크](https://leetcode.com/problems/same-tree/)** · `Easy` · Python · `자력해결`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- Input: p = [1,2,3], q = [1,2,3]
- Output: true

Constraints:

- The number of nodes in both trees is in the range [0, 100]
- -10^4 <= Node.val <= 10^4

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
p,q 두 개의 포인터로 각 트리를 순회해야한다.
최단거리 문제가 아니기 때문에 시간 복잡도 측면에서 DFS, BFS 중 우위는 없다.
두 트리가 동일할 경우 완전 탐색이다.

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- DFS를 선택했다.

**복잡도**
- 시간: `O(N)` — 트리가 동일한 경우 완전 탐색. 노드 수가 100개 이하이므로 `O(1)`이라고 할 수도 있다.
- 공간: `O(h)` — 트리의 깊이

**엣지 케이스** (최소 2개, 처리 방법까지)
- [x] p,q 둘 다 NULL -> 통과

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def check_tree(p,q):
            # 둘 다 NULL -> 통과
            if p is None and q is None:
                return True
            # 한쪽만 NULL -> false
            if p is None or q is None:
                return False
            # 둘 다 NULL 아님 -> 값 비교
            if p.val == q.val:
                # 자식으로 이동
                return check_tree(p.left, q.left) and check_tree(p.right, q.right)
            else:
                return False
        return check_tree(p,q)

```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 --> 재귀 시 어떤 식으로 값을 반환할지 잘 생각하자.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->
