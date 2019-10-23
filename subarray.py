def subArray(input, sum):
    result = []
    for start in range(len(input)):
        for end in range(start + 1, len(input)):
            total = 0
            for k in range(start, end + 1):
                total += input[k]
            if total == sum:
                result.append([i for i in range(start, k + 1)])

    print(result)

if __name__ == "__main__":
    input = [2,6,0,9,7,3,1,4,1,10]
    sum = 15
    subArray(input, sum)



