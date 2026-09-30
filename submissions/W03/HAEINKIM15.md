<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W03 — 김해인

| | |
|---|---|
| **주차 주제** | String |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** |`#슬라이딩윈도우` `#해시맵` `#투포인터` `#팰린드롬` |

**한 줄 회고:**
문자열->substring으로 보는 다양한 경우를 생각해볼 것..
left/right으로 포인트로 탐색범위를 줄이거나 늘리는 경우를 생각.

---

## 3. Longest Substring Without Repeating Characters

**[문제 링크](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** · `Medium` · Python · `해설봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
- 입력: 문자열 `s` (`0 <= s.length <= 10^5`), 영문자·숫자·기호·공백을 포함할 수 있다.
- 출력: 중복 문자가 없는 가장 긴 연속 부분 문자열(substring)의 길이를 반환한다.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 모든 부분 문자열을 확인하면서 중복되는 문자가 있는지 검사. 
2. 한계: 가능한 substring을 모두 확인하면 입력 크기가 커질수록 비효율적이다.
3. 최종: `left`, `right`로 현재 구간을 관리하고 중복이 생기면 `left`를 이동시키는 Sliding Window를 사용한다.

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- `set`을 이용하면 현재 구간에 문자가 존재하는지 평균 `O(1)`에 확인할 수 있다.
- 중복 문자가 발생하면 중복이 사라질 때까지 `left`를 이동하여 중복 없는 구간을 유지한다

**복잡도**
- 시간: `O(n)` — `right`와 `left`가 각각 문자열을 최대 한 번씩 이동한다.
- 공간: `O(n)` — 최악의 경우 모든 문자가 서로 다르면 `set`에 최대 `n`개의 문자가 저장된다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- ["bbbbb"] 모든 문자가 같은 경우 -> 중복이 생길 때마다 `left`를 이동하여 `1` 반환
- ["abcd"] 모든 문자가 다른 경우 -> 전체 문자열이 유효한 구간이 되어 `4` 반환
- 빈 문자열 -> 초기값 `0` 반환

**코드**

```python
def lengthOfLongestSubstring(self, s):
    chars = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
      while s[right] in chars:
        chars.remove(s[left])
        left+=1
  
      chars.add(s[right])
      
      max_length =max(max_length,right-left+1)

    return max_length
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 --> 중복 없는 가장 긴 **연속 구간**을 구해야 한다면 `Sliding Window + Set`

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 242. Valid Anagram

**[문제 링크](https://leetcode.com/problems/valid-anagram/)** · `Easy` · python · `힌트봄`

**입출력**
- 입력: 영어 소문자로 이루어진 두 문자열 `s`, `t` (`1 <= s.length, t.length <= 5 * 10^4`)
- 출력: `t`가 `s`의 anagram이면 `True`, 아니면 `False`를 반환한다.

**접근**
1. 브루트포스: `s`의 각 문자가 `t`에 같은 개수만큼 존재하는지 하나씩 탐색한다.
2. 한계: 각 문자마다 `t`를 다시 탐색하면 문자열이 길어질수록 비효율적이다.
3. 최종: 두 개의 해시맵에 각 문자열의 `문자: 등장 횟수`를 저장한 뒤 두 해시맵을 비교한다.

**선택 근거**
- Anagram은 문자의 순서가 아니라 각 문자의 등장 횟수가 같은지가 중요하므로 `문자: 등장 횟수`를 저장할 수 있는 해시맵을 사용했다.

**복잡도**
- 시간: `O( )` —
- 공간: `O( )` —

**엣지 케이스**
- [rat,rats] 두 문자열의 길이가 다른 경우 -> 문자별 등장 횟수가 달라 `False` 
- [aab,aba] 같은 문자가 여러 번 등장하는 경우->각 문자의 등장 횟수가 같으니까 `True`
- [aab,abb] 문자 종류는 비슷하지만 등장 횟수가 다른 경우->해시맵의 value가 달라 `False`

**코드**

```python
class Solution(object):
    def isAnagram(self, s, t):
      count_t={}
      count_s={}
      
      for char in s:
        if char in count_s:
          count_s[char]+=1
        else:
          count_s[char]=1

      for char in t:
        if char in count_t:
          count_t[char]+=1
        else:
          count_t[char]=1
      
      return count_s == count_t

```

**다시 볼 때의 트리거**
>두 문자열에서 순서는 중요하지 않고, **각 원소의 등장 횟수**를 비교해야 한다면 Hash Map으로 빈도를 센다. 

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**각 문자의 개수를 해시맵에 저장하는 것까지는 구현했지만 두 해시맵을 비교하는 방법?
파이썬엣는 딕셔너리끼리 `==`를 사용해 key와 value가 같은지 바로 비교 가능.
- **복습 필요:** [O]

</details>

---


## 5. Longest Palindromic Substring

**[문제 링크](https://leetcode.com/problems/longest-palindromic-substring/)** · `Medium` · python · `해설봄`

**입출력**
- 입력: 영문자와 숫자로 이루어진 문자열 `s` (`1 <= s.length <= 1000`)
- 출력: `s`의 연속된 부분 문자열 중 가장 긴 팰린드롬 문자열을 반환한다.

**접근**
1. 브루트포스: 가능한 모든 부분 문자열을 만든 뒤 각각 앞뒤가 같은 팰린드롬인지 확인한다.
2. 한계: 모든 부분 문자열을 만들고 각각 팰린드롬인지 확인하면 반복적인 비교가 많이 발생해 비효율적이다.
3. 최종: 각 위치를 팰린드롬의 중심으로 잡고 `left`, `right`를 양쪽으로 확장하면서 가장 긴 팰린드롬을 찾는다.


**선택 근거**
- 팰린드롬은 중심을 기준으로 양쪽 문자가 대칭이라는 특징이 있으므로 중심에서 양쪽으로 확장하는 방식을 사용했다.
- 홀수 길이는 `left = i, right = i`, 짝수 길이는 `left = i, right = i + 1`로 두 경우를 모두 확인한다.


**복잡도**
- 시간: `O(n²)` — `n`개의 위치를 중심으로 확인하고, 각 중심에서 최악의 경우 문자열의 양 끝까지 확장한다.
- 공간: `O(n)` — 슬라이싱 `s[left+1:right]`으로 새로운 문자열을 생성해 `current`와 `longest`에 저장한다.


**엣지 케이스**
- [a] 문자의 길이가 1인 경우 -> 문자 하나 자체가 팰린드롬이므로 `a`반환
- [babad] 홀수길이 팰린드롬 -> 한 문자를 중심으로 확장하며 `bab`또는 `aba`반환
- [cbbd] 짝수 길이 팰린드롬 -> 두 문자 사이를 중심으로 확장하여 `bb`반환

**코드**

```python
class Solution(object): 
    def longestPalindrome(self, s): 
 
        longest="" 
         
        for i in range(len(s)): 
            left=i 
            right=i 
 
            while left>=0 and right < len(s) and s[left]==s[right]: 
                left-=1 
                right+=1 
             
            current=s[left+1:right] 
 
            if len(current) > len(longest): 
                longest=current 
             
            left=i 
            right=i+1 
             
            while left>=0 and right<len(s) and s[left]==s[right]: 
                left-=1 
                right+=1 
             
            current = s[left + 1:right] 
 
            if len(current) > len(longest): 
                longest = current 
 
        return longest 
```

**다시 볼 때의 트리거**
> 가장 긴 팰린드롬을 찾는 문제라면 각 위치를 **중심으로 잡고 양쪽으로 확장하는 Expand Around Center**를 떠올린다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 처음에는 `left`, `right`를 양 끝처럼 사용하려 했고 홀수/짝수 팰린드롬을 `i`의 홀짝으로 구분하려 했다. 모든 `i`에서 홀수(`i, i`)와 짝수(`i, i+1`) 두 경우를 각각 확인해야 한다는 부분에서 막혔다.
- **복습 필요:** [x]
- **복습 필요:** [ ]

</details>

---


## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. --> 이번 세 문제에서는 문자열의 **연속된 구간, 문자 빈도, 대칭 구조**에 따라 서로 다른 접근을 사용했다.
- **Longest Substring Without Repeating Characters:** 중복 없는 연속 구간 → `Sliding Window + Set`
- **Valid Anagram:** 문자별 등장 횟수 비교 → `Hash Map`
- **Longest Palindromic Substring:** 중심을 기준으로 대칭 확인 → `Expand Around Center + Two Pointer`

문자열 문제를 만났을 때 바로 구현하기보다, 먼저 **중복을 관리해야 하는지 / 빈도를 세어야 하는지 / 양쪽을 비교해야 하는지**를 확인하고 그에 맞는 자료구조와 알고리즘을 선택하는 것이 중요!!
