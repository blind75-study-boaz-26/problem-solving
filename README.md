# Blind 75 코딩테스트 스터디

10주 동안 [Blind 75](https://www.teamblind.com/post/new-year-gift-curated-list-of-top-75-leetcode-questions-to-save-your-time-oam1oreu) 문제 75개를 풀고, 매주 수요일에 화이트보드 세션으로 검증합니다.

| | |
|---|---|
| **기간** | 2026-09-09 ~ 2026-11-25 (10회차) |
| **시간** | 매주 수요일 20:00 ~ 21:00 |
| **장소** | Hspace |
| **구성원** | 7명 — @wsxchoi(팀장), @github-id-2, @github-id-3, @github-id-4, @github-id-5, @github-id-6, @github-id-7 |

<!-- 구성원: 각자 본인 GitHub 아이디로 자리표시자를 교체해 주세요. 공개 저장소라 실명은 넣지 않습니다. -->

---

## 목차

- [주차별 문제 리스트](docs/weekly-problems.md) — 10주 분배표, 문제별 LeetCode 링크
- [과제 제출 가이드](docs/submission-guide.md) — 제출 문서에 무엇을 담고, 왜 담는가
- [주간 제출 템플릿](templates/weekly-submission.md) — 복사해서 바로 쓰는 양식
- [제출물](submissions/) — 주차별 제출 폴더

### 폴더 구조

```
.
├── README.md                  ← 지금 보고 있는 문서 (소개·일정·규칙)
├── docs/
│   ├── weekly-problems.md     주차별 문제 리스트 (LeetCode 링크)
│   └── submission-guide.md    과제에 무엇을 담는가
├── templates/
│   └── weekly-submission.md   복사해서 쓰는 제출 양식
└── submissions/
    ├── W02/ ... W10/          주차별 제출 폴더
    └── <github-아이디>.md      각자 여기에 파일 추가
```

---

## Blind 75가 무엇인가

Blind(teamblind.com)에 올라온 익명 글에서 시작된 LeetCode 75문제 큐레이션입니다. 작성자는 400~500문제를 풀어본 경험에서 "유형별 핵심 기법을 가르쳐주는 문제"를 추렸다고 밝혔습니다.

주의할 점: **통계나 기업별 출제 데이터가 아니라 한 개인의 경험적 큐레이션입니다.** Blind가 나중에 "Meta 테크 리드가 정리한 리스트"라고 소개했지만 이는 Blind 측의 사후 서술로, 원문만으로는 확인되지 않습니다. 그래도 유형 커버리지가 좋아 널리 쓰이는 입문 리스트입니다.

---

<a id="schedule"></a>

## 일정

| 회차 | 날짜 | 주제 | 문제 수 |
|---|---|---|---|
| W1 | 9/9 | OT — 운영 방식·제출 규칙 확정 | — |
| W2 | 9/16 | Array | 10 |
| W3 | 9/23 | String | 10 |
| W4 | 9/30 | Linked List + Binary | 10 |
| W5 | 10/7 | Tree 기초 | 7 |
| — | 10/14, 10/21 | 휴회 | — |
| W6 | 10/28 | Tree 심화 + Trie | 7 |
| W7 | 11/4 | Graph | 8 |
| W8 | 11/11 | Matrix + Interval | 9 |
| W9 | 11/18 | DP 1차원 | 6 |
| W10 | 11/25 | DP 심화 + Heap | 8 |

합계 **75문제**. 주차별 문제 목록은 [주차별 문제 리스트](docs/weekly-problems.md)에 있습니다.

---

<a id="rules"></a>

## 규칙

### 1. 목표 설정
매주 시작과 함께, 이번 주 문제 리스트 중 **자신이 몇 문제를 풀 것인지 정하고 공유**합니다.
**최소 3문제, 상한 없음.**

### 2. 인증
GitHub PR로 제출합니다. 코드 원본과 사고 과정을 함께 담습니다.

- 어떤 패턴으로 봤는지
- 왜 그 자료구조인지
- 시간·공간 복잡도
- 엣지 케이스

세부 양식은 [과제 제출 가이드](docs/submission-guide.md)를 따릅니다.

| 항목 | 규칙 |
|---|---|
| 파일 | `submissions/W02/<github-아이디>.md` |
| 브랜치 | `w02/<github-아이디>` |
| PR 제목 | `[W02] <이름> - 5문제` |
| 마감 | 해당 주차 수요일 **20:00 (세션 시작 전)** |

### 3. 정산
매주 선언한 목표 달성에 실패할 때마다 **벌금 4,000원**.

### 4. 분배
모인 벌금은 학기 종료 후 가장 문제를 많이 푼 **3명에게 차등 분배**합니다.

---

## 스터디 시간에는 무엇을 하나

매주 **화이트보드 세션**을 진행합니다.

1. 세션 시작 시 발표자 **3명 랜덤 추첨**
2. 뽑힌 사람이 이번 주 인증한 문제 중 **1문제를 다시 랜덤 추첨**
3. 화이트보드에 설명

### 설명에 반드시 포함할 것

- 입출력 분석
- 자료구조 선택 근거
- 시간·공간 복잡도
- 엣지 케이스

> 이 네 가지는 [제출 템플릿](templates/weekly-submission.md)의 필수 항목과 같습니다.
> 과제를 제대로 썼다면 그 문서가 곧 발표 대본입니다.

### 발표자 추첨 방식

- **비복원 추출**
- 한 번 걸린 사람은 전원이 한 바퀴 돌 때까지 후보에서 제외

---

## 처음 참여하는 사람이 할 일

1. [과제 제출 가이드](docs/submission-guide.md)를 읽습니다. (5분)
2. [주차별 문제 리스트](docs/weekly-problems.md)에서 이번 주 문제를 확인하고, **몇 문제를 풀지 선언**합니다.
3. 저장소를 클론하고 브랜치를 만듭니다.

   ```bash
   git clone https://github.com/blind75-study-boaz-26/problem-solving.git
   cd problem-solving
   git switch -c w02/<github-아이디>
   cp templates/weekly-submission.md submissions/W02/<github-아이디>.md
   ```

4. 문제를 풀고, LeetCode에서 Accepted를 받은 뒤 문서를 채웁니다.
5. 수요일 20:00 전에 PR을 엽니다. PR 제목은 `[W02] <이름> - 5문제` 형식입니다.
