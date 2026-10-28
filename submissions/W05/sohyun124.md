<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W05 — 박소현

| | |
|---|---|
| **주차 주제** | Tree |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#트리` `#재귀` `#DFS` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 104. Maximum Depth of Binary Tree

**[문제 링크](https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/2164246755/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: 이진 트리의 루트 노드 `root`
- 출력: 루트에서 가장 깊은 리프 노드까지의 최대 깊이

**접근**
1. 브루트포스: 루트에서 시작해서 각 경로를 따라가며 깊이를 직접 계산한다.
2. 한계: 트리는 왼쪽과 오른쪽으로 계속 나뉘기 때문에 각 경로를 따로 관리하기보다 서브트리 단위로 계산하는 것이 효율적이다.
3. 최종: 왼쪽 서브트리와 오른쪽 서브트리의 최대 깊이를 각각 구하고, 더 큰 값에 현재 노드의 깊이 `1`을 더한다.

**선택 근거**
- 트리는 왼쪽 서브트리와 오른쪽 서브트리로 나눌 수 있다.
- 각 서브트리에서도 똑같이 최대 깊이를 구해야 하므로 재귀를 사용한다.

**복잡도**
- 시간: `O(n)` — 모든 노드를 한 번씩 방문한다.
- 공간: `O(h)` — 재귀 호출 스택에 트리의 높이만큼 저장된다. 최악의 경우 `O(n)`이다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 빈 트리 → 노드가 없으므로 `0` 반환
- [ ] 노드가 하나뿐인 트리 → 루트 하나이므로 `1` 반환
- [ ] 한쪽으로만 이어진 트리 → 존재하는 방향으로 계속 재귀하여 깊이를 계산

**코드**

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
```

**다시 볼 때의 트리거**
> 트리에서 **최대 깊이**를 구한다 → 왼쪽/오른쪽 깊이를 구하고 `1 + max(left, right)`

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 226. Invert Binary Tree

**[문제 링크](https://leetcode.com/problems/invert-binary-tree/submissions/2164248095/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: 이진 트리의 루트 노드 `root`
- 출력: 모든 노드의 왼쪽과 오른쪽 자식이 뒤집힌 트리

**접근**
1. 현재 노드의 왼쪽 자식과 오른쪽 자식을 서로 바꾼다.
2. 루트만 바꾸면 아래의 노드들은 그대로이므로 모든 노드에서 같은 작업을 해야 한다.
3. 최종: 현재 노드의 왼쪽과 오른쪽을 바꾼 뒤, 왼쪽과 오른쪽 서브트리에서도 같은 작업을 재귀적으로 반복한다.

**선택 근거**
- 모든 노드에서 왼쪽과 오른쪽을 바꾸는 동일한 작업이 반복된다.
- 왼쪽과 오른쪽 서브트리도 각각 하나의 트리이므로 재귀를 사용할 수 있다.

**복잡도**
- 시간: `O(n)` — 모든 노드를 한 번씩 방문한다.
- 공간: `O(h)` — 재귀 호출 스택에 트리 높이만큼 저장된다. 최악의 경우 `O(n)`이다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 빈 트리 → 뒤집을 노드가 없으므로 `None` 반환
- [ ] 노드가 하나뿐인 트리 → 자식이 없으므로 그대로 반환
- [ ] 한쪽 자식만 존재 → 왼쪽 자식은 오른쪽으로, 오른쪽 자식은 왼쪽으로 이동

**코드**

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

**다시 볼 때의 트리거**
> 트리의 **모든 노드에서 같은 작업을 반복**한다 → 현재 노드 처리 후 왼쪽/오른쪽에 재귀

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 100. Same Tree

**[문제 링크](https://leetcode.com/problems/same-tree/submissions/2164249395/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: 두 이진 트리의 루트 노드 `p`, `q`
- 출력: 두 트리의 구조와 각 노드의 값이 모두 같으면 `True`, 아니면 `False`

**접근**
1. 현재 위치에 있는 두 노드의 값을 비교한다.
2. 현재 노드의 값만 같다고 두 트리가 같은 것은 아니므로 자식 노드들도 확인해야 한다.
3. 최종: 현재 노드를 비교한 뒤 왼쪽 자식끼리, 오른쪽 자식끼리 재귀적으로 비교한다.

**선택 근거**
- 두 트리가 같으려면 현재 노드의 값뿐만 아니라 전체 구조도 같아야 한다.
- 왼쪽 서브트리끼리, 오른쪽 서브트리끼리 같은 방식으로 계속 비교할 수 있으므로 재귀를 사용한다.

**복잡도**
- 시간: `O(n)` — 최대 모든 노드를 한 번씩 비교한다.
- 공간: `O(h)` — 재귀 호출 스택에 트리 높이만큼 저장된다. 최악의 경우 `O(n)`이다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 두 노드가 모두 `None` → 같은 위치에 노드가 없으므로 `True`
- [ ] 한쪽 노드만 `None` → 트리의 구조가 다르므로 `False`
- [ ] 두 노드의 값이 다름 → 같은 트리가 아니므로 `False`
- [ ] 값은 같지만 자식의 위치가 다름 → 왼쪽끼리, 오른쪽끼리 비교하므로 `False`

**코드**

```python
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
```

**다시 볼 때의 트리거**
> **두 트리의 구조와 값이 같은지** 확인한다 → 현재 노드 비교 + 왼쪽끼리/오른쪽끼리 재귀

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---