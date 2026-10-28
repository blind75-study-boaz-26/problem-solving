# W06 — 최우성

| | |
|---|---|
| **주차 주제** | Tree 심화 + Trie |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `Tree`, `Depth-First Search`, `Binary Search Tree`, `Binary Tree`, `Trie` |

**한 줄 회고:**
- BST를 inorder(DFS)로 순회하면 오름차순이 된다.

---

## 230. Kth Smallest Element in a BST

**[문제 링크](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)** · `Medium` · Python · `힌트봄`

**입출력**
- Input: `root = [5,3,6,2,4,null,null,1], k = 3`
- Output: `3`
- Constraints
  - 트리의 노드 수는 `n`
  - `1 <= k <= n <= 10^4`
  - `0 <= Node.val <= 10^4`

**접근**
1. 첫 접근: DFS로 완전 탐색하면서 크기가 k인 heap을 들고 다니기.
   - 답은 나오지만 모든 노드를 탐색해야 함.
2. 최종: BST의 성질을 사용하면 k번째 방문에서 답을 찾을 수 있음.
   - inorder로 순회하면 오름차순이 되기 때문.

**선택 근거**
- BST를 inorder로 순회하면 오름차순이라, k번째로 방문한 노드가 곧 답임.
- heap 같은 추가 자료구조 없이 순회 순서만으로 풀리고, 답을 찾는 즉시 멈출 수 있음.

**복잡도**
- 시간: `O(H + k)` — 가장 왼쪽 노드까지 H만큼 내려간 뒤 k개를 방문하고 멈춤. 편향 트리면 최악 `O(n)`
- 공간: `O(H)` — 재귀 호출 스택. 균형 트리면 `O(log n)`, 편향 트리면 `O(n)`

**엣지 케이스**
- 빈 트리, k > n: 제약상(`1 <= k <= n`) 나오지 않으므로 처리 불필요.
- **답이 `0`인 경우** (`Node.val`이 0일 수 있음): 종료 판정을 `if res:`로 하면 0을 "못 찾음"으로 오인함 → `res is not None`으로 비교해서 처리.
- **k = n** (가장 큰 값): 조기 종료가 안 되고 전체를 순회함. 결과는 정상, 최악 시간 `O(n)`.
- **한쪽으로 치우친 트리** (n = 10^4): 재귀 깊이가 10^4까지 감. LeetCode에선 통과했지만 Python 기본 재귀 한도(1000)를 넘는 깊이라, 일반 환경이면 스택을 쓰는 반복문 inorder가 안전함.

**코드**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        count = 0
        res = None

        def dfs(root):
            nonlocal count, res
            # 종료 조건
            if root is None or res is not None:
                return

            dfs(root.left)

            if res is not None:
                return

            count += 1

            if count == k:
                res = root.val
                return

            dfs(root.right)

        dfs(root)

        return res

```

**다시 볼 때의 트리거**
> BST에서 "k번째 / 정렬 순서"를 물으면 → inorder 순회 + 카운터, 찾으면 바로 멈추기.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]
- **메모**
  - DFS 재귀함수를 설계할 때 먼저 정해야 할 것: 무엇을 받아서 무엇을 리턴할 것인가?
  - 같은 DFS 문제라도 성격에 따라 값을 전달하는 적절한 방식이 있다.
    - 파라미터로 전달
    - 전역변수로 전달
    - 리턴 값으로 전달

</details>

---

## 105. Construct Binary Tree from Preorder and Inorder Traversal

**[문제 링크](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)** · `Medium` · Python · `힌트봄`

**입출력**
- Input: `preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]`
- Output: `[3,9,20,null,null,15,7]`
- Constraints
  - `1 <= preorder.length <= 3000`
  - `inorder.length == preorder.length`
  - `-3000 <= preorder[i], inorder[i] <= 3000`
  - 모든 값은 중복 없음 (unique)
  - `inorder`의 값은 모두 `preorder`에도 존재
  - 두 배열은 같은 트리의 올바른 preorder / inorder 순회 결과임이 보장됨

**접근**
1. 브루트포스: preorder의 첫 값이 루트 → inorder에서 그 값을 선형 탐색해 왼쪽/오른쪽으로 나누고, 배열을 슬라이싱해서 재귀.
2. 한계: 재귀마다 inorder 선형 탐색 + 슬라이싱 복사가 일어나서 최악 `O(n^2)`.
3. 최종: inorder의 값 → 인덱스를 해시맵에 미리 저장하고, 배열 대신 인덱스 구간(`s_p, e_p, s_i, e_i`)만 넘겨서 `O(n)`.

**선택 근거**
- preorder는 루트가 무엇인지, inorder는 왼쪽/오른쪽 서브트리의 경계를 알려줌 → 두 정보를 합쳐 분할 정복.
- 루트의 inorder 위치를 `O(1)`에 찾으려고 해시맵을 씀 (값이 unique라서 가능).

**복잡도**
- 시간: `O(n)` — 해시맵 구축 `O(n)` + 각 노드를 한 번씩 생성하며 inorder 위치는 해시맵으로 `O(1)` 조회
- 공간: `O(n)` — 해시맵 `O(n)` + 재귀 스택 `O(H)` (편향 트리면 최악 `O(n)`)

**엣지 케이스**
- **왼쪽 서브트리가 없는 경우** (inorder에서 루트가 구간 맨 앞): `len_of_left_sub_tree = 0`이 되어 왼쪽 호출 구간이 `s_p+1 > new_e_p`로 비어 있게 됨 → 종료 조건에서 `None` 반환. 오른쪽만 있는 경우도 같은 방식으로 처리됨.
- **노드 1개**: 양쪽 재귀 모두 빈 구간이라 바로 `None`. 별도 분기 필요 없음.
- **중복 값**: 해시맵(값 → 인덱스)이 성립하려면 값이 유일해야 함. 제약에서 unique를 보장하므로 처리 불필요.
- **한쪽으로 치우친 트리** (n = 3000): 재귀 깊이 3000. 230과 같이 Python 기본 재귀 한도를 넘는 깊이.

**코드**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # key: 노드 값
        # value: 인덱스
        inorder_dict = {}

        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        def find_root(s_p, e_p, s_i, e_i):
            # 없는 노드 처리
            if s_p > e_p or s_i > e_i:
                return None
            # root
            root_value = preorder[s_p]
            root = TreeNode(root_value)

            root_index_in_inorder = inorder_dict[root_value]

            len_of_left_sub_tree = root_index_in_inorder - s_i


            new_e_p = s_p + len_of_left_sub_tree
            new_e_i = s_i + len_of_left_sub_tree - 1
            

            root.left = find_root(s_p+1, new_e_p, s_i, new_e_i)
            root.right = find_root(new_e_p+1, e_p, root_index_in_inorder + 1, e_i)
            
            return root

        return find_root(0, len(preorder) - 1, 0, len(preorder) - 1)

```

**다시 볼 때의 트리거**
> preorder 첫 값 = 루트, inorder에서 루트 위치 = 왼쪽 서브트리 크기 → 그 크기로 두 배열을 같이 자른다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 208. Implement Trie (Prefix Tree)

**[문제 링크](https://leetcode.com/problems/implement-trie-prefix-tree/)** · `Medium` · Python · `힌트봄`

**입출력**

```text
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
```

```java
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

- Constraints
  - `1 <= word.length, prefix.length <= 2000`
  - `word`, `prefix`는 영어 소문자로만 구성
  - `insert`, `search`, `startsWith` 호출은 총 최대 `3 * 10^4`회

**접근**
1. 브루트포스: 단어를 set에 저장. `search`는 `O(L)`이지만 `startsWith`는 모든 단어를 훑으며 접두사를 비교해야 해서 `O(N·L)`.
2. 한계: 호출이 최대 `3 * 10^4`번인데, `startsWith`마다 저장된 단어 전체를 훑어야 함.
3. 최종: 글자 하나를 노드 하나로 두는 트리(Trie)에 저장. 같은 접두사는 같은 경로를 공유하므로 `search`/`startsWith` 모두 `O(L)`. 단어의 끝은 `is_end`로 표시.

**선택 근거**
- 접두사 질의가 핵심이라, 같은 접두사를 한 경로로 공유하는 Trie가 맞음.
- 자식 노드는 dict로 관리 (소문자 26개뿐이라 길이 26 배열도 가능).

**복잡도** (`L` = 단어/접두사 길이)
- 시간: `O(L)` — `insert`, `search`, `startsWith` 모두 글자 하나당 딕셔너리 조회/삽입 `O(1)`
- 공간: `insert`는 최악 `O(L)` (새 노드 L개 생성), `search`/`startsWith`는 `O(1)`. 트라이 전체는 삽입된 글자 수 총합에 비례

**엣지 케이스**
- **경로는 있지만 단어로 끝나지 않는 경우** ("apple"만 넣고 `search("app")`): 경로를 끝까지 따라가도 마지막 노드의 `is_end`가 False → `False`. 이 문제의 핵심 케이스.
- **완성된 단어로 `startsWith` 호출** (`startsWith("apple")`): `is_end`를 보지 않으므로 `True`. 단어 자체도 자기 자신의 접두사로 취급됨.
- **이미 있는 단어를 다시 `insert`**: 기존 노드를 따라가서 `is_end = True`만 다시 설정됨. 노드가 중복 생성되지 않음.
- 빈 문자열: 제약상(`length >= 1`) 나오지 않으므로 처리 불필요.

**코드**

```python
class Trie:

    def __init__(self):
        self.child = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Trie()
            cur = cur.child[ch]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return True if (cur.is_end == True) else False

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for ch in prefix:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```

**다시 볼 때의 트리거**
> 접두사(prefix) 검색이 나오면 Trie. `search`와 `startsWith`의 차이는 마지막에 `is_end`를 확인하느냐 하나뿐.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 이번 주 패턴 정리 (선택)

세 문제 모두 "트리를 어떤 순서로 보느냐"가 핵심이었음. 230은 BST의 inorder가 곧 정렬 순서라는 점을, 105는 preorder(루트 먼저)와 inorder(왼쪽-루트-오른쪽)의 성질을 조합해 트리를 복원하는 점을 이용함. 208은 문자열을 트리의 경로로 보는 문제. 재귀 DFS에서 값을 전달하는 방식도 문제마다 달랐음. 230은 `nonlocal` 변수로 결과를 모았고, 105는 서브트리를 리턴 값으로 받아 붙였음.
