class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_one = self.find_min(prices, -1)
        min_two = self.find_min(prices, min_one)
        
        if prices[min_one] + prices[min_two] <= money:
            return money - prices[min_one] - prices[min_two]
        return money

    def find_min(self, prices, idx):
        res = 1 if idx == 0 else 0

        for i in range(len(prices)):
            if i == idx:
                continue
            if prices[i] < prices[res]:
                res = i

        return res
        