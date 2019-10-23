def range_merge(a, b):
    i = 0
    j = 0

    ranges = []
    while (i < len(a) and j < len(b)):
        a_start = a[i][0]
        a_end = a[i][1]
        b_start = b[j][0]
        b_end = b[j][1]

        if a_end <= b_end:
            i += 1
        else:
            j += 1

        if a_end >= b_start and b_end >= a_start:
            points = sorted([a_start, a_end, b_start, b_end])
            mid1 = points[1]
            mid2 = points[2]

            ranges.append([mid1, mid2])

    t = 0
    while t < len(ranges) - 1:
        if ranges[t][1] == ranges[t + 1][0]:
            ranges[t:t+2] = [[ranges[t][0], ranges[t+1][1]]]
        t += 1

    return ranges


if __name__ == "__main__":
    a = [[0, 100]]
    b = [[1,5], [2,6], [8,12], [14,15]]
    c = range_merge(a, b)
    print(c)

