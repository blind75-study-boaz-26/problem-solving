<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W04 — 박소현

| | |
|---|---|
| **주차 주제** | Hashing / Stack |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#set` `#해시맵` `#스택` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 217. Contains Duplicate

**[문제 링크](https://leetcode.com/problems/contains-duplicate/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: 정수들이 들어있는 배열 `nums`
- 출력: 중복된 숫자가 하나라도 있으면 `True`, 모두 다르면 `False`

**접근**
1. 브루트포스: 숫자 하나를 잡고 뒤에 있는 모든 숫자와 비교한다.
2. 한계: 최악의 경우 모든 숫자를 서로 비교해야 해서 `O(n²)`이 걸린다.
3. 최종: 지금까지 나온 숫자를 `set`에 저장하고, 이미 들어있는 숫자가 다시 나오면 바로 `True`를 반환한다.

**선택 근거**
- 필요한 것은 숫자의 위치가 아니라 **이미 나온 숫자인지 여부**이다.
- `set`은 특정 값이 들어있는지 평균 `O(1)`에 확인할 수 있다.

**복잡도**
- 시간: `O(n)` — 배열을 한 번 순회한다.
- 공간: `O(n)` — 최악의 경우 모든 숫자를 `set`에 저장한다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] `[1]` → 비교할 다른 숫자가 없으므로 `False`
- [ ] `[1, 1]` → 두 번째 `1`이 이미 `set`에 있으므로 `True`
- [ ] `[-1, -2, -1]` → 음수도 동일하게 저장되므로 `True`

**코드**

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False
```

**다시 볼 때의 트리거**
> 배열에서 **중복된 값이 있는지만 확인**해야 한다 → `set`

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---
## 20. Valid Anagram

**[문제 링크](https://leetcode.com/problems/valid-anagram/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: 두 문자열 `s`, `t`
- 출력: 두 문자열에 들어있는 문자와 각 문자의 개수가 같으면 `True`, 아니면 `False`

**접근**
1. 브루트포스: `s`의 문자 하나하나가 `t`에 존재하는지 찾아서 비교한다.
2. 한계: 같은 문자가 여러 번 등장할 수 있기 때문에 단순히 존재 여부만 확인해서는 정확하게 판단할 수 없다.
3. 최종: 해시맵에 `s`의 각 문자가 몇 번 등장했는지 저장하고, `t`를 돌면서 해당 개수를 하나씩 감소시킨다.

**선택 근거**
- 애너그램에서는 문자의 순서가 아니라 **각 문자의 등장 횟수**가 중요하다.
- `dict`를 사용하면 `문자 : 등장 횟수` 형태로 저장할 수 있다.

**복잡도**
- 시간: `O(n)` — 문자열을 순회하면서 문자 개수를 확인한다.
- 공간: `O(k)` — 서로 다른 문자의 종류만큼 해시맵에 저장한다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] `"a"` / `"ab"` → 길이가 다르므로 바로 `False`
- [ ] `"anagram"` / `"nagaram"` → 각 문자 개수가 같으므로 `True`
- [ ] `"aacc"` / `"ccac"` → `a`와 `c`의 개수가 다르므로 `False`

**코드**

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True
```

**다시 볼 때의 트리거**
> 문자열의 **순서는 상관없고 각 문자의 개수가 같은지** 확인한다 → 해시맵으로 빈도수 세기

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 242. Valid Anagram

**[문제 링크](https://leetcode.com/problems/valid-anagram/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: 두 문자열 `s`, `t`
- 출력: 두 문자열에 들어있는 문자와 각 문자의 개수가 같으면 `True`, 아니면 `False`

**접근**
1. 브루트포스: `s`의 문자 하나하나가 `t`에 존재하는지 찾아서 비교한다.
2. 한계: 같은 문자가 여러 번 등장할 수 있기 때문에 단순히 존재 여부만 확인해서는 정확하게 판단할 수 없다.
3. 최종: 해시맵에 `s`의 각 문자가 몇 번 등장했는지 저장하고, `t`를 돌면서 해당 개수를 하나씩 감소시킨다.

**선택 근거**
- 애너그램에서는 문자의 순서가 아니라 **각 문자의 등장 횟수**가 중요하다.
- `dict`를 사용하면 `문자 : 등장 횟수` 형태로 저장할 수 있다.

**복잡도**
- 시간: `O(n)` — 문자열을 순회하면서 문자 개수를 확인한다.
- 공간: `O(k)` — 서로 다른 문자의 종류만큼 해시맵에 저장한다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] `"a"` / `"ab"` → 길이가 다르므로 바로 `False`
- [ ] `"anagram"` / `"nagaram"` → 각 문자 개수가 같으므로 `True`
- [ ] `"aacc"` / `"ccac"` → `a`와 `c`의 개수가 다르므로 `False`

**코드**

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True
```

**다시 볼 때의 트리거**
> 문자열의 **순서는 상관없고 각 문자의 개수가 같은지** 확인한다 → 해시맵으로 빈도수 세기

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 20. Valid Parentheses

**[문제 링크](https://leetcode.com/problems/valid-parentheses/)** · `Easy` · Python · `해설봄`

**입출력**
- 입력: `()`, `{}`, `[]` 종류의 괄호로 이루어진 문자열 `s`
- 출력: 모든 괄호가 올바른 순서와 종류로 닫히면 `True`, 아니면 `False`

**접근**
1. 브루트포스: 문자열에서 `()`, `{}`, `[]`를 계속 찾아서 제거한다.
2. 한계: 문자열을 반복해서 탐색하고 수정해야 해서 비효율적이다.
3. 최종: 여는 괄호는 `stack`에 넣고, 닫는 괄호가 나오면 가장 최근에 넣은 여는 괄호와 짝이 맞는지 확인한다.

**선택 근거**
- 가장 마지막에 열린 괄호가 가장 먼저 닫혀야 한다.
- 즉 **나중에 들어온 것이 먼저 나가는 LIFO 구조**이므로 `stack`이 적합하다.

**복잡도**
- 시간: `O(n)` — 문자열을 처음부터 끝까지 한 번 확인한다.
- 공간: `O(n)` — 최악의 경우 모든 여는 괄호가 stack에 들어간다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] `")("` → 닫는 괄호가 먼저 나오는데 stack이 비어 있으므로 `False`
- [ ] `"(]"` → 여는 괄호와 닫는 괄호 종류가 다르므로 `False`
- [ ] `"((("` → 반복이 끝난 뒤 stack에 괄호가 남아 있으므로 `False`
- [ ] `"()[]{}"` → 모든 괄호가 정상적으로 짝을 이루므로 `True`

**코드**

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in pairs:
                if not stack:
                    return False

                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

            else:
                stack.append(char)

        return len(stack) == 0
```

**다시 볼 때의 트리거**
> **가장 최근에 들어온 값을 먼저 확인해야 한다** → `stack`

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---