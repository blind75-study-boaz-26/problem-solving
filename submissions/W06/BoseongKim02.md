# W06 — 김보성

| | |
|---|---|
| **주차 주제** | Tree |
| **선언한 목표** | 2문제 |
| **실제로 푼 수** | 2문제 |
| **패턴 태그** | `#트리` `#BST` `#중위순회` `#재귀` |

**한 줄 회고:**
BST는 중위 순회하면 오름차순으로 방문되므로, 정렬 없이 순회 순서만으로 k번째 값을 찾을 수 있다.

---

## 230. Kth Smallest Element in a BST

**[문제 링크](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)** · `Medium` · Python · `힌트봄`

**입출력**
- 입력: BST의 root, 정수 k (1 ≤ k ≤ 노드 수 n). 출력: 노드 값 중 k번째로 작은 값 (k는 1부터 시작)

**접근**
1. 브루트포스: 모든 노드 값을 리스트에 담아 정렬한 뒤 list[k-1]을 반환 (O(n log n))
2. 한계: BST는 이미 정렬된 구조인데 그 성질을 쓰지 않고 다시 정렬하는 건 낭비
3. 최종: BST를 중위 순회(왼쪽 → 자신 → 오른쪽)하면 오름차순으로 방문되므로, 방문 횟수를 세다가 k번째 노드의 값을 기록

**선택 근거**
- BST의 "왼쪽 < 노드 < 오른쪽" 성질 때문에 중위 순회 = 오름차순 방문. 정렬 없이 순회만으로 k번째를 찾을 수 있고, 재귀가 트리 구조와 자연스럽게 맞음

**복잡도**
- 시간: `O(n)` — k번째를 찾은 뒤에도 순회를 멈추지 않고 모든 노드를 한 번씩 방문
- 공간: `O(h)` — 재귀 호출 스택이 트리 높이 h만큼 쌓임 (편향 트리면 O(n))

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] k = 1 (예: [3,1,4,null,2], k=1) → 왼쪽 끝까지 내려가 가장 먼저 방문하는 노드 1이 답
- [ ] k = n → 중위 순회의 마지막 방문 노드, 즉 가장 큰 값이 답
- [ ] 노드가 1개인 트리 → 왼쪽/오른쪽 재귀가 바로 종료되고 count=1이 되어 root 값을 반환

**코드**

```python
class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        self.ans = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)          # 빈칸 1: 왼쪽
            self.count += 1
            if self.count==k:               # 빈칸 2: 지금 노드가 k번째인 조건
                self.ans = node.val    # 빈칸 3: 기록할 값
            inorder(node.right)          # 빈칸 4: 오른쪽

        inorder(root)
        return self.ans
```

**다시 볼 때의 트리거**
> BST + k번째 → 중위 순회하면 오름차순. 왼쪽 재귀 → count 증가 → 오른쪽 재귀 순서가 핵심.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 중위 순회가 오름차순이라는 성질과 반복문 스택 뼈대를 힌트로 받았고, 재귀 빈칸은 스스로 채움. 내부 함수에서 count를 쓰려면 self. 또는 nonlocal이 필요하다는 점을 확인. / N분
- **복습 필요:** [ ]

</details>

---

## 208. Implement Trie(Prefix Tree)

**[문제 링크](https://leetcode.com/problems/implement-trie-prefix-tree/)** · `난이도` : Medium · Python · `해설봄`

**입출력**
- 입력: insert(word), search(word), startsWith(prefix) 메서드 호출 (문자열은 소문자 영어, 길이 1~2000, 호출 최대 3×10^4회). 출력: insert는 없음, search와 startsWith는 True/False

**접근**
1. 브루트포스: 삽입한 단어를 리스트(또는 set)에 저장해두고, search는 단어 일치 확인, startsWith는 모든 단어를 돌며 startswith로 접두사 비교
2. 한계: startsWith가 저장된 단어 수 n과 단어 길이 L에 비례해 O(n·L)이 걸림. 호출이 최대 3×10^4번이라 단어가 쌓이면 느려짐
3. 최종: 글자 하나를 노드로 하는 트라이(접두사 트리)를 만들고, 각 노드에 "단어의 끝" 표시를 둠. 경로 존재 여부로 startsWith를, 경로 + 끝 표시로 search를 처리

**선택 근거**
- 공통 접두사를 한 경로로 공유하므로 접두사 검색이 저장된 단어 수와 무관하게 단어 길이만큼만 걸림. 각 노드는 자식 딕셔너리(글자 → 노드)와 is_end 플래그를 가짐

**복잡도**
- 시간: `O(L)` — insert, search, startsWith 모두 문자열 길이 L만큼 글자를 한 칸씩 따라 내려감
- 공간: `O(N·L)` — 최악의 경우 삽입한 모든 글자가 각각 노드 하나를 차지 (N은 삽입한 단어 수, 접두사가 겹치면 줄어듦)

**엣지 케이스** (최소 2개, 처리 방법까지)
- "apple"만 삽입하고 search("app") → 경로는 존재하지만 "app" 끝 노드의 is_end가 False라 False 반환. startsWith("app")은 경로만 있으면 되므로 True
- "app" 삽입 후 "apple" 삽입 (접두사 단어가 나중에 들어오거나 먼저 들어오는 경우) → 같은 경로를 공유하고, "app" 끝 노드에 is_end=True가 별도로 켜져 둘 다 search 가능
- 존재하지 않는 글자가 중간에 나오는 경우 (예: "apple"만 있는데 search("apx")) → 자식 딕셔너리에 'x'가 없으므로 즉시 False 반환

**코드**

```python
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
```

**다시 볼 때의 트리거**
> 접두사 검색이 나오면 트라이: 글자별 노드 + 단어 끝 표시(is_end). search는 끝 표시까지, startsWith는 경로 존재만 확인.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 직접 풀지 못하고 해설로 확인함. search와 startsWith의 차이가 "단어 끝 표시(is_end)를 보느냐"에 있다는 점, 노드를 딕셔너리로 구현하는 방식을 해설에서 익힘. / N분
- **복습 필요:** []

</details>

---

## 이번 주 패턴 정리 (선택)