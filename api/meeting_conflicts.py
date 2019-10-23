class Node:
    def __init__(self, start=-1, end=-1):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.max = self.end

    def insert(self, root, start, end):
        if not root:
            root = Node(start, end)
            return root
        if start <= root.start:
            root.left = self.insert(root.left, start, end)
        else:
            root.right = self.insert(root.right, start, end)

        if end > root.max:
            root.max = end
        return root

    def overlap(self, root, start, end):
        if not root:
            return None
        if start < root.end and root.start < end:
            print("Interval %d:%d conflicts with %d:%d" % (start, end, root.start, root.end))
        if root.left and start <= root.left.max:
            self.overlap(root.left, start, end)
        self.overlap(root.right, start, end)

def overlapIntervals(intervals):
        if not intervals:
            return

        root = Node(intervals[0][0], intervals[0][1])
        for i in range(1, len(intervals)):
            root.overlap(root, intervals[i][0], intervals[i][1])
            root.insert(root, intervals[i][0], intervals[i][1])



if __name__ == "__main__":
    intervals = [ [1,2], [2,3], [3,4], [1,3], [1, 4] ]
    overlapIntervals(intervals)

