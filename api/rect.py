
def overlap_area(rect_1, rect_2):
    x_start = max(rect_1[0][0], rect_2[0][0])
    x_end = min(rect_1[1][0], rect_2[1][0])

    if x_start >= x_end:
        return 0

    y_start = max(rect_1[0][1], rect_2[0][1])
    y_end = min(rect_1[1][1], rect_2[1][1])

    if y_start >= y_end:
       return 0

    return (x_end - x_start) * (y_end - y_start)

if __name__ == "__main__":
    rect_1 = [[2, 2], [4, 4]]
    rect_2 = [[5, 2], [8, 4]]
    print(overlap_area(rect_1, rect_2))
