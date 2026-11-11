<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W08 — 최우성

| | |
|---|---|
| **주차 주제** | Matrix + Interval |
| **선언한 목표** | 1문제 |
| **실제로 푼 수** | 1문제 |
| **패턴 태그** | `#행렬` `#Set` `#마킹` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->
"You must do it in place." -> 파라미터로 받은 List를 그대로 활용해야한다는 말이다. 새로운 List를 만들어서 반환하면 안된다.
---

## 73. Set Matrix Zeroes

**[문제 링크](https://leetcode.com/problems/set-matrix-zeroes/)** · `Medium` · Python · `힌트봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

- 출력: 반환값 없음. matrix를 in-place로 수정
- 값 범위가 int 전체라 `-1` 같은 특정 값을 "0으로 바꿀 칸" 표시로 쓸 수 없다

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 0을 만나는 즉시 그 행/열을 0으로 바꾼다
2. 한계: 새로 만든 0을 원래 0으로 착각해 계속 번진다. 원본을 복사해 두면 피할 수 있지만 공간 `O(mn)`
3. 최종: 0의 위치를 먼저 다 기록하고, 0으로 채우는 건 그다음 단계에서 한다

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- Set이라 한 행/열에 0이 여러 개여도 중복 없이 한 번만 저장되고, 조회도 `O(1)`이다 (길이 m, n짜리 bool 배열로 대체 가능)

**복잡도**
- 시간: `O(mn)` 
    - 0의 위치를 찾기 위해 모든 원소를 한 번씩 탐색한다
    - 채우기 단계는 `|rows|·n + m·|cols| ≤ 2mn` 이라 전체도 `O(mn)`
- 공간: `O(m+n)`
    - 0의 위치를 담는 집합 2개.
    - 행을 담는 집합은 최대 크기가 m
    - 열을 담는 집합은 최대 크기가 n

**엣지 케이스** (최소 2개, 처리 방법까지)
- [x] 0이 하나도 없는 행렬 → Set이 비어 있어 채우기 루프가 돌지 않고, 행렬은 그대로
- [x] 한 행/열에 0이 여러 개 → Set이 중복을 걸러서 같은 행/열을 두 번 채우지 않음
- [x] 전부 0이거나 1×1 행렬 → 별도 분기 없이 같은 로직으로 처리됨

**코드**

```python

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seen_row = set()
        seen_col = set()

        # 0이 등장한 좌표를 기록한다 시간 복잡도 O(mn)
        for row_idx, row in enumerate(matrix):
            for col_idx, col_val in enumerate(row):
                if col_val == 0:
                    seen_row.add(row_idx)
                    seen_col.add(col_idx)
        
        # set 기반으로 0으로 채우기 - 행
        for row in seen_row:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        # set 기반으로 0으로 채우기 - 열
        for row in range(len(matrix)):
            for col in seen_col:
                matrix[row][col] = 0

```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 -->
> in-place로 값이 번지는 문제면 기록 단계와 수정 단계를 분리한다. 그래야 내가 새로 쓴 0이 원래 0(마커)을 덮어쓰지 않는다

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>
