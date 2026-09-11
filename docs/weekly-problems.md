# 주차별 문제 리스트

Blind 75, 10주 완주용 주차별 분배표입니다. 문제 제목을 누르면 LeetCode로 이동합니다.

- **최소 3문제**, 상한 없음. 주차 시작 시 몇 문제를 풀지 선언합니다. → [스터디 규칙](../README.md#rules)
- 제출 방법과 문서에 담을 내용은 [과제 제출 가이드](submission-guide.md)를 보세요.
- `(P)` 는 LeetCode Premium 전용 문제입니다. 구독이 없으면 같은 주차의 다른 문제로 대체하세요.
- 난이도는 LeetCode 표기 기준이며, 사이트에서 변경될 수 있습니다.

> 각 주차의 **"이 주차에서 익힐 패턴"** 은 접어두었습니다. 먼저 문제를 직접 분류해 보고,
> 30분 이상 방향이 안 잡힐 때 펼쳐 보세요. 패턴을 스스로 찾아내는 것이 이 스터디의 핵심입니다.

---

<a id="w1"></a>

## W1 — OT (9/9)

문제 없음. 스터디 운영 방식, 제출 규칙, 벌금·발표 규칙을 확정합니다.
이 주에 [과제 제출 가이드](submission-guide.md)와 [제출 템플릿](../templates/weekly-submission.md)을 한 번 읽어두세요.

---

<a id="w2"></a>

## W2 — Array (9/16) · 10문제

- [ ] [Two Sum](https://leetcode.com/problems/two-sum/) `Easy`
- [ ] [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) `Easy`
- [ ] [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) `Easy`
- [ ] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) `Medium`
- [ ] [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) `Medium`
- [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) `Medium`
- [ ] [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) `Medium`
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) `Medium`
- [ ] [3Sum](https://leetcode.com/problems/3sum/) `Medium`
- [ ] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) `Medium`

<details><summary>이 주차에서 익힐 패턴</summary>

- 해시맵으로 "찾아야 할 값"을 O(1)에 조회하기 (보수 탐색)
- 정렬해서 얻는 것과 잃는 것 (인덱스 소실 vs 투 포인터 가능)
- 투 포인터: 양끝에서 좁히기 / 한 방향 이동
- 누적 상태를 한 번의 순회로 들고 가기 (카데인, 접두·접미 곱)
- 정렬 배열이 회전되어도 "한쪽은 항상 정렬" 이라는 성질로 이진 탐색

</details>

---

<a id="w3"></a>

## W3 — String (9/23) · 10문제

- [ ] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) `Medium`
- [ ] [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) `Medium`
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) `Hard`
- [ ] [Valid Anagram](https://leetcode.com/problems/valid-anagram/) `Easy`
- [ ] [Group Anagrams](https://leetcode.com/problems/group-anagrams/) `Medium`
- [ ] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) `Easy`
- [ ] [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) `Easy`
- [ ] [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) `Medium`
- [ ] [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) `Medium`
- [ ] [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) `Medium` `(P)`

<details><summary>이 주차에서 익힐 패턴</summary>

- 슬라이딩 윈도우: 윈도우를 언제 늘리고 언제 줄이는지 조건을 말로 먼저 정의
- 빈도 배열(26칸) vs 해시맵: 문자 집합이 정해져 있을 때의 선택
- 정렬된 문자열·문자 카운트를 해시 키로 쓰기 (그룹핑)
- 스택으로 짝 맞추기
- 팰린드롬: 중심 확장(홀/짝 두 경우)
- 직렬화에서 구분자가 데이터에 나타날 수 있는 문제 → 길이 접두어

</details>

---

<a id="w4"></a>

## W4 — Linked List + Binary (9/30) · 10문제

**Linked List (5)**

- [ ] [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) `Easy`
- [ ] [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) `Easy`
- [ ] [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) `Easy`
- [ ] [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) `Medium`
- [ ] [Reorder List](https://leetcode.com/problems/reorder-list/) `Medium`

**Binary (5)**

- [ ] [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) `Medium`
- [ ] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) `Easy`
- [ ] [Counting Bits](https://leetcode.com/problems/counting-bits/) `Easy`
- [ ] [Missing Number](https://leetcode.com/problems/missing-number/) `Easy`
- [ ] [Reverse Bits](https://leetcode.com/problems/reverse-bits/) `Easy`

<details><summary>이 주차에서 익힐 패턴</summary>

- 더미(dummy) 헤드로 "머리 노드가 바뀌는 경우"를 분기 없이 처리
- 세 포인터(prev/cur/next)로 제자리 뒤집기
- 느린/빠른 포인터: 순환 탐지, 중간 지점 찾기
- 두 포인터의 간격을 n으로 고정해 한 번의 순회로 끝내기
- XOR의 성질 (a^a=0, 항등원 0), 시프트와 마스킹
- 비트 개수 세기에서 이전 결과 재사용 → DP와의 연결

</details>

---

<a id="w5"></a>

## W5 — Tree 기초 (10/7) · 7문제

- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) `Easy`
- [ ] [Same Tree](https://leetcode.com/problems/same-tree/) `Easy`
- [ ] [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) `Easy`
- [ ] [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) `Easy`
- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) `Medium`
- [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) `Medium`
- [ ] [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) `Medium`

> 10/14, 10/21은 휴회입니다. W5와 W6 사이에 3주가 있으니, 밀린 문제를 따라잡기 좋은 구간입니다.

<details><summary>이 주차에서 익힐 패턴</summary>

- 재귀 3단계: 종료 조건 → 자식에게 맡길 일 → 자식 결과로 내 답 만들기
- 두 트리를 동시에 내려가며 비교하기
- BFS 레벨 순회에서 "레벨 경계"를 잡는 방법 (큐 크기 스냅샷)
- BST는 "왼쪽 < 나 < 오른쪽"이 부분트리 전체에 성립 → 값 비교가 아니라 범위(min, max) 전달
- BST 탐색은 방향을 알기 때문에 O(h)

</details>

---

<a id="w6"></a>

## W6 — Tree 심화 + Trie (10/28) · 7문제

- [ ] [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) `Medium`
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) `Hard`
- [ ] [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) `Medium`
- [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) `Hard`
- [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) `Medium`
- [ ] [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) `Medium`
- [ ] [Word Search II](https://leetcode.com/problems/word-search-ii/) `Hard`

<details><summary>이 주차에서 익힐 패턴</summary>

- BST의 중위 순회 = 오름차순. "k번째"는 순회 카운트로 해결
- 재귀 함수가 **반환하는 값**과 **갱신하는 전역 답**을 분리하기 (max path sum의 핵심)
- preorder는 루트를, inorder는 좌/우 분할점을 알려준다 → 인덱스 맵으로 O(n)
- 직렬화는 null까지 기록해야 트리 모양이 복원된다
- Trie 노드 설계(자식 맵 + 끝 표시)와 와일드카드에서의 분기 탐색
- Trie + 격자 백트래킹: 접두어가 없으면 즉시 가지치기

</details>

---

<a id="w7"></a>

## W7 — Graph (11/4) · 8문제

- [ ] [Clone Graph](https://leetcode.com/problems/clone-graph/) `Medium`
- [ ] [Course Schedule](https://leetcode.com/problems/course-schedule/) `Medium`
- [ ] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) `Medium`
- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/) `Medium`
- [ ] [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) `Medium`
- [ ] [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) `Hard` `(P)`
- [ ] [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) `Medium` `(P)`
- [ ] [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) `Medium` `(P)`

<details><summary>이 주차에서 익힐 패턴</summary>

- 문제를 그래프로 번역하기: 무엇이 정점이고 무엇이 간선인가
- 격자(grid)는 암시적 그래프 — 4방향 이동이 간선
- 방문 처리를 언제 하는가 (큐에 넣을 때 vs 꺼낼 때)
- 복제 문제에서 원본→사본 매핑으로 무한 루프 끊기
- 위상 정렬(진입 차수 / DFS 색칠)과 사이클 판정
- 유니온 파인드로 연결 요소 세기, 트리 판정(간선 수 = n-1 이고 사이클 없음)
- 바깥에서 안으로 거꾸로 탐색하기 (Pacific Atlantic)

</details>

---

<a id="w8"></a>

## W8 — Matrix + Interval (11/11) · 9문제

**Matrix (4)**

- [ ] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) `Medium`
- [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) `Medium`
- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/) `Medium`
- [ ] [Word Search](https://leetcode.com/problems/word-search/) `Medium`

**Interval (5)**

- [ ] [Insert Interval](https://leetcode.com/problems/insert-interval/) `Medium`
- [ ] [Merge Intervals](https://leetcode.com/problems/merge-intervals/) `Medium`
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) `Medium`
- [ ] [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) `Easy` `(P)`
- [ ] [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) `Medium` `(P)`

<details><summary>이 주차에서 익힐 패턴</summary>

- 제자리(in-place) 변환: 첫 행/열을 표시용 공간으로 재활용
- 90도 회전 = 전치 + 행 뒤집기
- 경계 4개를 변수로 들고 좁히는 순회
- 백트래킹에서 방문 표시를 되돌리는 위치
- 구간 문제는 **무엇으로 정렬하느냐**가 절반: 시작점(병합) vs 끝점(그리디 최대 개수)
- 겹침 조건을 부등식으로 정확히 쓰기 (`a.start <= b.end`)
- 시작/종료 이벤트를 분리해 정렬하거나, 최소 힙으로 종료 시각 관리

</details>

---

<a id="w9"></a>

## W9 — DP 1차원 (11/18) · 6문제

- [ ] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) `Easy`
- [ ] [House Robber](https://leetcode.com/problems/house-robber/) `Medium`
- [ ] [House Robber II](https://leetcode.com/problems/house-robber-ii/) `Medium`
- [ ] [Jump Game](https://leetcode.com/problems/jump-game/) `Medium`
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/) `Medium`
- [ ] [Decode Ways](https://leetcode.com/problems/decode-ways/) `Medium`

<details><summary>이 주차에서 익힐 패턴</summary>

- `dp[i]`가 **무엇을 뜻하는지 한 문장으로** 쓰고 시작하기. 이게 안 되면 점화식도 안 나온다
- 기저 조건과 인덱스 경계(0, 1) 처리
- 점화식이 직전 두 값만 보면 배열을 두 변수로 압축 (O(1) 공간)
- 원형 조건은 "첫 번째를 쓰는 경우 / 안 쓰는 경우" 두 번의 선형 DP로 분해
- DP와 그리디의 갈림길 (Jump Game은 그리디로도 풀린다 — 왜 되는지 설명해 보기)
- 문자열 DP에서 1자리/2자리 전이와 '0' 예외

</details>

---

<a id="w10"></a>

## W10 — DP 심화 + Heap (11/25) · 8문제

**DP (5)**

- [ ] [Coin Change](https://leetcode.com/problems/coin-change/) `Medium`
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) `Medium`
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) `Medium`
- [ ] [Word Break](https://leetcode.com/problems/word-break/) `Medium`
- [ ] [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) `Medium`

**Heap (3)**

- [ ] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) `Medium`
- [ ] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) `Hard`
- [ ] [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) `Hard`

<details><summary>이 주차에서 익힐 패턴</summary>

- 무한 개수 배낭(coin change) 루프 순서: 조합이냐 순열이냐가 루프 순서로 결정된다
  (Coin Change vs Combination Sum IV를 나란히 놓고 비교해 보세요)
- 2차원 DP 테이블 채우기와 전이 방향 (LCS)
- LIS의 O(n²) DP와 O(n log n) 이진 탐색 풀이
- 문자열을 쪼개는 DP에서 상태를 "위치"로 잡기
- 힙은 "전체 정렬은 필요 없고 극값만 필요할 때" → O(n log k)
- 두 개의 힙(최대 힙 + 최소 힙)으로 중앙값을 O(log n)에 유지하기

</details>

---

## 진행 현황

총 **75문제** / 10주 (W1은 OT). 주차별 문제 수: 10, 10, 10, 7, 7, 8, 9, 6, 8.

## 관련 문서

- [스터디 개요와 규칙](../README.md)
- [과제 제출 가이드](submission-guide.md)
- [주간 제출 템플릿](../templates/weekly-submission.md)
