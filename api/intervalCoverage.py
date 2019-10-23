class intervalMerge():
    def __init__(self):
        self.result = []

    def addInterval(self, s, e):
        l = -1
        r = len(self.result) + 1

        for i in range(len(self.result)):
            if self.result[i][1] < s:
                l = max(l, i)
            elif self.result[i][0] > e:
                r = min(r, i)
            else:
                # collision
                s = min(s, self.result[i][0])
                e = max(e, self.result[i][1])


        self.result[l+1:r] = [[s, e]]
        print(self.result)

    def getTotalCoveredLength(self):
        coverage = 0
        for interval in self.result:
            coverage += interval[1] - interval[0]

        return coverage

m = intervalMerge()
m.addInterval(2, 3)
m.addInterval(1, 4)
print(m.getTotalCoveredLength())
m.addInterval(10, 12)
print(m.getTotalCoveredLength())


"""
(2, 3), (1, 4), (10, 12)
"""
