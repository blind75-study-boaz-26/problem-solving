<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W04 — 이수민

| | |
|---|---|
| **주차 주제** | linked list, binary |
| **선언한 목표** | 2문제 |
| **실제로 푼 수** | 2문제 |
| **패턴 태그** | `#해시맵` `#투포인터` `#카데인` |

**한 줄 회고:**
<!-- 이번 주에 새로 알게 된 것 한 가지 -->

---

## 1. Reverse Linked List(206)

**[문제 링크](https://leetcode.com/problems/reverse-linked-list/)** · `Easy` · Python · `자력해결`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
<!-- 입력 제약(길이·값 범위·중복·음수 여부)과 출력 형태. 1~2줄 -->
- 입력 : 단일 연결 리스트의 첫 노드 head. 노드 수는 0~5,000개이며, 값은 −5,000~5,000으로 음수와 중복이 가능함.
- 출력 : 연결 방향을 뒤집은 리스트의 첫 노드. 빈 리스트이면 None을 반환함. 예: [1,2,3,4,5] → [5,4,3,2,1], [] → []

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 빈 배열을 만들어서 리스트의 모든 값을 저장하고 배열의 마지막 인덱스부터 읽음. 해당 값으로 연결 리스트를 만들어 반환함. 
2. 한계: 배열과 새 노드를 생성하므로 O(n)의 추가 공간이 필요
3. 최종: 기존 노드의 연결 방향을 반대로 변경함. 노드 수와 관계없이 일정한 개수의 변수만 사용함. 
**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- 기존 연결 리스트의 next를 직접 변경하는 반복문 방식을 선택함. 배열이나 새 노드 없이 일정한 개수의 변수만 사용하므로 추가 공간을 O(1)로 줄일 수 있음.

**복잡도**
- 시간: `O(n)` — 노드 n개를 한 번씩 방문
- 공간: `O(1)` — 노드 수와 관계없이 일정한 개수의 변수 사용

**엣지 케이스** (최소 2개, 처리 방법까지)
- 빈 리스트 (head = None): 반복문이 실행되지 않고 prev의 초기값인 None을 반환함.
- 노드가 1개인 리스트 (head = [1]): 반복문이 한 번 실행되어 노드의 next가 None으로 유지되고, 해당 노드를 그대로 반환함.

**코드**

```python
# LeetCode에서 Accepted 받은 코드를 그대로. 다듬지 않기.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current is not None:
            next_node = current.next  # 원래 다음 노드를 기억
            current.next = prev   # 연결 방향을 이전 노드 쪽으로 변경   
            prev = current  # 이전 노드를 현재 노드로  갱신       
            current = next_node  # 원래 다음 노드로 이동    

        return prev  
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 -->

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [ ]

</details>

---

## 2. Remove Nth Node From End of List

**[https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/]()** · `Medium` · python · `힌트`

**입출력**
- 입력 : head: 연결 리스트의 첫 노드 / n : 뒤에서 몇 번째 노드를 삭제할지 나타내는 정수. 맨 뒤 노드가 1번째임.
- 출력 : 남은 리스트의 첫 노드(head)

**접근**
1. 브루트포스: 전체를 순회해 길이를 구한 뒤, 다시 앞에서 (길이)-(n-1) 번째 노드를 찾아 삭제 (뒤에서 n번째 노드 뒤에는 n-1개의 노드가 있음)
2. 한계: 시간 O(길이), 공간 O(1)이지만, 두 번 순회하므로 한 번 순회라는 문제 조건을 만족하지 못함
3. 최종: 두 포인터를 n칸 간격으로 이동시켜 삭제할 노드를 찾는 투 포인터 방식 사용

**선택 근거**
- 연결 리스트는 노드의 `next`를 변경하여 삭제할 수 있으므로 별도 자료구조 없이 처리함. 투 포인터의 간격을 n칸으로 유지하면 전체 길이를 미리 구하지 않고 한 번의 순회로 삭제할 노드의 직전 노드를 찾을 수 있음.

**복잡도**
- 시간: O(L) — 리스트 길이 L에 비례하여 두 포인터를 이동함.
fast 이동 횟수 : 먼저 n칸 + 마지막 노드까지 L-n 칸 = L 번
- 공간: O(1) — 더미 노드와 두 포인터만 추가로 사용함.

**엣지 케이스**
- [ ] 노드가 하나인 경우: head = [1], n = 1 → 유일한 노드를 삭제하고 None을 반환함.
- [ ] 첫 노드를 삭제하는 경우: head = [1,2,3], n = 3 → 더미 노드의 next를 두 번째 노드로 연결하여 [2,3]을 반환함. 더미 노드를 두어 첫 노드를 삭제할 때도 다른 노드를 삭제할 때와 같은 코드로 처리. dummy(0) → 1 → 2 → 3 → 4 → 5 → None

**코드**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # fast를 n칸 먼저 이동
        for _ in range(n):
            fast = fast.next

        # fast가 마지막 노드에 도착할 때까지 함께 이동
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # slow 바로 다음 노드를 삭제
        slow.next = slow.next.next

        return dummy.next
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