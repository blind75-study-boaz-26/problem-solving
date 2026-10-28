
# W06 — sohyun124

| | |
|---|---|
| **주차 주제** | Tree 심화 + Trie |
| **선언한 목표** | 2문제 |
| **실제로 푼 수** | 제출 전 작성 |
| **패턴 태그** | `#BST` `#중위순회` `#Trie` `#해시맵` |

**한 줄 회고:**
BST의 중위 순회는 값을 오름차순으로 방문하며, Trie는 문자별 노드를 연결해 접두어를 효율적으로 확인한다.

---

## 230. Kth Smallest Element in a BST

**[문제 링크](https://leetcode.com/problems/kth-smallest-element-in-a-bst/?envType=problem-list-v2&envId=oizxjoit)** · `Medium` · Python

**입출력**
- 입력: 이진 탐색 트리의 루트 `root`, 양의 정수 `k`
- 출력: 트리에서 `k`번째로 작은 값

**접근**
1. 브루트포스: 모든 노드의 값을 배열에 담고 정렬한 다음 `k-1`번째 값을 반환한다.
2. 한계: 정렬에 `O(n log n)` 시간이 필요하고, BST의 정렬 특성을 활용하지 못한다.
3. 최종: BST를 중위 순회(왼쪽 → 현재 → 오른쪽)하면 값이 오름차순으로 나오므로, `k`번째 방문한 값을 반환한다.

**선택 근거**
- BST에서는 왼쪽 자식의 값이 현재 노드보다 작고, 오른쪽 자식의 값은 크다.
- 중위 순회 순서가 곧 오름차순이므로 별도 정렬이 필요 없다.

**복잡도**
- 시간: `O(h + k)` — 반복형 중위 순회에서 최대 높이 `h`만큼 내려가고 `k`개 노드를 방문한다. 최악 `O(n)`.
- 공간: `O(h)` — 탐색 경로를 스택에 저장한다. 최악 `O(n)`.

**엣지 케이스**
- [ ] `root = [1], k = 1` → 첫 번째 노드 값 `1` 반환
- [ ] `root = [3,1,4,null,2], k = 1` → 중위 순회 첫 값 `1` 반환
- [ ] `root = [3,1,4,null,2], k = 4` → 중위 순회 마지막 값 `4` 반환

**코드**

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val

            current = current.right
```

**다시 볼 때의 트리거**
> **BST에서 k번째로 작은 값**을 찾는다 → 중위 순회로 오름차순 방문

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 208. Implement Trie (Prefix Tree)

**[문제 링크](https://leetcode.com/problems/implement-trie-prefix-tree/submissions/2183714534/)** · `Medium` · Python

**입출력**
- 입력: `insert(word)`, `search(word)`, `startsWith(prefix)` 연산
- 출력: `search`는 단어의 완전한 존재 여부, `startsWith`는 접두어 존재 여부를 불리언으로 반환

**접근**
1. 단순 접근: 삽입한 단어들을 리스트에 저장하고, 검색할 때마다 하나씩 비교한다.
2. 한계: 단어가 많아지면 검색할 때 전체 단어를 확인해야 한다.
3. 최종: 각 노드에 다음 문자로 연결되는 딕셔너리와 단어 종료 표시를 두어, 문자 단위로 탐색한다.

**선택 근거**
- 여러 단어가 동일한 접두어를 공유할 수 있다.
- Trie는 공통 접두어 경로를 재사용하고, 단어가 끝나는 위치를 별도로 표시한다.

**복잡도**
- 시간: `insert`, `search`, `startsWith` 모두 `O(L)` — 입력 문자열 길이 `L`만큼 탐색한다.
- 공간: 전체 저장 문자열 길이의 합을 `S`라고 하면 `O(S)` — 최악의 경우 각 문자마다 새 노드를 만든다.

**엣지 케이스**
- [ ] `insert("apple")`, `search("app")` → 접두어만 존재하므로 `False`
- [ ] `insert("apple")`, `startsWith("app")` → 접두어가 존재하므로 `True`
- [ ] `insert("app")`, `search("app")` → 단어 종료 표시가 있으므로 `True`

**코드**

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```

**다시 볼 때의 트리거**
> **단어의 존재 여부와 접두어 여부**를 구분해 빠르게 검색한다 → Trie + 단어 종료 표시

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>
