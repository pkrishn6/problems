from collections import defaultdict

def subArray(input, sum):
    d = defaultdict(int)
    result = []
    total = 0
    d[0] = -1

    for i in range(len(input)):
        total += input[i]
        if total - sum in d:
            result.append([k for k in range(d[total - sum] + 1, i + 1)])
        d[total] = i
    print(result)


if __name__ == "__main__":
    input = [6,0,0,9,7,3,1,4,1,10]
    sum = 15
    subArray(input, sum)



