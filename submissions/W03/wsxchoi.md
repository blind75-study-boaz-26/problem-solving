<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W03 — 최우성

| | |
|---|---|
| **주차 주제** | String |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#해시맵` `#Slinding-Window` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->


---

## 5. Longest Palindromic Substring

**[문제 링크](https://leetcode.com/problems/longest-palindromic-substring/)** · `Medium` · Python · `자력해결`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

> Given a string s, return the longest palindromic substring in s.

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- `1 <= s.length <= 1000` : O(N^2) 까진 가능하다.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 가능한 모든 부분 문자열 만들고, 각 문자열에 대해 Palindromic 검증
2. 한계: 가능한 모든 부분 문자열을 만들기 O(N^2), 각 부분 문자열마다 Palindromic 검증 O(N). O(N^3)으로 시간 초과.
3. 최종: 중심 확장 알고리즘을 사용해서 O(N^2)으로 줄인다.

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 중심 확장 알고리즘(Center Expansion Algorithm) : 부분 문자열을 만들지 않아도 된다. O(N^2) 만족 가능.

**복잡도**
- 시간: `O(N^2)`
- 공간: `O(1)` — l, r 포인터만 있으면 된다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [X] len(s)가 1인 경우

**코드**

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0,0)

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return (l+1,r-1)
        
        for i, ch in enumerate(s):
            # 홀수
            l, r = expand(i, i)
            if r-l > res[1] - res[0]:
                res = (l,r)
            # 짝수
            l, r = expand(i, i+1)
            if r-l > res[1] - res[0]:
                res = (l,r)
            
        return s[res[0]:res[1]+1]

```

**다시 볼 때의 트리거**
> Palindrome -> 중심 확장

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 3. Longest Substring Without Repeating Characters

**[문제 링크](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** · `Medium` · python · `자력해결`

> Given a string s, find the length of the longest substring without duplicate characters.

**입출력**
- `0 <= s.length <= 10^5`: O(N^2)는 불가능
- s consists of English letters, digits, symbols and spaces. 유한한 문자집합.

**접근**
1. Set 도입(시작점 고정): 시작점을 고정하고 끝 포인터를 늘려가며 등장한 문자를 Set에 추가한다. 중복이 발생하면 더 볼 필요 없기 때문에 시작점을 오른쪽으로 이동시킨다. O(N^2)인 것 같지만, 입출력 제약 중 `s consists of English letters, digits, symbols and spaces.`이 있었다. 문자 집합 크기는 약 95정도로, 시작점에서 95칸 이상 떨어지면 무조건 중복이 발생할 수 밖에 없고, 다음 시작점으로 넘어간다.(비둘기집 원리) 따라서 O(N)이라고 할 수 있다.
2. 개선 방식: 시작점을 고정할 필요가 없다. Sliding Window 알고리즘을 사용해서 중복 문자가 등장하면 left pointer를 중복이 없어질 때까지 오른쪽으로 밀면 된다. 위와 같은 O(N)이지만 연산이 더 적다.
3. 최종: Sliding Window + Set

**선택 근거**
- Set: 중복을 검사해야하기 때문에 필수적.
- Sliding Window: 이전 단계에서 얻은 정보를 버리지 않는다. 더 적은 연산이 가능하다.

**복잡도**
- 시간: `O(N)`
- 공간: Set의 크기에 따라 결정된다. `O(N)` 같지만 엄밀히 말하면 `O(min(N,K))`이다. (K는 문자집합의 크기) 이 때 K가 약 95이므로 O(1)이라 할 수 있다.

**엣지 케이스**
- [X] len(s)가 0인 경우 

**코드**

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        longest = 0
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            # 이제 add 가능한 상태
            seen.add(ch)
            # 최대 길이 갱신
            longest = max(longest, r-l+1)

        return longest

```

**다시 볼 때의 트리거**
> 이전 단계 정보를 잘 활용한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 76. Minimum Window Substring

**[문제 링크](https://leetcode.com/problems/minimum-window-substring/)** · `Hard` · python · `힌트봄`

> Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "". The testcases will be generated such that the answer is unique.

**입출력**
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`: O(N^2)이나 O(MN)은 지양
- `s and t consist of uppercase and lowercase English letters.`

**접근**
- 첫 풀이
  - hash map 도입: target의 문자를 모두 포함하는지 검증하려면 현재 얼마나 만족했는지 기록해둔 자료구조가 있어야한다. target이 "abc"라고 할 때, `state = {"a":1, "b":1, "c":1}` 같은 카운터 맵을 만들어두고, 현재 윈도우 안에 해당 문자가 등장할 때 마다 횟수를 차감한다. `state = {"a":0, "b":0, "c":0}`이 되면 조건을 만족했다는 뜻이다. 즉 value는 `target에서의 개수 - 현재 윈도우 안에서의 개수`.
  - sliding window: O(N^2)이 불가능 하기 때문에 브루트 포스로 substring을 모두 만들어보는 건 불가능하다. sliding window를 활용해서 O(N)으로 줄여야함.
  - 매 윈도우마다 `hash map의 모든 원소가 0 이하인가?`를 검증한다. 이때 만약 만족한다면 길이를 갱신하고, 만족하지 않을 때까지 윈도우를 줄이는 것을 반복한다.
  - 한계: 그러나 검증 과정에서 hash map의 모든 원소를 보는 것은 비효율적이다. 문자 집합은 52개로 key의 개수는 최대 52개이다. 상수 시간이라 O(52N) -> O(N)이긴 하지만, 검증 과정을 더 줄일 수 있다.

- 두번째 풀이
  - 검증 과정을 비교 한번으로 끝낸다.
  - `hash map의 모든 원소가 0 이하인가?` 라는 정보를 remaining이라는 변수 하나로 압축한다. remaining은 hash map의 모든 value의 합이다. remaining == 0이면 조건을 만족하는 형태로 바뀌게 된다.

**선택 근거**
- Hash Map: 카운터 맵을 만들기 위해 가장 적절하다.
- Sliding Window: 이전 단계에서 얻은 정보를 버리지 않는다. 더 적은 연산이 가능하다.

**복잡도**
- 시간: `O(N)`
- 공간: hash map의 크기에 따라 결정된다. 문자 종류가 52개라, key 공간이 52로 제한된다. 따라서 `O(N)`

**엣지 케이스**
- [X] len(s)가 0인 경우 
- [X] target에 같은 문자가 2번 이상 등장하는 경우

**코드**

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # init state map
        state = {}
        for ch in t:
            if ch not in state:
                state[ch] = 1
                continue
            state[ch] += 1
        
        remaining = len(t)
        window = (0,len(s))
        l = 0
        for r, ch in enumerate(s):
            if ch in state:
                if state[ch] > 0:
                    remaining -= 1
                state[ch] -= 1
                
            while remaining == 0:
                # updating sliding window size
                if (window[1]-window[0]) > r-l:
                    window = (l,r)
                # updating state map
                if s[l] in state:
                    # updating remaining
                    if state[s[l]] >= 0:
                        remaining += 1
                    state[s[l]] += 1
                # updating left pointer
                l += 1
        
        if window == (0,len(s)):
            return ""
        return s[window[0]:window[1]+1]
        
```

**다시 볼 때의 트리거**
> 이전 단계 정보를 잘 활용한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->
Sliding Window를 쓸 때, 무조건 O(N)이 아니다. 각 윈도우마다 돌리는 검증 로직이 O(N)이면 O(N^2)이 되어버린다. 검증 로직을 O(1)로 줄이기 위해서는 이전 윈도우에서 얻은 정보를 잘 활용하는 것이 중요하다.
