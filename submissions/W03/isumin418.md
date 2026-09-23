<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W03 — 이수민

| | |
|---|---|
| **주차 주제** | string |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#해시맵` `#투포인터` `#카데인` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 1. Longest Substring Without Repeating Characters

**[문제 링크](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)** · `medium` · Python · `자력해결`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
-입력: 영문자, 숫자, 기호, 공백으로 구성된 문자열 s
-출력: 중복 문자가 없는 가장 긴 연속 부분 문자열의 길이

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 만들 수 있는 모든 연속 부분 문자열을 확인하고, 각 부분 문자열에 중복 문자가 있는지 검사함. 
2. 한계: 부분 문자열 개수 * 각 부분 문자열의 중복 검사 = O(n²) × O(n) = O(n³)
3. 최종: right을 이동하며 새로운 문자를 구간에 추가하고, 중복이 발생하면 중복이 사라질 때까지 left를 이동함. 매번 right - left + 1 로 현재 구간 길이를 계산해 최댓값을 갱신함. 

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 현재 구간에 포함된 문자를 set에 저장하면 중복 여부를 평균 O(1)에 확인할 수 있음. left와 right는 각각 문자열을 오른쪽으로 최대 한 번씩 지나감 -> 모든 부분 문자열을 확인하지 않고 가장 긴 구간 찾을 수 있음

**복잡도**
- 시간: `O(n)` — left와 right가 각 문자를 최대 한 번씩 추가하고 제거함
- 공간: `O(n)` — 최악의 경우 문자열의 모든 문자가 서로 달라 set에 최대 n개의 문자가 저장됨

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 빈 문자열("") 입력되면 0을 반환하는가: 문자열의 길이가 0 이므로 for 문이 한 번도 돌지 않음. max_length의 초기값인 0 그대로 반환함. 
- [ ] 모든 문자가 같은 경우 1을 반환하는가: 중복된 문자가 들어올 때마다 기존 문자를 제거하므로 구간의 길이가 항상 1로 유지되어 1 반환함. 

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left +1)
        
        return max_length
        
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 -->

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 2. Longest Repeating Character Replacement

**[https://leetcode.com/problems/longest-repeating-character-replacement/description/]()** · `medium` · python · `힌트 봄`

**입출력**
- 입력: 영어 대문자로만 이뤄진 문자열 s, 최대 변경 횟수 k (0 ≤ k ≤ s)
- 출력: 글자를 최대 k개 바꿔 같은 글자가 연속되게 만들 수 있는 가장 긴 구간의 길이 반환. 

**접근**
1. 브루트포스: 모든 연속 구간을 고르고, 각 구간의 글자 수를 처음부터 세어 필요한 변경 횟수를 확인함. 
2. 한계: 구간마다 글자를 세면 O(n³)으로 문자열 길이가 최대 10⁵일 때 너무 느림. 
3. 최종: 슬라이딩 윈도우로 구간을 늘리고 변경 횟수가 k를 넘으면 왼쪽을 줄이며 최대 길이를 기록함. 

**선택 근거**
- 딕셔너리: 구간에 글자가 들어오거나 빠질 때 개수를 바로 갱신하기 위해서 사용함. 배열도 가능하지만 대문자를 배열 인덱스로 변환해야 하므로 이 코드에서는 딕셔너리가 읽기 쉬움.

- 슬라이딩 윈도우: 반환 연속 구간의 최대 길이이고 조건을 넘으면 왼쪽을 줄여 탐색할 수 있어 모든 구간을 따로 확인하지 않아도 됨. 

**복잡도**
- 시간: `O(n)` — right와 left가 각각 최대 n번 이동하고, max(counts.values())는 대문자 최대 26종의 개수만 확인함. 
- 공간: `O(1)` — 딕셔너리에 저장되는 문자 종류가 최대 26개로 고정되어 있음. 

**엣지 케이스**
- [ ] k = 0: 글자를 바꿀 수 없으므로, 서로 다른 글자가 들어오면 left를 옮겨 같은 글자가 연속된 구간만 남긴다.
- [ ] k = len(s): 모든 글자를 바꿀 수 있으므로 구간을 줄이지 않고 문자열 전체 길이를 반환한다.

**코드**

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0 
        answer = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char,0)+1

            while (right - left + 1) - max(counts.values()) > k:
                left_char = s[left]
                counts[left_char] -= 1
                left += 1

            answer = max(answer, right - left +1 )
        return answer
        
```

**다시 볼 때의 트리거**
>

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

## 3. Valid Anagram

**[https://leetcode.com/problems/valid-anagram/description/]()** · `easy` · python · `힌트봄`

**입출력**
-입력: 길이 1~50,000인 소문자 영어 문자열 s
-출력: 두 문자열의 글자별 개수가 모두 같으면 true, 아니면 false

**접근**
1. 브루트포스:s의 각 글자와 일치하는 글자를 t에서 하나씩 찾아 사용한 것으로 표시
2. 한계:글자마다 t를 다시 탐색하면 최악의 경우 O(n²)
3. 최종:길이가 다르면 바로 false를 반환하고 길이가 같으면 글자별 개수를 세어 비교

**선택 근거**
- 순서가 아니라 글자별 개수가 같아야 하므로, 정렬 대신 딕셔너리로 개수를 센다. 정렬은 O(n log n)이지만 개수를 세면 O(n)이고 딕셔너리는 문자를 인덱스로 바꾸지 않고 바로 키로 사용할 수 있다. 

**복잡도**
- 시간: `O(n)` — 두 문자열을 각각 한 번씩 순회하며 글자 개수를 센다(n은 문자열 길이)
- 공간: `O(1)` — 딕셔너리에 저장할 수 있는 키는 영어 소문자 최대 26

**엣지 케이스**
- [ ]길이가 다른 경우: 글자 구성을 비교하기 전에 바로 false를 반환한다.
- [ ] 같은 글자가 중복되지만 횟수가 다른 경우("aab", "abb"): 글자별 개수를 비교해 false를 반환한다.

**코드**

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1  
        for char in t:
            if counts.get(char, 0) == 0:
                return False
            counts[char] -= 1

        return True
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