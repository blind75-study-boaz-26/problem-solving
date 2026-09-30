<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W04 — 최우성

| | |
|---|---|
| **주차 주제** | Linked List + Binary |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `Linked List`, `Two Pointers`, `Bit Manipulation` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->
> 파이썬은 int를 표현할 때 비트 폭에 제한을 두지 않는다. 부호 값과 절댓값을 따로 저장한다. 때문에 MSB를 부호로 표현하는 규칙이 없다. 비트 연산을 할 때 음수인 경우 추가적인 처리가 필요하다.

---

## 19. Remove Nth Node From End of List

**[문제 링크](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)** · `Medium` · Python · `자력해결`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 리스트 원소 수가 30개 이하로 브루트 포스가 충분히 가능하다. 먼저 순회를 통해 원소를 list(python 자료형)에 담아서 배열처럼 사용할 수 있음.
2. 보완할 점: 모든 원소를 list에 복사하는 것은 비효율적이다. 투포인터를 쓰면 모든 원소를 복사하지 않아도 된다.
3. 최종: 투포인터 활용

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- list를 도입할 수 있지만 메모리를 아끼기 위해 투포인터를 활용한다.

**복잡도**
- 시간: `O(N)`
- 공간: `O(1)`

**엣지 케이스** (최소 2개, 처리 방법까지)
- Input: head = [1], n = 1, Output: []
  - 원소가 하나고, 그 원소를 지워야하는 경우이다. None을 반환한다.
- Input: head = [1,2,3], n = 3, Output: [2,3]
  - 지워야할 원소가 첫 원소인 경우이다. head만 다음 원소로 옮겨준다.

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # edge case 1: 원소가 하나인 케이스
        if head.next is None and n == 1:
            return None

        l = r = head
        for i in range(n):
            r = r.next
        
        # edge case 2: 지워야할 원소가 첫 원소
        if r is None:
            head = head.next
            return head

        while r.next is not None:
            l = l.next
            r = r.next

        # l이 지워야하는 원소 앞에 위치함.
        l.next = l.next.next

        return head

```

**다시 볼 때의 트리거**
> Linked List 순회 시 이미 지나친 원소를 다시 조회해야할 경우 투포인터를 도입할 수 있다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 268. Missing Number

**[문제 링크](https://leetcode.com/problems/missing-number/)** · `Easy` · python · `힌트봄`

> Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

**입출력**
- n == nums.length
- 1 <= n <= 104
- 0 <= nums[i] <= n
- All the numbers of nums are unique.

**접근**

- **비효율적인 풀이**: 0~n을 for문으로 돌면서 array 안에 그 값이 있는지 확인하는 방법. in 연산에 O(N)의 시간이 걸린다. 따라서 최종 시간 복잡도는 O(N^2)이다.

- **개선된 풀이**: `(0~n까지의 합) - (배열의 모든 원소를 합한 값) = 빼먹은 값`의 아이디어 사용

- **xor을 활용한 풀이**: (0~n까지의 합)에 대해 array의 모든 원소를 xor하면 빼먹은 원소가 나온다.

**선택 근거**
- 빼기 연산보다 xor 연산이 더 효율적이므로 xor을 활용한다.

**복잡도**
- 시간: `O(N)`: array의 모든 원소를 한 번 순회한다.
- 공간: `O(1)`

**엣지 케이스**
- [ ]
- [ ]

**코드**

```python
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            n ^= i ^ num
        
        return n

```

**다시 볼 때의 트리거**
> - a ^ a = 0
> - (a ^ b ^ c) ^ b ^ c = a

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 190. Reverse Bits

**[문제 링크](https://leetcode.com/problems/reverse-bits/)** · `Easy` · python · `힌트봄`

> Reverse bits of a given 32 bits signed integer.

**입출력**

Example 1:

- Input: n = 43261596
- Output: 964176192

Example 2:

- Input: n = 2147483644
- Output: 1073741822

Constraints:

- 0 <= n <= 2^31 - 2
- n is even.
  - 비트의 순서를 역순으로 뒤집어도 MSB가 0이라 양수다. 음수인 경우는 고려하지 않아도 된다.

**접근**
1. n에서 비트 마스킹을 통해 마지막 비트를 뽑는다.
2. 그 비트를 result에 넣는다
3. n = n >> 1
4. result = result << 1
5. 위의 과정을 반복한다.

**복잡도**
- 시간: `O(1)`: 32비트 고정이기 때문에 O(1)이다.
- 공간: `O(1)`

**엣지 케이스**
- [ ]
- [ ]

**코드**

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
        return res

```

**다시 볼 때의 트리거**
> 원하는 비트를 추출하고 싶을 때는 &를 통해 마스킹 연산을 하면 된다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

<!-- 문제 수만큼 위 블록을 복사해서 이어 쓰세요. -->

## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. -->
