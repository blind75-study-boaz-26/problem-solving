<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W02 — 최우성

| | |
|---|---|
| **주차 주제** | Array |
| **선언한 목표** | 2문제 |
| **실제로 푼 수** | 2문제 |
| **패턴 태그** | `#binary search` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->
binary search는 정렬된 배열에서 target을 찾을 때만 활용할 수 있는 것이 아니라, F/T 경계값을 찾을 때도 활용할 수 있다.

---

## 1. Find Minimum in Rotated Sorted Array

**[문제 링크](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)** · `Medium` · Python · `힌트봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- 길이 n인 배열이 주어지고, 1 <= n <= 5000로 입력의 크기는 작은 편
- 하지만 문제 조건에 O(logN)안에 해결하라고 명시되어있음

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
- 브루트포스: 
  - 모든 원소를 순차 탐색하면서 최소값을 갱신하는 방식
    - 한계: O(N)으로 O(logN)을 만족하지 못한다.
  - 다시 재정렬하는 방식
    - 한계: O(logN)을 만족하는 정렬 알고리즘이 존재하지 않음
- 최종: binary search

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 부분적으로 정렬된 배열
- O(logN)을 만족해야함
- 위의 두 키워드를 엮었을 때 binary search만 남는다.

**복잡도**
- 시간: `O(logN)`
- 공간: `O(1)`

**엣지 케이스** (최소 2개, 처리 방법까지)
- 길이가 1인 경우
- 최솟값이 마지막 인덱스인 경우

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums)
        # predicate: nums[-1] 이하
        # 목표: nums[-1] 이하가 되는 경계값 찾기
        # 미검증 구간: [lo, hi)
        # lo 미만 -> F
        # hi 이상 -> T
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] <= nums[-1]:
                hi = mid
            else:
                lo = mid + 1
            
        return nums[lo]

```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 --> 경계값을 묻는 문제에서는 binary search 를 활용할 수 있다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 2. Search in Rotated Sorted Array

**[문제 링크](https://leetcode.com/problems/search-in-rotated-sorted-array/)** · `Medium` · python · `힌트봄`

**입출력**
- 길이 n인 배열이 주어지고, 1 <= n <= 5000로 입력의 크기는 작은 편
- 하지만 문제 조건에 O(logN)안에 해결하라고 명시되어있음

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
- 브루트포스: 
  - 모든 원소를 순차 탐색하면서 최소값을 갱신하는 방식
    - 한계: O(N)으로 O(logN)을 만족하지 못한다.
  - 다시 재정렬하는 방식
    - 한계: O(logN)을 만족하는 정렬 알고리즘이 존재하지 않음
- 최종: binary search

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 부분적으로 정렬된 배열
- O(logN)을 만족해야함
- 위의 두 키워드를 엮었을 때 binary search만 남는다.

**복잡도**
- 시간: `O(logN)`
- 공간: `O(1)`

**엣지 케이스**
- 길이가 1인 경우
- 최솟값이 마지막 인덱스인 경우

**코드**

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= nums[-1]:
                hi = mid
            else:
                lo = mid + 1
        min_idx = lo

        if target <= nums[-1]:
            lo = min_idx
            hi = len(nums)
        else:
            lo = 0
            hi = min_idx
            
        while lo < hi:
            mid = (lo+hi) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
            
        return -1

```

**다시 볼 때의 트리거**
> loop invarient를 명확히 정의하자

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->
