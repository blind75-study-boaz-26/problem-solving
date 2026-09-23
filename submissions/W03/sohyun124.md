<!--
  이 파일을 그대로 복사해서 submissions/W0X/<github-아이디>.md 로 저장하세요.
  작성 기준과 각 항목을 왜 쓰는지는 ../docs/submission-guide.md 를 보세요.
  원칙: 한 문제당 10분 이내. 대부분의 항목은 한두 줄입니다.
-->

# W03 — 소현

| | |
|---|---|
| **주차 주제** | Array |
| **선언한 목표** | 3문제 |
| **실제로 푼 수** | 3문제 |
| **패턴 태그** | `#나머지연산` `#Set` `#해시맵` |

**한 줄 회고:**
배열을 순회하면서 문제에 필요한 정보가 존재 여부인지, 등장 횟수인지에 따라 적절한 자료구조를 선택하는 방법을 익혔다.

---

## 1. Minimum Operations to Make Array Sum Divisible by K

**[문제 링크](https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/)** · `Easy` · JavaScript · `해설봄`

**입출력**

- `1 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`, `1 <= k <= 100`이며, 배열의 합이 k로 나누어떨어지도록 만드는 최소 연산 횟수를 반환한다.

**접근**

1. 브루트포스: 배열의 합을 구하고 1씩 감소시키면서 k로 나누어떨어지는지 확인한다.

2. 한계: 나누어떨어질 때까지 합을 직접 1씩 감소시키며 반복해서 확인할 필요가 있다.

3. 최종: 전체 합을 k로 나눈 나머지만큼 감소시키면 가장 가까운 k의 배수가 되므로 `sum % k`를 반환한다.

**선택 근거**

- 한 번의 연산마다 전체 합이 1씩 감소하므로, 전체 합을 k로 나눈 나머지가 필요한 최소 연산 횟수가 된다.

**복잡도**

- 시간: `O(n)` — 배열의 전체 합을 구하기 위해 n개의 원소를 한 번씩 확인한다.

- 공간: `O(1)` — 별도의 자료구조 없이 합을 저장하는 변수만 사용한다.

**엣지 케이스**

- [x] 합이 이미 k로 나누어떨어지는 경우 → 나머지가 0이므로 0을 반환한다.

- [x] 배열의 합이 k보다 작은 경우 → 합을 0까지 감소시키면 되므로 나머지인 합 자체가 정답이 된다.

**코드**

```javascript
var minOperations = function(nums, k) {
    const total = nums.reduce((sum, num) => sum + num, 0);
    return total % k;
};
```

**다시 볼 때의 트리거**

> 합을 k로 나누어떨어지게 만들기 위해 1씩 감소시킨다 → 전체 합을 k로 나눈 나머지만큼 감소시키면 된다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 나머지가 왜 최소 연산 횟수가 되는지 이해하는 부분

- **복습 필요:** [x]

</details>

---

## 2. Jewels and Stones

**[문제 링크](https://leetcode.com/problems/jewels-and-stones/)** · `Easy` · JavaScript · `해설봄`

**입출력**

- `1 <= jewels.length, stones.length <= 50`이며 영문 대소문자를 구분한다. stones의 문자 중 jewels에 포함되는 문자의 개수를 반환한다.

**접근**

1. 브루트포스: stones의 각 문자마다 jewels를 순회하면서 보석인지 확인한다.

2. 한계: 돌 하나를 확인할 때마다 jewels를 다시 탐색해야 한다.

3. 최종: jewels를 Set에 저장하고 stones를 한 번 순회하면서 현재 문자가 Set에 존재하는지 확인한다.

**선택 근거**

- 각 돌이 보석인지에 대한 존재 여부만 필요하므로 특정 값의 존재 여부를 빠르게 확인할 수 있는 Set을 사용한다.

**복잡도**

- 시간: `O(j + s)` — jewels를 Set으로 만드는 데 O(j), stones를 순회하는 데 O(s)가 필요하다.

- 공간: `O(j)` — jewels의 문자들을 Set에 저장한다.

**엣지 케이스**

- [x] 보석에 해당하는 돌이 하나도 없는 경우 → count가 증가하지 않으므로 0을 반환한다.

- [x] `"a"`와 `"A"`가 존재하는 경우 → 대소문자를 서로 다른 문자로 처리한다.

**코드**

```javascript
var numJewelsInStones = function(jewels, stones) {
    const jewelSet = new Set(jewels);
    let count = 0;

    for (const stone of stones) {
        if (jewelSet.has(stone)) {
            count++;
        }
    }

    return count;
};
```

**다시 볼 때의 트리거**

> 각 값이 특정 목록에 포함되어 있는지만 확인하면 된다 → Set으로 존재 여부를 확인한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** Set을 사용하는 이유와 `has()`를 이용한 존재 여부 확인

- **복습 필요:** [x]

</details>

---

## 3. Number of Good Pairs

**[문제 링크](https://leetcode.com/problems/number-of-good-pairs/)** · `Easy` · JavaScript · `해설봄`

**입출력**

- `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`이며, `nums[i] == nums[j]`이고 `i < j`인 좋은 쌍의 개수를 반환한다.

**접근**

1. 브루트포스: 모든 두 원소를 비교하면서 값이 같은 경우 좋은 쌍의 개수를 증가시킨다.

2. 한계: 각 원소마다 다른 원소들을 다시 비교하기 때문에 시간복잡도가 O(n²)이 된다.

3. 최종: 현재 숫자와 같은 숫자가 이전에 등장한 횟수만큼 새로운 쌍이 생기므로 Hash Map에 숫자별 등장 횟수를 저장한다.

**선택 근거**

- 현재 숫자가 이전에 몇 번 등장했는지 알아야 하므로 `숫자 → 등장 횟수`를 저장할 수 있는 Hash Map을 사용한다.

**복잡도**

- 시간: `O(n)` — 배열의 각 숫자를 한 번씩 확인한다.

- 공간: `O(n)` — 최악의 경우 Hash Map에 최대 n개의 서로 다른 숫자를 저장한다.

**엣지 케이스**

- [x] 모든 숫자가 서로 다른 경우 → 이전 등장 횟수가 모두 0이므로 결과는 0이다.

- [x] 모든 숫자가 같은 경우 → 이전 등장 횟수만큼 새로운 좋은 쌍을 추가한다.

**코드**

```javascript
var numIdenticalPairs = function(nums) {
    const freq = {};
    let count = 0;

    for (const num of nums) {
        count += freq[num] || 0;
        freq[num] = (freq[num] || 0) + 1;
    }

    return count;
};
```

**다시 볼 때의 트리거**

> 같은 값끼리 쌍을 만들어야 한다 → 현재 값의 이전 등장 횟수만큼 새로운 쌍이 생긴다 → Hash Map으로 등장 횟수를 저장한다.

<details><summary>선택 항목</summary>

- **소요 시간 / 막힌 지점:** 이전 등장 횟수만큼 새로운 쌍이 생긴다는 아이디어

- **복습 필요:** [x]

</details>

---