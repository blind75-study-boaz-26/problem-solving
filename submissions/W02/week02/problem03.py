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

'''
이 문제는 Best Time to Buy and Sell Stock 문제이며, 그리디(Greedy) 방식으로 풀이하였다.

핵심 아이디어는 배열을 한 번 순회하면서, 지금까지 본 가격 중 최솟값을 계속 갱신하고, 동시에 오늘 팔았을 때 얻을 수 있는 이익을 계산해서 최댓값을 갱신하는 것이다.

구체적으로 살펴보면, min_price는 무한대로, max_profit은 0으로 초기화한다. 이후 리스트를 순회하며 현재 가격이 지금까지의 최솟값보다 작으면 min_price를 갱신하고, 그렇지 않다면 오늘 가격에서 최솟값을 뺀 값, 즉 오늘 팔았을 때의 이익을 계산하여 max_profit보다 크면 갱신한다.

여기서 조건문을 if-else로 나눈 이유는, 오늘이 지금까지의 최저가라면 그날 사서 그날 파는 것은 의미가 없으므로 이익 계산을 할 필요가 없기 때문이다. 즉 최솟값을 갱신하는 시점과 이익을 계산하는 시점을 분리함으로써, "미래의 최솟값으로 과거에 팔아버리는" 논리적 오류를 방지한다.

시간 복잡도는 O(N)이다. 그 이유는 리스트를 처음부터 끝까지 단 한 번만 순회하기 때문이며, 가격 데이터의 개수 N에 비례해서 실행 시간이 늘어나기 때문이다.

공간 복잡도는 O(1)이다. 그 이유는 별도의 배열이나 딕셔너리 같은 추가 자료구조를 사용하지 않고, min_price와 max_profit이라는 상수 개의 변수만 사용하기 때문이다. 입력으로 주어지는 prices 리스트는 알고리즘이 새로 차지하는 공간이 아니므로 공간 복잡도 계산에서 제외한다.

정리하면, 이 알고리즘은 배열을 한 번만 순회하면서 최솟값과 최대 이익을 동시에 갱신해나가는 그리디 방식이며, 시간 복잡도 O(N), 공간 복잡도 O(1)의 효율적인 풀이이다.
'''