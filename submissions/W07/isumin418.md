<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W07 — 이수민

| | |
|---|---|
| **주차 주제** | graph |
| **선언한 목표** | 1문제 |
| **실제로 푼 수** | 1문제 |
| **패턴 태그** | `#그래프` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 1. course schedule (207)

**[문제 링크](https://leetcode.com/problems/course-schedule/)** · `Medium` · Python · `해설봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- 입력: 과목 수 numCourses(1~2,000), 중복 없는 선수과목 쌍 prerequisites(0~5,000개). [a,b]는 b를 먼저 들어야 a를 수강할 수 있다는 뜻이며, 과목 번호는 0~`numCourses-1`이다.
- 출력 : 모든 과목을 이수할 수 있으면 true, 없으면 false.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 모든 과목의 수강 순서를 나열하고, 선수과목 조건을 만족하는 순서가 있는지 확인한다.
2. 한계: 가능한 순서가 numCourses!개이므로 과목 수가 많으면 탐색이 불가능하다.
3. 최종: 선수과목 관계를 방향 그래프로 만들고, DFS에서 미방문·탐색 중·탐색 완료 상태를 구분하여 사이클이 있으면 false, 없으면 true를 반환한다.

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 모든 수강 순서를 나열하는 브루트포스 대신, DFS로 선수과목 관계를 따라가며 사이클을 확인한다. 단순 방문 여부만 확인하면 탐색이 끝난 정점을 다시 만난 경우도 사이클로 오인할 수 있으므로, 미방문·탐색 중·탐색 완료의 세 상태를 구분한다.

**복잡도**
- 시간: `O(V + E)` — 각 과목과 선수과목 관계를 한 번씩 탐색한다. 
- 공간: `O(V + E)` — 인접 리스트에 O(V + E), 상태 배열과 재귀 호출 스택에 각각 O(V)가 필요하다. 

**엣지 케이스** (최소 2개, 처리 방법까지)
- [ ] 탐색 완료 정점을 다시 만나는 경우: 사이클로 판단하지 않고 true를 반환해 중복 탐색을 생략한다.
- [ ] 자기 자신이 선수과목인 경우([0,0]): 탐색 중인 자신을 다시 만나므로 사이클로 판단해 false를 반환한다.

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
from typing import List
import sys

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sys.setrecursionlimit(max(sys.getrecursionlimit(), numCourses + 100))

        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)  # b를 먼저 들어야 a를 수강할 수 있음

        # 0: 미방문, 1: 탐색 중, 2: 탐색 완료
        state = [0] * numCourses

        def dfs(v):
            if state[v] == 1:
                return False  # 현재 경로에 있는 정점을 다시 만나면 사이클

            if state[v] == 2:
                return True  # 이미 안전하다고 확인한 정점

            state[v] = 1

            for w in graph[v]:
                if not dfs(w):
                    return False

            state[v] = 2
            return True

        for v in range(numCourses):
            if state[v] == 0:
                if not dfs(v):
                    return False

        return True
```

**다시 볼 때의 트리거**
> 선수과목·선후관계·전체 이수 가능 여부 → 방향 그래프 + DFS 3가지 상태로 사이클 탐지

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

