class Solution:
    def sort(self, input, k):
        result = []
        for _ in range(k + 1):
            result.append((-1, 0))

        for num in input:
            if result[num][0] == -1:
                result[num] = (num, 1)
            else:
                num, count = result[num]
                count += 1
                result[num] = (num, count)

        free_slot = 0
        for i in range(len(result)):
            if result[i][0] != -1:
                result[i], result[free_slot] = result[free_slot], result[i]
                free_slot += 1

        result = result[:free_slot]

        final = []
        for i in range(len(result)):
            num, count = result[i]
            while count:
                final.append(num)
                count -= 1

        return final


a = [42, 31, 0, 22, 4, 6, 7]
b = [42, 31, 0, 0, 22, 22, 31, 22, 7, 7, 4, 3, 3, 3, 3]
c = [0, 0, 0, 0, 0, 0]

sol = Solution()
print(sol.sort(a, 42))
print(sol.sort(b, 42))
print(sol.sort(c, 0))


