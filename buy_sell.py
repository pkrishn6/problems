class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        result: List[List[int]] = []

        count = 0
        i = 0
        while (i < length - 1):
            while (i < length - 1 and prices[i + 1] <= prices[i]):
                i += 1

            if i == (length - 1):
                break

            result.append([i, 0])

            i += 1
            while (i < length - 1 and prices[i + 1] >= prices[i]):
                i += 1

            result[count][1] = i

            count += 1

        for val in result:
            print("Buy and sell", val[0], val[1])
