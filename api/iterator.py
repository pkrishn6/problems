from heapq import heappush, heappop

class Iterator:
    def __init__(self, input):
        self.input = input
        self.index = 0
    def hasNext(self):
        return self.index < len(self.input)
    def next(self):
        if not self.hasNext():
            return None
        val = self.input[self.index]
        self.index += 1
        return val

class SuperIterator:
    def __init__(self, iterators):
        self.itrs = iterators
        self.h = []

        for i,itr in enumerate(iterators):
            if itr.hasNext():
                heappush(self.h, (itr.next(), i, itr))

    def hasNext(self):
        return len(self.h) != 0

    def next(self):
        if not self.hasNext():
            return None
        val, index, itr = heappop(self.h)
        if itr.hasNext():
            heappush(self.h, (itr.next(), index, itr))

        return val



if __name__ == "__main__":
    itr1 = Iterator([1,4,7,8,9])
    itr2 = Iterator([2,3,20,21,31,41])
    itr3 = Iterator([])

    superItr = SuperIterator([itr1, itr2, itr3])

    while(superItr.hasNext()):
        print(superItr.next())
