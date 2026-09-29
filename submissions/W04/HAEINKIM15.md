<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W04 — 김해인

| | |
|---|---|
| **주차 주제** | Linked List |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** |`#LinkedList` `#TwoPointer` `#FastSlowPointer` `#Reverse`|

**한 줄 회고:**
연결리스트에서는 값 자체보다 next가 어떤 노드를 가리키는지 생각..
연결을 바꾸기 전에 기존 next를 임시 변수에 저장해야 노드를 잃어버리지 않는다는 점을 기억할 것.

---

## 206. Reverse Linked List

**[문제 링크](https://leetcode.com/problems/reverse-linked-list/description/)** · `Easy` · Python · `해설봄`
<!-- 결과 태그: 자력해결 / 힌트봄 / 해설봄 — 솔직하게. 복습 리스트의 근거가 됩니다. -->

**입출력**
- 입력: 단일 연결 리스트의 시작 노드 head (노드 개수 0 ~ 5000)
- 출력: 각 노드의 연결 방향을 반대로 뒤집은 연결 리스트의 새로운 head를 반환한다.

**접근**
<!-- 브루트포스 → 왜 부족한가 → 최종 아이디어 한 문장. 3줄 이내 -->
1. 브루트포스: 노드의 값을 배열에 저장하고 역순으로 새로운 연결 리스트를 만든다. 
2. 한계: 별도의 배열과 새로운 노드가 필요해 추가 공간을 사용하며, 기존 노드의 연결을 직접 뒤집을 필요가 없다.
3. 최종: `prev_node`, `current_node`, `next_node`를 사용해 각 노드의 `next` 방향을 하나씩 반대로 변경한다.

**선택 근거**
<!-- 왜 이 자료구조/알고리즘인가. 1~2줄 -->
- `단일 연결 리스트`는 각 노드가 `next`로 다음 노드를 가리키므로`next`의 방향만 변경하면 리스트를 뒤집을 수 있다.
- `current_node.next`를 변경하기 전에 원래 다음 노드를 `next_node`에 저장하여 연결이 끊겨도 다음 노드로 이동할 수 있도록 한다.

**복잡도**
- 시간:` O(n)` — 모든 노드를 처음부터 끝까지 한 번씩 방문한다.
- 공간: `O(1)` — `prev_node`,`current_node`, `next_node` 등 일정한 개수의 포인터만 사용한다.

**엣지 케이스** (최소 2개, 처리 방법까지)
- [`빈 리스트`] `current_node`가 처음부터 `None`이므로 반복문을 실행하지 않고 `None` 반환
- [`1`] 노드가 하나인 경우 → `1.next`를 `None`으로 설정하고 그대로 `1`을 새로운 `head`로 반환
- [`1,2`] 노드가 두 개인 경우 → 1 → 2의 방향을 2 → 1로 변경

**코드**

```python
class Solution(object):
    def reverseList(self, head):
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
```

**다시 볼 때의 트리거**
> <!-- "두 달 뒤 이 문제를 만나면 무엇을 떠올려야 하는가" 한 문장 --> Linked List의 연결 방향을 반대로 바꿔야 한다면 next 저장 → 방향 뒤집기 → prev 이동 → current 이동 순서를 떠올린다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** next..??current..?? 
- **복습 필요:** [O]

</details>

---

## 21. Merge Two Sorted Lists

**[문제 링크](https://leetcode.com/problems/merge-two-sorted-lists/description/)** · `Easy` · python · `힌트봄`

**입출력**
- 입력: 입력: 오름차순으로 정렬된 두 연결 리스트` list1`, `list2` (각 리스트의 노드 개수 0 ~ 50)
- 출력: 두 리스트의 기존 노드들을 하나의 오름차순 연결 리스트로 병합하여 새로운 head를 반환한다.
접근

**접근**
1. 브루트포스: 두 리스트의 값을 배열에 저장한 뒤 정렬하고 새로운 연결 리스트를 만들 수 있다.
2. 한계: 이미 두 리스트가 정렬되어 있는데 다시 전체를 정렬할 필요가 없고 추가 배열과 노드가 필요하다.
3. 최종: 두 리스트의 현재 노드 값을 비교해 더 작은 노드를 current.next에 연결하고, 선택한 리스트의 포인터를 한 칸 이동한다.

**선택 근거**
- 두 리스트가 이미 정렬되어 있으므로 각 리스트의 `맨 앞 노드`만 비교하면서 작은 노드를 순서대로 연결할 수 있다.
- `dummy `노드를 사용하면 첫 번째 노드를 별도로 처리할 필요가 없고, 마지막에` dummy.next`로 결과 리스트의 head를 쉽게 반환할 수 있다.

**복잡도**
- 시간: `O(n + m)` — `list1의 n개 노드`와 `list2의 m개 노드`를 각각 최대 한 번씩 처리한다.
- 공간: `O(1)` — 기존 노드들을 다시 연결하며 `dummy`, `current `등 일정한 개수의 포인터만 추가로 사용한다.

**엣지 케이스**
- list1 = [], list2 = [] → 두 리스트가 모두 비어 있으므로` dummy.next`, 즉 `None `반환
- list1 = [], list2 = [0] → 비교 없이 남아 있는 list2를` current.next에 그대로 연결`
- list1 = [1,2], list2 = [3,4] → list1이 먼저 끝나면 남은 list2를 결과 뒤에 그대로 연결

**코드**

```python
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return dummy.next
```

**다시 볼 때의 트리거**
> 정렬된 두 Linked List를 하나로 합쳐야 한다면 두 현재 노드를 비교하면서 Dummy Node + Current Pointer로 작은 노드부터 연결한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:**
- **복습 필요:** [O]

</details>

---


## 143. Reorder List

**[문제 링크](https://leetcode.com/problems/reorder-list/)** · `Medium` · python · `해설봄`

**입출력**
- 입력: 단일 연결 리스트의 시작 노드 head (`노드 개수 1 ~ 5 * 10^4`)
- 출력: 별도의 값을 반환하지 않고 기존 리스트를 `L0 → Ln → L1 → Ln-1 → ... `순서가 되도록 직접 변경한다.

**접근**
1. 브루트포스: 모든 노드를 배열에 저장한 뒤 앞과 뒤에서 번갈아 꺼내 연결할 수 있다.
2. 한계: 배열을 추가로 사용하기 때문에 O(n)의 추가 공간이 필요하다.
3. 최종: `Slow/Fast Pointer`로 `중간`을 찾고 → 뒤쪽 절반을 `Reverse` → 앞쪽과 뒤쪽을 번갈아 `Merge`한다.


**선택 근거**
- 단일 연결 리스트에서는 마지막 노드에 바로 접근할 수 없으므로 `slow`, `fast` 포인터로 중간을 찾은 뒤 뒤쪽 절반을 뒤집어 앞에서부터 접근할 수 있도록 한다.
- 이후 `first`, `second`의 다음 노드를 임시 저장하면서 두 리스트의 노드를 번갈아 연결하면 추가 배열 없이 재배열할 수 있다.


**복잡도**
- 시간:` O(n)` — 중간 찾기 `O(n)`, 뒤쪽 리스트 뒤집기 `O(n)`, 두 리스트 병합 `O(n)`이므로 전체는 `O(n)`이다.
- 공간: `O(1)` — `slow, fast, prev, current, first, second `등 일정한 개수의 포인터만 사용한다.


**엣지 케이스**
- [1] 노드가 하나인 경우 → 뒤쪽 리스트가 없으므로 병합할 노드 없이 기존 리스트 유지
- [1,2] 노드가 두 개인 경우 → 이미 L0 → L1 형태이므로 결과는 [1,2]
- [1,2,3,4,5] 홀수 개의 노드 → 중간 노드 3은 앞쪽 리스트의 마지막에 남아 [1,5,2,4,3]으로 재배열

**코드**

```python
class Solution(object):
    def reorderList(self, head):
    
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

    
        prev = None
        current = second

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node


        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
```

**다시 볼 때의 트리거**
> Linked List를 앞 → 뒤 → 앞 → 뒤 순서로 재배열해야 한다면 중간 찾기 → 뒤 절반 Reverse → 두 리스트 Merge의 3단계를 떠올린다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 처음에는 중간 노드를 길이 // 2로 찾으려 했고 Slow/Fast Pointer를 힌트로 확인했다.
- **복습 필요:** [O]

</details>

---


## 이번 주 패턴 정리 (선택)

<!-- 이번 주 문제들을 관통하는 패턴이 있었다면 한 단락. 세션 발표 때 바로 쓸 수 있습니다. --> 
이번 세 문제에서는 Linked List의 노드 값이 아니라 next 연결 관계를 직접 조작하는 방법을 연습했다.
- Reverse Linked List: 연결 방향 뒤집기 → prev + current + next
- Merge Two Sorted Lists: 정렬된 두 리스트 병합 → Dummy Node + Current Pointer
- Reorder List: 중간을 기준으로 분리하고 재배열 → Slow/Fast Pointer + Reverse + Merge

문자열 문제를 만났을 때 바로 구현하기보다, 먼저 **중복을 관리해야 하는지 / 빈도를 세어야 하는지 / 양쪽을 비교해야 하는지**를 확인하고 그에 맞는 자료구조와 알고리즘을 선택하는 것이 중요!!
