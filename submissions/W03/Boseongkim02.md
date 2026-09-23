
# W03 — 김보성

| | |
|---|---|
| **주차 주제** | String |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#해시맵` `#카데인` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 125. Valid Palindrome

**[문제 링크](https://leetcode.com/problems/valid-palindrome/)** · `Easy` · Python · `힌트봄`

**입출력**
- 입력: 문자열 s (길이 1~2×10^5, printable ASCII 문자만 포함), 출력: 소문자 변환 및 non-alphanumeric 제거 후 앞뒤로 읽어도 같으면 True, 아니면 False

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 원본 문자열에서 곧바로 양 끝 인덱스의 원소를 비교
2. 한계: 원본 문자열에는 공백, 특수문자, 대소문자가 섞여 있어서 대응 위치가 맞지 않다.
3. 최종: 먼저, 알파벳과 숫자만 남긴 뒤, 대문자는 소문자로 변환한 후 그 문자열에서 양끝에서 좁혀나가는 식으로 비교한다.

**선택 근거**
- 별도 자료구조 없이 전처리한 문자열 하나만으로 문제가 해결 가능하다.

**복잡도**
- 시간: `O(n)` — 전처리에 한 번, 양 끝부터 비교에 한 번. 총 두 번의 독립된 선형 순회.
- 공간: `O(n)` — 필터링된 새 문자열을 저장하는 데 입력 크기 만큼의 추가 공간 사용.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 빈 문자열의 경우. ex- "" -> 필터링 후에도 "". for문이 아예 안 돌고 바로 True를 리턴
- [ ] 숫자가 포함된 경우. ex- "0P" -> isalnum()으로 숫자도 포함시켜 걸러지지 않게 한다.

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        for i in range(0, len(s)):
            if s[i] == s[len(s)-1-i]:
                pass
            else:
                return False
        return True
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 -->
Palindrome 문제는 먼저 조건에 맞게 전처리(필터링, 정규화)한 후에 양 끝에서부터 비교하는 방식으로 해결한다.
<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
처음에는 숫자 조건을 보지 못하여 isalpha()만 썼고, 비교 로직에서 첫 번째 비교만에 바로 return 해버리는 오류를 범하였다.
- **복습 필요:** [ ]

</details>

---

## 242. Valid Anagram

**[문제 링크](https://leetcode.com/problems/valid-anagram/)** · `Easy` · Python · `힌트봄`

**입출력**
- 입력: 문자열 s, t (각각 길이 1~5×10^4, 소문자 영어 알파벳만 포함), 출력: t가 s의 애너그램이면 True, 아니면 False

**접근**
1. 브루트포스: 두 문자열을 각각 정렬해서 완전히 같은지 비교 (O(n log n))
2. 한계: 정렬을 안 쓰고도 더 빠르게 O(n)으로 풀 수 있음
3. 최종: 애너그램은 같은 문자가 같은 개수만큼 있다는 뜻이므로, 딕셔너리 하나로 s의 문자는 +1, t의 문자는 -1 하며 카운트한 뒤 모든 값이 0인지 확인

**선택 근거**
- 딕셔너리는 각 문자의 등장 횟수를 key-value로 관리하며 O(1)에 조회·갱신 가능. defaultdict(int)를 사용해 처음 나온 문자에 접근해도 자동으로 0부터 시작하게 하여 KeyError를 방지

**복잡도**
- 시간: `O(n)` — s, t를 각각 한 번씩만 순회
- 공간: `O(k)` — k는 서로 다른 문자 종류 수. 소문자 영어로 제한되어 최대 26개이므로 사실상 O(1)에 가까움

**엣지 케이스**
- [ ] 길이가 다른 경우 (예: s="rat", t="ca") → 애초에 애너그램이 될 수 없으므로 순회 전에 길이 비교로 바로 False 반환
- [ ] 길이는 같지만 겹치지 않는 문자가 있는 경우 (예: s="rat", t="car") → t 순회 중 s에 없던 문자(c)가 카운트 -1로 새로 생기고, 마지막 all() 검사에서 0이 아닌 값이 걸려 False 판정

**코드**

```python
from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
        
        for c in t:
            count[c] -= 1
        
        return all(v == 0 for v in count.values())
```

**다시 볼 때의 트리거**
> 애너그램 판별은 문자별 등장 횟수를 하나의 딕셔너리에서 더하고 빼서, 마지막에 전부 0인지 확인한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** defaultdict 없이 일반 딕셔너리로 시도했을 때 처음 나온 문자에 접근하며 KeyError가 발생해 처리 방법을 고민했다. / 약 10분 소요
- **복습 필요:** [ ]
</details>

--- 
## 424. Longest Repeating Character Replacement

**[문제 링크](https://leetcode.com/problems/longest-repeating-character-replacement/description/)** · `Medium` · 언어 · `해설봄`

**입출력**
- 입력: 문자열 s (길이 1~10^5, 대문자 영어 알파벳만 포함), 정수 k (0~s.length). 출력: s 안의 문자를 최대 k번 다른 대문자로 바꿀 수 있을 때, 같은 문자로만 이루어진 부분 문자열의 최대 길이

**접근**
1. 브루트포스: 모든 부분 문자열을 다 확인하면서, 각 부분 문자열에서 가장 많이 나온 문자를 찾고 나머지를 바꾸는 데 필요한 횟수가 k 이하인지 확인 (O(n²) 이상)
2. 한계: s.length가 최대 10^5라 O(n²)은 시간 초과. 매번 부분 문자열을 통째로 다시 훑는 대신 효율적으로 갱신하는 방법 필요
3. 최종: 슬라이딩 윈도우(투 포인터) + 해시맵으로 윈도우 안의 문자별 개수를 추적. 윈도우 길이에서 윈도우 안 최다 등장 문자 개수(max_count)를 뺀 값이 "바꿔야 하는 횟수"이고, 이게 k를 넘으면 왼쪽 포인터를 줄여서 윈도우를 좁힘

**선택 근거**
- 해시맵으로 현재 윈도우 안의 문자별 등장 횟수를 O(1)에 갱신 가능. 매번 부분 문자열 전체를 다시 세지 않고, 포인터를 이동하며 개수만 증감시켜 효율적으로 처리

**복잡도**
- 시간: `O(n)` — right가 한 번씩만 오른쪽으로 이동하고, left도 전체적으로 최대 n번만 이동
- 공간: `O(1)` — count 딕셔너리는 대문자 알파벳 26개로 크기가 고정되어 사실상 상수 공간

**엣지 케이스**
- [ ] k=0인 경우 (예: "ABAB", k=0) → 바꿀 수 있는 횟수가 없으므로 이미 같은 문자로 연속된 가장 긴 구간만 찾아야 함(여기선 1)
- [ ] s 전체가 같은 문자로만 이루어진 경우 (예: "AAAA", k=1) → 바꿀 필요가 없으므로 윈도우가 끝까지 확장되어 s.length 전체가 답

**코드**

```python
class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_count = 0
        max_length = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            
            window_length = right - left + 1
            if window_length - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
```

**다시 볼 때의 트리거**
> 문자열에서 최대 k번 교체 후 가장 긴 동일 문자 구간은, 슬라이딩 윈도우로 (윈도우 길이 - 윈도우 내 최다 문자 개수)가 k를 넘는지 확인하며 찾는다. max_count는 줄이지 않아도 답에 영향 없다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 슬라이딩 윈도우 접근 자체는 힌트로 감을 잡았지만, max_count를 왼쪽 포인터가 이동해도 줄이지 않는 이유(이미 달성한 윈도우 길이보다 짧은 윈도우는 답 갱신에 영향을 주지 않는다는 논리)를 스스로 도출하지 못해 코드를 받아서 이해하는 방식으로 풀었다.
- **복습 필요:** []

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->
