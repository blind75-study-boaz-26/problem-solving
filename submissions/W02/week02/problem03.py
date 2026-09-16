'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        half_len = len(prices) // 2
        max_value = 0 
        min_value = 0
        seen = {}
        if len(prices)%2==0:
            for num in prices[:half_len]:
                min_value = min(prices[:half_len])
                for i in range(half_len):
                    seen[i] = min_value                
            for num in prices[half_len:]:
                max_value = max(prices[half_len:])
            if max_value>min_value:
                return max_value-min_value
            else:
                return 0
        else:
            for num in prices[:half_len]:
                min_value = min(prices[:half_len])
            for num in prices[half_len:]:
                max_value = max(prices[half_len:])
            if max_value>min_value:
                return max_value-min_value
            else:
                return 0

원래는 절반으로 쪼개서 앞쪽에서는 최솟값, 뒤쪽에서는 최댓값 구해서 이익 구하려고 했는데 반례가 너무 많음 --> 중첩 반복문이 너무 많아져서 로직이 복잡해진다.
'''

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# greedy 방식 -> 시간 복잡도 : O(N), 공간 복잡도: O(1)
# 시간 복잡도 : 리스트를 처음부터 끝까지 딱 한 번만 순회(Loop)하기 때문에, 가격 데이터의 개수(N)만큼 시간이 비례해서 늘어난다.
# 공간 복잡도 : 추가로 커다란 배열이나 딕셔너리 같은 자료구조를 만들지 않고, min_price랑 max_profit이라는 변수 몇 개만 기억하면서 돌고 있다. prices 는 기존 문제에서 주어져있어서 알고리즘이 새로 차지하는 공간 복잡도에 포함되지 않는다.
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')  # 최솟값을 무한대로 초기화
        max_profit = 0            # 최대 이익을 0으로 초기화
        
        for price in prices:
            if price < min_price:
                min_price = price  # 더 싼 가격을 만나면 최솟값 갱신
            else:
                profit = price - min_price  # 오늘 팔았을 때의 이익 계산
                if profit > max_profit:
                    max_profit = profit     # 최대 이익 갱신
                    
        return max_profit

    