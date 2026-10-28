<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W06 — 이수민

| | |
|---|---|
| **주차 주제** | tree |
| **선언한 목표** | 2문제 |
| **실제로 푼 수** | 2문제 |
| **패턴 태그** | `#트리` `#dp`|

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 1. Binary Tree Maximum Path Sum (124)

**[문제 링크](https://leetcode.com/problems/binary-tree-maximum-path-sum/)** · `Hard` · Python · `해설 봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- 이진트리에서 하나의 경로를 골랐을 때, 그 경로에 있는 노드 값의 합이 최대가 되는 정수 값을 구하는 문제 
- 입력 : 노드 수 1~30,000인 이진트리의 루트. 노드 값은 -1,000~1,000이며, 중복·음수 가능.
- 출력 : 비어 있지 않은 경로 중 최대 노드 합을 정수로 반환. 루트를 지나지 않아도 됨.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 각 노드에서 DFS로 모든 다른 노드까지의 경로 합을 구해 최댓값을 찾는다.
2. 한계: 노드마다 탐색을 반복하므로 O(n²)이 걸린다. n 개의 노드 x O(n)
3. 최종: 위 순회 기반 트리 DP로, 각 노드에서 양쪽 경로를 합쳐 정답을 갱신하고 부모에게는 한쪽 경로의 최대 합만 반환한다. O(n). n 개의 노드 x 노드 당 O(1)

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 모든 경로는 가장 위의 노드와 좌우의 한 갈래 경로로 나눌 수 있으므로, 자식이 반환한 최대 경로 합으로 현재 노드의 정답 후보를 계산하는 트리 DP를 사용한다. 자식의 결과가 먼저 필요하므로 후위 순회한다.

**복잡도**
- 시간: `O(n)` — 각 노드를 한 번 방문하고, 노드마다 상수 시간 계산.
- 공간: `O(n)` — 트리 높이 h만큼 재귀 호출 스택 사용. 편향 트리는 최악 O(n)

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ]모든 노드가 음수: answer를 −∞로 초기화하여 가장 큰 노드 값 하나를 선택.
- [ ]자식의 경로 합이 음수: max(0, 자식 결과)로 제외하여 현재 경로의 합이 감소하지 않도록 처리.

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        answer = float("-inf")

        def solve(node):
            nonlocal answer

            if node is None:
                return 0

            L = max(0, solve(node.left))
            R = max(0, solve(node.right))

            # 현재 노드에서 양쪽을 연결한 경로
            answer = max(answer, node.val + L + R)

            # 부모에게 연결할 한쪽 경로
            return node.val + max(L, R)

        solve(root)
        return answer
```

**다시 볼 때의 트리거**
> <트리에서 최대 경로 합 → 자식의 결과를 부모에서 조합하는 트리 DP + 후위 순회> 

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 2.  Kth Smallest Element in a BST (230)

**[문제 링크](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)** · `medium` · python · `결과태그`

**입출력**
- 이진 탐색 트리에 있는 모든 노드 값 중, k번째로 작은 값을 구하는 문제
- 입력 : BST의 루트 root와 정수 k. 노드 수는 1 ≤ n ≤ 10⁴, 1 ≤ k ≤ n, 노드 값은 0~10⁴.
- 출력 : k번째로 작은 노드의 값.

**접근**
1. 브루트포스: 모든 노드 값을 리스트에 저장하고 정렬한 뒤, 인덱스 k−1의 값을 반환한다.
2. 한계: 병합정렬에 O(n log n)이 걸리며, BST의 구조를 활용하지 못한다.
3. 최종: 중위 순회로 값을 리스트에 오름차순으로 저장한 뒤, 인덱스 k−1의 값을 반환한다. 시간은 O(n).

**선택 근거**
- BST는 왼쪽 서브트리 < 현재 노드 < 오른쪽 서브트리이므로, 중위 순회하면 별도의 정렬 없이 오름차순으로 값을 얻을 수 있다.

**복잡도**
- 시간: `O(n)` — 중위 순회로 모든 노드를 한 번 방문한다. 
- 공간: `O(n)` — n개의 값을 저장하는 리스트와 재귀 호출 스택을 사용한다. 

**엣지 케이스**
- [ ] 노드가 하나뿐: k = 1이므로 해당 노드 값을 반환한다.
- [ ] 한쪽으로 편향된 트리: 중위 순회는 동일하게 적용되지만, 재귀 깊이가 n이 되어 Python에서 재귀 제한을 초과할 수 있으므로 반복문과 스택으로 구현한다.

**코드**

```python
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        values = []
        stack = []
        node = root

        while node is not None or stack:
            # 왼쪽 자식부터 방문하도록 저장
            while node is not None:
                stack.append(node)
                node = node.left

            # 현재 노드의 값을 저장
            node = stack.pop()
            values.append(node.val)

            # 오른쪽 서브트리로 이동
            node = node.right

        return values[k - 1]

```

**다시 볼 때의 트리거**
>

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->
