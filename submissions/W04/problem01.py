# https://leetcode.com/problems/valid-anagram/description/?envType=problem-list-v2&envId=oizxjoit
# 시간 복잡도: O(n) - s, t를 각각 한 번씩 순회 (n = 문자열 길이)
# 공간 복잡도: O(1) - 입력 크기와 무관하게 26칸 리스트 2개만 사용
# 이때, len 함수는 파이썬에서 O(1) 이므로, 괜찮음

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 제약 조건 확인 (문제에서 보장하므로 사실 생략 가능)
        # 주의: 파이썬에서 ^는 XOR, 거듭제곱은 **
        if(len(t) <= 5 * (10**4) and 1 <= len(s)):
            # 길이가 다르면 애너그램일 수 없음
            if(len(s)==len(t)):
                # s의 알파벳별 등장 횟수 (인덱스 0~25 = 'a'~'z')
                count_s = [0] * 26
                for c in s:
                    # ord(c) - ord('a'): 글자를 0~25 인덱스로 변환 ('a'→0, 'z'→25)
                    count_s[ord(c)-ord('a')]+=1
                # t의 알파벳별 등장 횟수
                count_t = [0] * 26
                for b in t:
                    count_t[ord(b)-ord('a')]+=1
                # 두 리스트의 모든 칸 값이 같으면 = 모든 글자 개수가 같으면 애너그램
                if(count_s==count_t):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False