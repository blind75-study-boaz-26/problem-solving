# W08 — 권준희

| | |
|---|---|
| **주차 주제** | Matrix + Interval (이번 제출: Tree / String 복습) |
| **선언한 목표** | 미기록 |
| **실제로 푼 수** | 2문제 |
| **패턴 태그** | `#트리` `#DFS` `#재귀` `#투포인터` `#문자열` |

**한 줄 회고:**
트리의 깊이는 자식의 결과를 합쳐 계산하고, 문자열은 양끝 포인터를 이동하며 필요한 문자만 비교할 수 있다.

> 참고: 이 문서는 W08 폴더의 실제 풀이 2개를 기록합니다. `Maximum Depth of Binary Tree`는 W05, `Valid Palindrome`은 W03 문제로, W08 지정 문제 목록에는 없습니다. 선언한 목표, 결과 태그(`자력해결` / `힌트봄` / `해설봄`), LeetCode Accepted 여부는 기존 파일만으로 확인할 수 없어 미확인으로 남겼습니다.

---

## 1. Maximum Depth of Binary Tree

**[문제 링크](https://leetcode.com/problems/maximum-depth-of-binary-tree/)** · `Easy` · Python · `결과 태그 미확인`

**입출력**
- 이진 트리의 루트 `root`를 입력받아 루트부터 가장 먼 리프까지의 노드 수를 정수로 반환한다.
- 노드 수는 `0 ~ 10^4`, 노드 값은 `-100 ~ 100`이며, 빈 트리는 깊이 `0`으로 처리한다.

**접근**
1. 브루트포스: 루트에서 리프까지의 모든 경로를 저장한 뒤 가장 긴 경로의 길이를 구한다.
2. 한계: 깊이만 필요하므로 경로 자체를 저장할 필요가 없다.
3. 최종: 빈 노드이면 0, 그 외에는 왼쪽·오른쪽 깊이의 최댓값에 1을 더한다.

**선택 근거**
서브트리의 깊이도 같은 문제이므로 재귀 DFS로 자식의 결과를 받아 결합한다.

**복잡도**
- 시간: `O(n)` — 노드 n개를 각각 한 번 방문한다.
- 공간: `O(h)` — 높이 h만큼 재귀 스택을 사용하며 편향 트리에서는 최악 `O(n)`이다.

**엣지 케이스**
- [x] 빈 트리: `root is None`에서 `0`을 반환한다.
- [x] 루트만 있는 트리: 자식 깊이가 모두 `0`이므로 `1`을 반환한다.
- [x] 한쪽으로 치우친 트리: 긴 쪽의 깊이를 선택한다. 높이가 실행 환경의 재귀 한도를 넘으면 `RecursionError`가 발생할 수 있다.

**코드**

```python
#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=problem-list-v2&envId=oizxjoit
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
```

**다시 볼 때의 트리거**
> 트리 높이 → 빈 노드는 0, 현재 노드는 1 + 양쪽 서브트리 높이의 최댓값.

---

## 2. Valid Palindrome

**[문제 링크](https://leetcode.com/problems/valid-palindrome/)** · `Easy` · Python · `결과 태그 미확인`

**입출력**
- 문자열 `s`에서 영숫자만 남기고 대소문자를 무시했을 때 팰린드롬인지 불리언으로 반환한다.
- 입력은 길이 `1 ~ 2 * 10^5`의 출력 가능한 ASCII 문자로 구성된다. 영숫자가 하나도 없으면 `True`를 반환한다.

**접근**
1. 브루트포스: 영숫자만 추려 소문자로 변환한 문자열을 만들고 역순 문자열과 비교한다.
2. 한계: 필터링한 문자열과 역순 복사에 입력 길이에 비례하는 추가 공간이 필요하다.
3. 최종: 양끝 포인터로 영숫자가 아닌 문자를 건너뛰고 소문자로 비교하며 안쪽으로 이동한다.

**선택 근거**
양끝 문자만 비교하면 되므로 원본 문자열을 가리키는 인덱스 두 개로 처리할 수 있다.

**복잡도**
- 시간: `O(n)` — 두 포인터가 각각 한 방향으로만 이동한다.
- 공간: `O(1)` — 포인터 두 개와 개별 문자 비교만 사용한다.

**엣지 케이스**
- [x] 공백·기호만 있는 문자열: 문자를 건너뛰다 포인터가 만나면 `True`를 반환한다.
- [x] 대소문자가 섞인 문자열: `.lower()`로 변환한 값을 비교한다.
- [x] 양끝 유효 문자가 다른 경우: 즉시 `False`를 반환한다.

**코드**

```python
#https://leetcode.com/problems/valid-palindrome/?envType=problem-list-v2&envId=oizxjoit
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
```

**다시 볼 때의 트리거**
> 문자열 팰린드롬 → 양끝 투 포인터, 불필요한 문자 건너뛰기, 대소문자 통일.
