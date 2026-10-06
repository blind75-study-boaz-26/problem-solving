<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W05 — 김해인

| | |
|---|---|
| **주차 주제** | Tree 기초 |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** |`#BinaryTree` `#DFS` `#BFS` `#Queue`|

**한 줄 회고:**
subtree는 재귀로 살펴본다. tree를 특정 순서대로 순회할 땐 큐나 스택 중 FIFO인지 LIFO인지 생각해보기. 
---

## 104. Maximum Depth of Binary Tree

**[문제 링크](https://leetcode.com/problems/maximum-depth-of-binary-tree/)** · `Easy` · Python · `힌트봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
- 입력: 이진 트리의 루트 노드 root (노드 개수 0 ~ 10⁴)
- 출력: 루트 노드에서 가장 멀리 떨어진 리프 노드까지의 최대 깊이를 반환한다.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 루트에서 모든 리프 노드까지의 경로를 직접 탐색하고 각 경로의 길이를 비교한다
2. 한계: 각 경로를 따로 저장하거나 반복해서 탐색할 필요 없이, 각 서브트리의 최대 깊이만 알면 현재 노드의 최대 깊이를 계산할 수 있다.
3. 최종: DFS 재귀를 사용해 왼쪽과 오른쪽 서브트리의 최대 깊이를 구하고, 둘 중 큰 값에 현재 노드 1을 더한다.

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- `Binary Tree`는 각 노드가 왼쪽과 오른쪽 자식을 가지므로, 왼쪽 서브트리와 오른쪽 서브트리를 각각 재귀적으로 탐색하기 적합하다.
- `self.maxDepth(root.left)`와 `self.maxDepth(root.right)`가 각 서브트리의 최대 깊이를 반환하므로 `max(left, right) + 1`로 현재 노드의 최대 깊이를 계산할 수 있다.

**복잡도**
- 시간:`O(n)` — 최대 깊이를 구하기 위해 트리의 모든 노드를 한 번씩 방문한다.
- 공간:`O(h)` — 재귀 호출 스택에 트리의 높이 h만큼 함수 호출이 저장된다. 최악의 경우 한쪽으로만 이어진 트리에서는 O(n)이다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [빈 트리] `root`가 `None`이면 노드가 없으므로 깊이 0을 반환한다.
- [1] 루트 노드 하나만 있는 경우 → 왼쪽과 오른쪽이 모두 None이므로 `max(0, 0) + 1 = 1`을 반환한다.
- [1,null,2] 한쪽으로만 자식 노드가 이어지는 경우 → 존재하는 방향으로 재귀 호출을 계속하며 깊이를 계산한다.

**코드**

```python
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 --> Binary Tree에서 높이 또는 최대 깊이를 구해야 한다면 왼쪽 깊이, 오른쪽 깊이를 재귀로 구한 뒤 max(left, right) + 1을 떠올린다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** self.maxDepth(root.left)처럼 자기 자신을 다시 호출하는 것만으로 어떻게 깊이가 계산되는지 재귀 동작이 헷갈렸음.
- **복습 필요:** [O]

</details>

---

## 226. Invert Binary Tree

**[문제 링크](https://leetcode.com/problems/invert-binary-tree/)** · `Easy` · python · `힌트봄`

**입출력**
- 입력: 이진 트리의 루트 노드 root (노드 개수 0 ~ 100)
- 출력: 모든 노드의 왼쪽 자식과 오른쪽 자식을 서로 바꾼 뒤, `뒤집힌 트리의 root`를 반환한다.


**접근**
1. 브루트포스: 트리의 모든 노드를 순회하면서 각 노드의 왼쪽 자식과 오른쪽 자식을 직접 교환한다.
2. 한계: 트리 구조상 각 노드 아래에 또 같은 형태의 서브트리가 있으므로 반복적으로 직접 처리하기보다 재귀적으로 같은 연산을 적용하는 것이 자연스럽다.
3. 최종: 현재 노드의 `left`와 `right`를 교환한 뒤, 왼쪽 서브트리와 오른쪽 서브트리에 같은 함수를 `재귀 호출`한다.

**선택 근거**
- `Binary Tree`는 각 노드 아래에 다시 `왼쪽·오른쪽 서브트리`가 존재하므로, 현재 노드에서 수행한 작업을 `자식 노드`에도 동일하게 적용하는 재귀 방식이 적합하다.
- 현재 노드의 `left`와 `right`를 먼저 교환한 뒤 두 서브트리를 재귀적으로 뒤집으면 전체 트리가 뒤집힌다.

**복잡도**
- 시간: `O(n)` — 트리의 모든 노드를 한 번씩 방문하며 각 노드에서 왼쪽·오른쪽 자식을 한 번 교환한다.
- 공간: `O(h)` — 재귀 호출 스택에 트리의 높이 h만큼 함수 호출이 저장된다. 한쪽으로 치우친 트리에서는 최악의 경우 O(n)이다.

**엣지 케이스**
- [빈 트리] root가 None이면 뒤집을 노드가 없으므로 None을 반환한다.
- [1] 노드가 하나뿐이면 왼쪽과 오른쪽 자식이 모두 None이므로 그대로 해당 노드를 반환한다.
- [2,1,3] 루트의 왼쪽 1과 오른쪽 3을 교환하여 [2,3,1] 형태로 만든다.


**코드**

```python
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

**다시 볼 때의 트리거**
> Binary Tree에서 모든 노드에 같은 작업을 반복해야 한다면 현재 노드에서 처리한 뒤 왼쪽·오른쪽 서브트리에 같은 함수를 재귀 호출하는 방식을 떠올린다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 재귀구조... self.invertTree(root.left)
- **복습 필요:** [O]

</details>

---


## 102. Binary Tree Level Order Traversal

**[문제 링크](https://leetcode.com/problems/binary-tree-level-order-traversal/)** · `Medium` · python · `해설봄`

**입출력**
- 입력: 이진 트리의 루트 노드 root (노드 개수 0 ~ 2000)
- 출력: 트리의 노드 값을 위에서 아래로, 같은 레벨에서는 왼쪽에서 오른쪽 순서로 묶은 2차원 리스트를 반환한다.

**접근**
1. 브루트포스: 각 노드의 깊이를 따로 계산한 뒤 같은 깊이의 노드끼리 묶을 수 있다.
2. 한계: 각 노드의 깊이를 별도로 계산할 필요 없이, `큐`를 사용하면 처음부터 `레벨 단위`로 탐색할 수 있다.
3. 최종: `BFS`와 `Queue`를 사용하고, 각 반복 시작 시점의 `len(queue)`만큼만 노드를 꺼내 현재 레벨을 구성한다.


**선택 근거**
- `Level Order Traversal`은 루트에서 가까운 노드부터 순서대로 탐색해야 하므로 `FIFO` 방식의 `Queue`를 사용하는 `BFS`가 적합하다.
- 반복 시작 시점의 `len(queue)`는 현재 레벨에 존재하는 노드 개수이므로, 그 개수만큼만 처리하면 레벨별로 값을 묶을 수 있다.


**복잡도**
- 시간: `O(n)` — 각 노드를 한 번씩 방문한다. 단, Python 리스트의 pop(0)을 사용하면 앞 원소 제거에 추가 비용이 발생하므로 실제 구현에서는 deque.popleft()가 더 적합하다.
- 공간: `O(n)` — 최악의 경우 한 레벨에 많은 노드가 존재할 수 있어 큐에 최대 O(n)개의 노드가 저장될 수 있다.

**엣지 케이스**
- [빈 트리] root가 없으면 순회할 노드가 없으므로 빈 리스트 []를 반환한다.
- [1] 루트 노드 하나만 존재하면 [[1]]을 반환한다.
- [3,9,20,null,null,15,7] 각 레벨을 [3], [9,20], [15,7]로 나누어 최종적으로 [[3],[9,20],[15,7]]을 반환한다.

**코드**

```python
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
```

**다시 볼 때의 트리거**
> Binary Tree를 레벨별로 탐색해야 한다면 BFS + Queue를 떠올리고, len(queue)만큼만 처리해서 현재 레벨과 다음 레벨을 분리한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 왜 Queue를 사용하는지, 그리고 for i in range(len(queue))가 어떻게 현재 레벨만 처리하는지 헷갈렸음.
- **복습 필요:** [O]

</details>

---


## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. --> 
모두 이진 트리를 순회하는 문제.
Maximum Depth와 Invert Binary Tree는 현재 노드에서 처리한 뒤 왼쪽·오른쪽 서브트리에 같은 작업을 반복하는 DFS + 재귀 패턴을 사용했다.
Level Order Traversal은 가까운 노드부터 레벨별로 탐색해야 하므로 BFS + Queue 패턴을 사용했다.

- 깊이 방향으로 내려가며 처리 → DFS / Recursion
- 레벨별로 왼쪽부터 처리 → BFS / Queue