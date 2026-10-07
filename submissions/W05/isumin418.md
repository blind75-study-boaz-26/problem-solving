<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W05 — 이수민

| | |
|---|---|
| **주차 주제** | tree 기초 |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#tree' |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 104. Maximum Depth of Binary Tree

**[문제 링크](https://leetcode.com/problems/maximum-depth-of-binary-tree/)** · `Easy` · Python · `힌트봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- 입력 : 이진 트리의 루트 root. 노드 수는 0~10⁴개, 노드 값은 100~100이며 중복 가능함.
- 출력 : 루트부터 가장 먼 리프까지의 노드 개수를 정수로 반환함. 빈 트리는 0을 반환함.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스:루트부터 모든 리프까지의 경로를 각각 저장하고, 가장 긴 경로의 길이를 구함.
2. 한계: 모든 경로를 복사 후 저장하면 시간과 공간이 최악 O(n²)까지 필요
3. 최종:재귀 DFS로 왼쪽, 오른쪽 서브트리의 깊이를 각각 구해서 더 큰 값에 1을 더해 반환

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 트리는 왼쪽, 오른쪽 서브트리로 나뉘므로 재귀 DFS가 적합함. 각 서브트리의 깊이를 구한 뒤, 더 큰 값에 현재 노드 1개를 더해 최대 깊이를 계산
- 재귀 DFS : 한쪽 자식을 따라 끝까지 내려간 다음 돌아와서 다른 쪽을 탐색하는 DFS를 함수가 자기 자신을 다시 호출하는 방식으로 구현

**복잡도**
- 시간: `O(n)` — 전체 노드 n개를 한 번씩 방문함
- 공간: `O(h)` — 트리 높이만큼 재귀 호출이 쌓임. 한쪽으로 편향된 트리는 최악 O(n)임. 

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 빈 트리 (root = []): root is None 조건에서 0을 반환함.
- [ ] 노드가 하나인 트리 (root = [1]): 양쪽 자식의 깊이가 0이므로 max(0, 0) + 1 = 1을 반환함.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 노드가 없으면 깊이는 0
        if root is None:
            return 0

        # 왼쪽과 오른쪽 자식에서 시작하는 깊이
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 더 깊은 쪽에 현재 노드 1개를 더함
        return max(left_depth, right_depth) + 1
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 -->

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 100. Same Tree

**[https://leetcode.com/problems/same-tree/]()** · `easy` · python · `힌트 봄`

**입출력**
- 입력: 두 이진 트리의 루트 노드 p, q
- 출력: 구조와 같은 위치의 노드 값이 모두 같으면 True, 아니면 False

**접근**
1. 브루트포스: 두 트리 노드를 각각 순회하며 노드 값을 배열에 기록한 뒤 두 배열을 비교
2. 한계: 전체 트리를 순회하고 저장하므로 시간과 추가 공간이 각각 O(n+m) 필요. 두 트리가 중간에 달라도 배열을 모두 만든 뒤 비교함. 
3. 최종: 재귀 DFS로 같은 위치의 노드를 직접 비교함. 둘 다 없으면 True, 한 쪽만 없거나 값이 다르면 False 반환. 값이 같으면 오른쪽 서브트리를 비교하고 모두 같아야 True 반환함. 

**선택 근거**
- 배열에 저장하는 방식은 추가 저장 공간이 필요하고, BFS는 비교할 노드들을 큐로 관리해야 함. 재귀 DFS는 트리의 자식 구조를 그대로 따라가며 별도 자료구조 없이 구조와 값을 비교할 수 있음. 

**복잡도**
- 시간: `O(n)` — 최악의 경우 두 트리의 같은 위치에 있는 노드 쌍을 각각 한 번씩 비교함
- 공간: `O(h)` — 재귀 호출이 트리 높이만큼 쌓임. 균형 트리는 O(log n), 한쪽으로 치우친 트리는 O(n)임.

**엣지 케이스**
- [ ] 두 트리가 모두 빈 경우 (p = [], q = []): 둘 다 None이므로 True를 반환함.
- [ ] 값은 같지만 자식 위치가 다른 경우 (p = [1,2], q = [1,null,2]): 왼쪽 자식 비교에서 한쪽만 None이므로 False를 반환함

**코드**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p.val ! = q.val :
            return False
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
```

**다시 볼 때의 트리거**
>

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

---

## 572. Subtree of Another Tree

**[https://leetcode.com/problems/subtree-of-another-tree/]()** · `easy` · python · `힌트봄`

**입출력**
- 입력: 두 이진 트리의 루트 노드 root, subRoot
- 출력: root 안에 subRoot와 구조와 노드 값이 완전히 같은 서브트리가 있으면 True, 없으면 False

**접근**
1. 브루트포스: root의 모든 노드를 시작점으로 잡고 해당 노드와 모든 자손이 subRoot와 완전히 같은지 비교
2. 한계: root의 노드 수를 n, subRoot의 노드 수를 m이라고 하면 최악의 경우 시작점마다 최대 m개 노드를 비교해 시간 복잡도가 O(nm)
3. 최종: 재귀 DFS로 root 탐색하고, 각 시작점에서 isSameTree로 구조와 값을 비교함. 브루트포스 방식을 재귀로 구현하고 일치하는 서브트리를 찾으면 즉시 True 반환함. 

**선택 근거**
- BFS처럼 비교할 노드를 별도의 큐로 관리할 필요가 없음

**복잡도**
- 시간: `O(nm)` — root의 노드 n개를 시작점으로 삼아, 각 시작점에서 subRoot의 노드 최대 m개를 비교함.
- 공간: `O(h)` — root의 높이 h에 비례하는 재귀 호출 스택을 사용함. 한쪽으로 치우친 트리에서는 최악 O(n)임.

**엣지 케이스**
- [ ] root 전체가 subRoot와 같은 경우 → 첫 시작점의 isSameTree가 True를 반환함.
- [ ] 값은 같지만 root 쪽에 자손이 더 있는 경우 → isSameTree에서 한쪽만 None인 것을 확인하여 False를 반환하고, 다른 시작점을 계속 탐색함.

**코드**

```python
class Solution:
# 시작점 탐색
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
#현재 노드부터 두 트리가 완전히 같은지 비교
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

```

**다시 볼 때의 트리거**
>

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->